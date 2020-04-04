import pytest
from fuzzy_text_classifier import Snorm

data = [
    (0.1, 0.2, 0.28, 0.29),
    (0.3, 0.6, 0.72, 0.76),
    (0.34, 1, 1, 1),
    (0.5, 0, 0.5, 0.5)
];

class TestSnorm:

    @pytest.mark.parametrize("a,b,r1, r2", data)
    def test_algebraic(self, a, b, r1, r2):
        assert round(Snorm.algebraic(a, b), 2) == r1

    @pytest.mark.parametrize("a,b,r1, r2", data)
    def test_einstein(self, a, b, r1, r2):
        assert round(Snorm.einstein(a, b), 2) == r2
