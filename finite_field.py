class FiniteFieldElement:
    """Element al corpului finit F_p."""

    def __init__(self, value: int, prime: int):
        if prime <= 1:
            raise ValueError("Modulul trebuie sa fie un numar intreg mai mare decat 1.")

        self.prime = prime
        self.value = value % prime

    def __add__(self, other):
        if isinstance(other, FiniteFieldElement):
            if other.prime != self.prime:
                raise ValueError("Elementele trebuie sa apartina aceluiasi corp.")
            value = self.value + other.value
        else:
            value = self.value + other

        return FiniteFieldElement(value, self.prime)

    def __sub__(self, other):
        if isinstance(other, FiniteFieldElement):
            if other.prime != self.prime:
                raise ValueError("Elementele trebuie sa apartina aceluiasi corp.")
            value = self.value - other.value
        else:
            value = self.value - other

        return FiniteFieldElement(value, self.prime)

    def __mul__(self, other):
        if isinstance(other, FiniteFieldElement):
            if other.prime != self.prime:
                raise ValueError("Elementele trebuie sa apartina aceluiasi corp.")
            value = self.value * other.value
        else:
            value = self.value * other

        return FiniteFieldElement(value, self.prime)

    def inverse(self):
        """Calculeaza inversul multiplicativ pentru un element nenul."""

        if self.value == 0:
            raise ZeroDivisionError("Zero nu are invers multiplicativ in F_p.")

        return FiniteFieldElement(pow(self.value, self.prime - 2, self.prime), self.prime)

    def __truediv__(self, other):
        if isinstance(other, FiniteFieldElement):
            if other.prime != self.prime:
                raise ValueError("Elementele trebuie sa apartina aceluiasi corp.")
            inverse = other.inverse()
        else:
            inverse = FiniteFieldElement(other, self.prime).inverse()

        return self * inverse

    def __repr__(self):
        return f"FiniteFieldElement({self.value}, {self.prime})"
