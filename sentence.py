from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int

    def init_completed_sentence(self, sentence):
        self.completed_sentence = sentence

    def init_source_text(self, path):
        self.source_text = path

    def init_offset(self, offset):
        self.offset = offset

    def init_score(self, score):
        self.score = score
