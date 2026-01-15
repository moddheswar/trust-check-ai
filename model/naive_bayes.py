from math import log
from utils.preprocessing import preprocess_texts

class NaiveBayesClassifier:
    def __init__(self):
        self.Safe_dict = {}
        self.Risky_dict = {}
        self.Safe_words = 0
        self.Risky_words = 0
        self.vocab = set()
        self.prior_safe = 0
        self.prior_risky = 0

    def train(self, safe_statements, risky_statements):
        self.Safe_tokens = preprocess_texts(safe_statements)
        self.Risky_tokens = preprocess_texts(risky_statements)

        # count words
        for lst in self.Safe_tokens:
            for token in lst:
                self.Safe_words += 1
                self.Safe_dict[token] = self.Safe_dict.get(token, 0) + 1

        for lst in self.Risky_tokens:
            for token in lst:
                self.Risky_words += 1
                self.Risky_dict[token] = self.Risky_dict.get(token, 0) + 1

        # vocab
        self.vocab = set(list(self.Safe_dict.keys()) + list(self.Risky_dict.keys()))

        # priors
        total_statements = len(safe_statements) + len(risky_statements)
        self.prior_safe = log(len(safe_statements) / total_statements)
        self.prior_risky = log(len(risky_statements) / total_statements)

    def predict(self, statement):
        tokens = preprocess_texts([statement])[0]
        score_safe = self.prior_safe
        score_risky = self.prior_risky

        for w in tokens:
            count_safe = self.Safe_dict.get(w, 0)
            count_risky = self.Risky_dict.get(w, 0)
            score_safe += log((count_safe + 1) / (self.Safe_words + len(self.vocab)))
            score_risky += log((count_risky + 1) / (self.Risky_words + len(self.vocab)))

        if score_risky > score_safe:
            return "Risky"
        else:
            return "Safe"
