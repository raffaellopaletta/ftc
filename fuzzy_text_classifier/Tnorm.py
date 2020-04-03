class Tnorm:

    @staticmethod
    def algebraic(a: float, b: float):
        return a*b

    @staticmethod
    def einstein(a: float, b: float):
        return (a*b)/(2-(a+b-(a*b)))
