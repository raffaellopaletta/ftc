class FuzzySet:

    def __init__(self, terms: dict):
        self.terms = terms

    @property
    def terms(self):
        return self._terms

    @terms.setter
    def terms(self, terms: dict):
        for k, v in terms.items():
            if v < 0 or v > 1:
                raise ValueError('terms value must be >= 0 and <= 1')

        self._terms = terms
