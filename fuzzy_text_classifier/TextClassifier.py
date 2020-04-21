from typing import List
from collections import defaultdict, Counter
from .FuzzySet import FuzzySet
from .Tnorm import Tnorm
from .Snorm import Snorm
from .AbstractTokenizer import AbstractTokenizer


class TextClassifier:

    def __init__(self, tokenizer: AbstractTokenizer = None):

        if tokenizer is not None and not isinstance(tokenizer, AbstractTokenizer):
            raise ValueError('instance of AbstractTokenizer required')

        self.tokenizer = tokenizer
        self.documents = defaultdict(list)

    def add_document(self, fs: FuzzySet, category: str):
        self.documents[category].append(fs)

    def train(self, text: str, category: str):

        fs = self.fuzzyfy(self.tokenize(text))
        self.documents[category].append(fs)

    def classify(self, text: str) -> []:

        similarities = {}
        max_sim = 0

        fs = self.fuzzyfy(self.tokenize(text))

        for category in self.documents.keys():
            similarities[category] = self.similarity(fs, category)
            if similarities[category] > max_sim:
                max_sim = similarities[category]

        if max_sim > 0:
            for category in self.documents.keys():
                similarities[category] = similarities[category] / max_sim

        out = []

        for k, v in sorted(similarities.items(), reverse=True, key=lambda key: key[1]):
            out.append({k: v})

        return out

    def tokenize(self, text: str) -> List[str]:
        if self.tokenizer is None:
            return text.split()
        else:
            return self.tokenizer.tokenize(text)

    @staticmethod
    def fuzzyfy(words: List[str]) -> FuzzySet:

        c = Counter(words)
        maximum_value = c.most_common(1)[0][1]
        d = dict(c)
        terms = {k:round(d[k]/maximum_value,2) for k in d}
        return FuzzySet(terms)

    def __dist(self, term: str, category: str):

        numerators = []
        denominators = []

        for doc in self.documents[category]:
            try:
                numerators.append(doc.terms[term])
            except KeyError:
                pass

        for docs in self.documents.values():
            for doc in docs:
                try:
                    denominators.append(doc.terms[term])
                except KeyError:
                    pass

        try:
            return sum(numerators)/sum(denominators)
        except ZeroDivisionError:
            return 0

    def __r(self, term: str, category: str):

        numerator = self.__dist(term, category)
        denominator = 0

        for cat in self.documents.keys():
            dist = self.__dist(term, cat)
            if dist > denominator:
                denominator = dist

        try:
            return numerator / denominator
        except ZeroDivisionError:
            return 0

    def similarity(self, doc: FuzzySet, category: str):
        numerators = []
        denominators = []

        for term in doc.terms:
            r = self.__r(term, category)
            s = doc.terms.get(term, 0)
            numerators.append(Tnorm.einstein(r, s))
            denominators.append(Snorm.einstein(r, s))

        try:
            return abs(sum(numerators)/sum(denominators))
        except ZeroDivisionError:
            return 0
