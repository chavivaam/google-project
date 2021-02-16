from autocompleter import get_completions
from model import DataModel

print('Loading the data...')
data = DataModel()


def get_input_from_user(output_str):
    val = input(output_str)
    return val


def print_completions(completions):
    for i, auto_complete_obj in enumerate(completions):
        str_ = auto_complete_obj.completed_sentence
        path_ = auto_complete_obj.source_text
        offset = auto_complete_obj.offset
        score = auto_complete_obj.score
        print("{}. {} ({}, offset: {}), score: {}".format(i + 1, str_, path_, offset, score))


def get_most_relevant(completions):
    sorted_by_score = sorted(completions, key=lambda tup: tup[2], reverse=True)
    return sorted_by_score[:5]


def get_best_k_completions(prefix: str):
    storage_tree = data.get_completions_tree()

    data_dict = data.get_base_data()
    completions = get_completions(prefix, storage_tree)
    filtered_suggestions = get_most_relevant(completions)

    # conversion from tuple to AutoCompleteData
    auto_complete_data_lst = []
    for suggest in filtered_suggestions:
        suggest_id = suggest[0]
        offset = suggest[1]
        score = suggest[2]
        suggest_data = data_dict.get(suggest_id)
        suggest_data.init_offset(offset)
        suggest_data.init_score(score)
        auto_complete_data_lst.append(suggest_data)

    return auto_complete_data_lst


def run():
    while True:
        to_end = False
        print_before = "The system is ready. Enter your text:\n"
        input_val = ""
        while not to_end:
            input_val = input_val + get_input_from_user(print_before)
            print_before = input_val
            if input_val[-1] == '#':
                to_end = True
            best_completions = get_best_k_completions(input_val)
            print_completions(best_completions)


run()
