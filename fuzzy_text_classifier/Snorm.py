class Snorm:

    @staticmethod
    def algebraic(a: float, b: float):
        return a+b-a*b

    @staticmethod
    def einstein(a: float, b: float):
        return (a+b)/(1+a*b)
