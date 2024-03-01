class SquareRoot:
    def __init__(self, C, D,  H):
        self.C = C
        self.D = D
        self.H = H

    def square_root(self, C, D, H):
        self.D = input("Enter a value")
        self.C = 50
        self.H = 30

    def __repr__(self):
        return f"C :{self.C},D :{self.D},H : {self.H}"


C = 50
D = 75
H = 30
Q = ([(2 * C * D) / H])

print(list(map(lambda Q: ([(2 * C * D) / H]), Q)))




def main():
    squareRoot = SquareRoot(C, D, H)

    squareRoot.square_root(100, 150, 180)


if __name__ == "__main__":
    main()
