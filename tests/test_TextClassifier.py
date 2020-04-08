import pytest
from fuzzy_text_classifier import TextClassifier
from fuzzy_text_classifier import AbstractTokenizer
from fuzzy_text_classifier import FuzzySet
from collections import defaultdict


class MockTokenizer(AbstractTokenizer):

    def tokenize(self, text):
        tokens = text.split()
        tokens.remove('this')
        return tokens


class TestTextClassifier:

    def test__init(self):
        tc = TextClassifier()
        assert tc.tokenizer is None
        assert isinstance(tc.documents, defaultdict) is True

        with pytest.raises(ValueError):
            TextClassifier([])

    def test_add_document(self):
        fs = FuzzySet({'a': 0, 'b': 0.5, 'c': 1})
        tc = TextClassifier()
        tc.add_document(fs, 'test')
        assert len(tc.documents['test']) == 1
        assert isinstance(tc.documents['test'][0], FuzzySet)
        terms = tc.documents['test'][0].terms
        assert terms['a'] == 0
        assert terms['b'] == 0.5
        assert terms['c'] == 1

    def test_tokenize(self):
        text = "this is some text and we wont to tokenize it"
        tc = TextClassifier()
        tokens = tc.tokenize(text)
        assert len(tokens) == 10

        tokenizer = MockTokenizer()
        tc = TextClassifier(tokenizer)
        tokens = tc.tokenize(text)
        assert len(tokens) == 9

    def test_fuzzify(self):
        text = 'a a a b b c'
        tc = TextClassifier()
        fs = tc.fuzzyfy(tc.tokenize(text))
        assert isinstance(fs, FuzzySet) is True
        terms = fs.terms
        assert terms['a'] == 1.00
        assert terms['b'] == 0.67
        assert terms['c'] == 0.33

    def test_train(self):
        text = 'a a a b b c'
        tc = TextClassifier()
        tc.train(text, 'test')
        assert len(tc.documents['test']) == 1
        assert isinstance(tc.documents['test'][0], FuzzySet)
        terms = tc.documents['test'][0].terms
        assert terms['a'] == 1.00
        assert terms['b'] == 0.67
        assert terms['c'] == 0.33

    def test_similarity(self):
        tc = TextClassifier()
        doc1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi semper luctus convallis. Cras accumsan iaculis tortor at ullamcorper. Donec eu aliquam lorem, in facilisis ante. '
        tc.train(doc1, 'cat1')
        text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi semper luctus convallis. Cras accumsan iaculis tortor at ullamcorper. Donec eu aliquam lorem, in facilisis ante. '
        assert tc.similarity(tc.fuzzyfy(tc.tokenize(text)), 'cat1') == 1
        text = 'any word inside this document'
        assert tc.similarity(tc.fuzzyfy(tc.tokenize(text)), 'cat1') == 0

    def test_classify(self):
        tc = TextClassifier()
        doc1 = 'a b c d e g f h'
        doc2 = 'i l m n o a b c'
        tc.train(doc1, 'cat1')
        tc.train(doc2, 'cat2')
        ranking = tc.classify('a b c d')
        keys = list(ranking[0])
        assert keys[0] == 'cat1'



