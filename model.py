import random
import re


class TextGenerator:
    def __init__(self, n=3):
        self.n_grams = {}
        self.first_n_words = []
        self.n = n

    def __n_grams_creator(self, words: list[str]) -> None:
        for i in range(self.n, len(words)):
            if tuple(words[i - j] for j in range(self.n, 0, -1)) not in self.n_grams:
                self.n_grams[tuple(words[i - j] for j in range(self.n, 0, -1))] = []
            self.n_grams[tuple(words[i - j] for j in range(self.n, 0, -1))].append(words[i])

    def __line_handler(self, string: str, last_n_words: list[str]) -> list[str]:
        words = last_n_words + re.compile('[^а-яА-Я ]').sub(' ', string).lower().split()
        if not len(self.first_n_words) and len(words) > self.n:
            self.first_n_words = [words[j] for j in range(self.n)]
        self.__n_grams_creator(words)
        return words[-self.n::]

    def fit(self, input_dir=None) -> None:
        if input_dir is not None:
            with open(input_dir, 'r', encoding='utf-8') as f:
                last_n_words = []
                for i in f:
                    last_n_words = self.__line_handler(i, last_n_words)
                self.__n_grams_creator(last_n_words + self.first_n_words)

    def generate(self, length: int, prefix=None, seed=None) -> None:
        if seed is not None:
            random.seed(seed)
        if prefix is None:
            prefix = random.choice(list(self.n_grams.keys()))
        else:
            prefix = tuple(prefix[-self.n:])
        for i in range(length):
            word = random.choice(self.n_grams[prefix])
            prefix = prefix[1:] + (word,)
            print(word, end=' ')
        print()
