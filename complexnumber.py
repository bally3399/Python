class Complex:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __add__(self, other):
        return Complex(self.left + other.left, self.right + other.right)

    def __sub__(self, other):
        return Complex(self.left - other.left, self.right - other.right)

    def __truediv__(self, other):
        return self.left / other.left and self.right / other.right

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __gt__(self, other):
        return self.left > other.left and self.right > other.right

    def __iadd__(self, other):
        return Complex(self.left + other.left, self.right + other.right)

    def __ge__(self, other):
        return self.left >= other.left and self.right + other.right

    def __mod__(self, other):
        return self.left % self.left and self.right % other.right

    def __pow__(self, power):
        return self.left ** power.left and self.right ** power.right

    def __repr__(self):
        return f'{self.left}j {'+' if self.right > 0 else "-"} {abs(self.right)}i'


c1 = Complex(2, 3)
c2 = Complex(5, 5)
c3 = Complex(2, 3)
print(c1)
print(c3)
print(c2)
print(c1 + c2)
print(c1 - c2)
print(c1 == c3)
print(c1 != c3)
print(c2 > c1)
print(c2 < c1)
c2 += c1
print(c2)
print(c2 / c1)
print(c2 >= c1)
print(c2 % c1)
print(c2 ** c1)
