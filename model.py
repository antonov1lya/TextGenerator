import random
import re
import sys


class TextGenerator:
    def __init__(self, n=3):
        self.n_grams = {}
        self.n_grams_keys = []
        self.n = n

    def __line_tokenizer(self, string: str, last_n_words: list[str]) -> list[str]:
        words = last_n_words + re.compile('[^а-яА-Я ]').sub(' ', string).lower().split()
        for i in range(self.n, len(words)):
            if tuple(words[i - j] for j in range(self.n, 0, -1)) not in self.n_grams:
                self.n_grams[tuple(words[i - j] for j in range(self.n, 0, -1))] = []
            self.n_grams[tuple(words[i - j] for j in range(self.n, 0, -1))].append(words[i])
        return words[-self.n::]

    def fit(self, input_dir=None) -> None:
        last_n_words = []
        if input_dir is not None:
            with open(input_dir, 'r', encoding='utf-8') as f:
                for i in f:
                    last_n_words = self.__line_tokenizer(i, last_n_words)
        else:
            print('Введите текст в консоль. По окончании ввода введите символ EOF (Ctrl+D в UNIX, Ctrl+Z в Windows).')
            for i in sys.stdin:
                last_n_words = self.__line_tokenizer(i, last_n_words)
        self.n_grams_keys = list(self.n_grams.keys())

    def generate(self, length: int, prefix=None, seed=None) -> str:
        if not len(self.n_grams):
            return 'Невозможно сгенерировать текст! Модель пустая.'
        if seed is not None:
            random.seed(seed)
        if prefix is None:
            prefix = random.choice(self.n_grams_keys)
        else:
            prefix = tuple(prefix[-self.n:])
        text = list(prefix) + []
        for i in range(length - self.n):
            if prefix not in self.n_grams:
                prefix = random.choice(self.n_grams_keys)
            word = random.choice(self.n_grams[prefix])
            prefix = prefix[1:] + (word,)
            text.append(word)
        return ' '.join(text)
