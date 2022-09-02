import re
from random import choice


class TextGenerator:
    def __init__(self):
        self.bigrams = {}
        self.first_words = []

    def __line_handler(self, string: str, prefix=[]) -> list[str]:
        words = prefix + re.compile('[^а-яА-Я ]').sub(' ', string).lower().split()
        for i in range(2, len(words)):
            if not len(self.first_words):
                self.first_words = [words[0], words[1]]
            if (words[i - 2], words[i - 1]) not in self.bigrams:
                self.bigrams[(words[i - 2], words[i - 1])] = []
            self.bigrams[(words[i - 2], words[i - 1])].append(words[i])
        return words[-2::]

    def __extreme_case(self, prefix: list[str]) -> None:
        if (prefix[0], prefix[1]) not in self.bigrams:
            self.bigrams[(prefix[0], prefix[1])] = []
        self.bigrams[(prefix[0], prefix[1])].append(self.first_words[0])
        if (prefix[1], self.first_words[0]) not in self.bigrams:
            self.bigrams[(prefix[1], self.first_words[0])] = []
        self.bigrams[(prefix[1], self.first_words[0])].append(self.first_words[1])

    def fit(self, input_dir=None) -> None:
        if input_dir is not None:
            with open(input_dir, 'r', encoding='utf-8') as f:
                prefix = []
                for i in f:
                    prefix = self.__line_handler(i, prefix)
                self.__extreme_case(prefix)

    def generate(self, length: int, prefix=None) -> None:
        if prefix is None:
            prefix = choice(list(self.bigrams.keys()))
        for i in range(length):
            word = choice(self.bigrams[prefix])
            prefix = (prefix[1], word)
            print(word, end=' ')
        print()
