import pytest
from fuzzy_text_classifier import FuzzySet
from collections import defaultdict

terms = {'a': 0, 'b': 0.5, 'c': 1.0}
fs = FuzzySet(terms)


class TestFuzzySet:

    def test_terms(self):
        assert terms == fs.terms
        assert isinstance(fs.terms, defaultdict)
        fs.terms = terms
        assert isinstance(fs.terms, defaultdict)

    def test_terms_setter(self):
        with pytest.raises(ValueError):
            fs.terms = {'a': 2}

