class FiniteFieldElement:
    """Reprezintă un element în corpul finit F_p cu operații modulare."""
    def __init__(self, value: int, prime: int):
        self.prime = prime
        self.value = value % prime

    def __add__(self, other):
        val = (self.value + other.value) if isinstance(other, FiniteFieldElement) else (self.value + other)
        return FiniteFieldElement(val, self.prime)

    def __sub__(self, other):
        val = (self.value - other.value) if isinstance(other, FiniteFieldElement) else (self.value - other)
        return FiniteFieldElement(val, self.prime)

    def __mul__(self, other):
        val = (self.value * other.value) if isinstance(other, FiniteFieldElement) else (self.value * other)
        return FiniteFieldElement(val, self.prime)

    def inverse(self):
        """Calculează inversul multiplicativ folosind Mica Teoremă a lui Fermat."""
        return FiniteFieldElement(
            pow(self.value, self.prime - 2, self.prime),
            self.prime
        )

    def __truediv__(self, other):
        inv = other.inverse() if isinstance(other, FiniteFieldElement) else FiniteFieldElement(other, self.prime).inverse()
        return self * inv
