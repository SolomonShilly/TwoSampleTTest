from sympy import Matrix

class CramersRule:
    def __init__(self, A, B):
        self.X = []
        self.A = A
        self.B = B
        self.column = A.cols

    def checker(self):
        return self.A.det() != 0

    def matrixCalculator(self):
        detA = self.A.det()

        for i in range(self.column):
            Ai = self.A.copy()
            Ai[:, i] = self.B
            detI = Ai.det()
            Xi = detI / detA
            self.X.append(Xi)
        return self.X

    def solver(self):
        print(self.checker(), '\n')
        if self.checker():
            self.matrixCalculator()
            n = 1
            for i in self.X:
                print(f'x{n} = {i}')
                n += 1
        else:
            if self.matrixCalculator() == 0:
                print("System is consistent and has infinite solutions")
            else:
                print("System is inconsistent and has no solution")

class main:
    def __init__(self):
        A = Matrix([
            [2, 3, -4, 5, 6],
            [1, -2, 3, -4, 5],
            [3, 1, 2, 4, -1],
            [2, -3, 4, 1, 5],
            [4, 2, 3, -1, 2]
        ])

        B = Matrix([10, 20, 15, 25, 30])

        # A = Matrix([[2, 4, -6], [3, 6, -9], [4, -7, 1]])

        # B = Matrix([19, 30, 15])

        solution = CramersRule(A, B)
        solve = solution.solver()

main()