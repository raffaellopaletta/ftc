import pytest
from fuzzy_text_classifier import Tnorm

data = [
    (0.1, 0.2, 0.02, 0.01),
    (0.3, 0.6, 0.18, 0.14),
    (0.34, 1, 0.34, 0.34),
    (0.5, 0, 0, 0)
];

class TestTnorm:

    @pytest.mark.parametrize("a,b,r1, r2", data)
    def test_algebraic(self, a, b, r1, r2):
        assert round(Tnorm.algebraic(a, b), 2) == r1

    @pytest.mark.parametrize("a,b,r1, r2", data)
    def test_einstein(self, a, b, r1, r2):
        assert round(Tnorm.einstein(a, b), 2) == r2
