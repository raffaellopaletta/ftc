import pytest
from fuzzy_text_classifier import FuzzySet


terms = {'a': 0, 'b': 0.5, 'c': 1}
fs = FuzzySet(terms)


class TestFuzzySet:

    def test_terms(self):
        assert terms == fs.terms

    def test_terms_setter(self):
        with pytest.raises(ValueError):
            fs.terms = {'a': 2}

