from typing import List
from collections import defaultdict
from .FuzzySet import FuzzySet
from .Tnorm import Tnorm
from .Snorm import Snorm
import operator


class TextClassifier:

    def __init__(self, tokenizer=None):
        self.tokenizer = tokenizer
        self.documents = defaultdict(list)

    def add_document(self, fs: FuzzySet, category: str):
        self.documents[category].append(fs)

    def train(self, text: str, category: str):

        fs = self.fuzzyfy(self.tokenize(text))
        self.documents[category].append(fs)

    def classify(self, text: str) -> dict:

        similarities = {}

        fs = self.fuzzyfy(self.tokenize(text))

        for category in self.documents.keys():
            similarities[category] = self.similarity(fs, category)

        ret = dict( sorted(similarities.items(), key=operator.itemgetter(0), reverse=True))
        out = []

        for k, v in ret.items():
            out.append({k: v})

        return out

    def tokenize(self, text: str) -> List[str]:
        if self.tokenizer is None:
            return text.split()
        else:
            return self.tokenizer.tokenize(text)

    @staticmethod
    def fuzzyfy(words: List[str]) -> FuzzySet:

        terms = {}

        for word in words:
            if word in terms:
                terms[word] += 1
            else:
                terms[word] = 1

        maximum_key = max(terms, key=terms.get)
        maximum_value = terms[maximum_key]

        for term in terms:
            terms[term] = round(terms.get(term) / maximum_value, 2)

        return FuzzySet(terms)

    def __dist(self, term: str, category: str):

        numerator = 0
        denominator = 0

        for doc in self.documents[category]:
            numerator += doc.terms.get(term, 0)

        for docs in self.documents.values():
            for doc in docs:
                denominator += doc.terms.get(term, 0)

        if denominator == 0:
            return 0

        return numerator/denominator

    def __r(self, term: str, category: str):

        numerator = self.__dist(term, category)
        dists = []

        for cat in self.documents.keys():
            dists.append(self.__dist(term, cat))

        denominator = max(dists)

        if denominator == 0:
            return 0

        return numerator/denominator

    def similarity(self, doc: FuzzySet, category: str):
        numerator = 0
        denominator = 0

        for term in doc.terms:
            numerator += Tnorm.einstein(self.__r(term, category), doc.terms.get(term, 0))
            denominator += Snorm.einstein(self.__r(term, category), doc.terms.get(term, 0))

        if denominator == 0:
            return 0

        return abs(numerator/denominator)