from data_parser import clear_str


def update_suggestions(suggestions, possible_suggestions):
    for suggest in possible_suggestions:
        suggest_id = suggest[0]
        current_suggest = suggestions.get(suggest_id)
        if current_suggest is None:
            suggestions[suggest_id] = suggest
        else:
            current_max_score = suggestions[suggest_id][2]
            if suggest[2] > current_max_score:
                suggestions[suggest_id] = suggest


def get_suggestions(input_, substrs_tree):
    temp_tree = substrs_tree
    suggestion = {}
    for letter_index, letter in enumerate(input_):
        possible_suggestions = get_suggestion_with_replace_letter(input_, temp_tree, letter_index)
        update_suggestions(suggestion, possible_suggestions)

        possible_suggestions = get_suggestion_with_redundant_letter(input_, temp_tree, letter_index)
        update_suggestions(suggestion, possible_suggestions)

        possible_suggestions = get_suggestion_with_missed_letter(input_, temp_tree, letter_index)
        update_suggestions(suggestion, possible_suggestions)

        if letter in temp_tree.children.keys():
            temp_tree = temp_tree.children[letter]
        else:
            return suggestion.values()

    suggestions_lst = []
    for suggest in temp_tree.data:
        suggest_info = (suggest[0], suggest[1], 2 * len(input_))
        suggestions_lst.append(suggest_info)

    update_suggestions(suggestion, suggestions_lst)
    return suggestion.values()



def get_suggestion_with_replace_letter(input_, sub_tree, letter_index):
    suggestions = []
    temp_tree = sub_tree
    counter = letter_index + 1
    for key, child in temp_tree.children.items():
        child_suggest = get_suggestions_subtree(input_, letter_index + 1, child)
        suggestions = suggestions + child_suggest
    suggestions_info = []
    for suggest in suggestions:

        decrease_score = get_fine(counter, 'replace')
        score = 2 * (len(input_) - 1) - decrease_score
        suggest_info = (suggest[0], suggest[1], score)
        suggestions_info.append(suggest_info)
    return suggestions_info


def get_suggestions_subtree(input_, letter_index, sub_tree):
    temp_tree = sub_tree
    while letter_index < len(input_):
        letter = input_[letter_index]
        if letter in temp_tree.children.keys():
            temp_tree = temp_tree.children[letter]
        else:
            return []
        letter_index += 1
    return temp_tree.data


def get_fine(index, error_type):
    replace_error = {1: 5, 2: 4, 3: 3, 4: 2}
    redundant_missed_error = {1: 10, 2: 8, 3: 6, 4: 4}
    fine = None
    if error_type == 'replace':
        fine = replace_error.get(index, 1)
    elif error_type == 'missed' or error_type == 'redundant':
        fine = redundant_missed_error.get(index, 2)
    return fine


def get_suggestion_with_missed_letter(input_, sub_tree, letter_index):
    suggestions = []
    counter = letter_index + 1
    for key, child in sub_tree.children.items():
        child_suggest = get_suggestions_subtree(input_, letter_index, child)
        suggestions = suggestions + child_suggest
    suggestions_info = []
    for suggest in suggestions:
        decrease_score = get_fine(counter, 'missed')
        score = 2 * (len(input_)) - decrease_score
        suggest_info = (suggest[0], suggest[1], score)
        suggestions_info.append(suggest_info)
    return suggestions_info


def get_suggestion_with_redundant_letter(input_, sub_tree, letter_index):
    counter = letter_index + 1
    suggestions = get_suggestions_subtree(input_, letter_index + 1, sub_tree)
    suggestions_info = []
    for suggest in suggestions:
        decrease_score = get_fine(counter, 'redundant')
        score = 2 * (len(input_) - 1) - decrease_score
        suggest_info = (suggest[0], suggest[1], score)
        suggestions_info.append(suggest_info)

    return suggestions_info


def get_completions(input, storage_tree):
    cleared_input = clear_str(input)
    suggestions = get_suggestions(cleared_input, storage_tree)
    return suggestions



