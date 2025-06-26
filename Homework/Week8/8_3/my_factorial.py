class Fac:
    def loop(self, n):
        result = 1
        sequence = []
        for i in range(n, 0, -1):
            result *= i
            sequence.append(str(i))
        print(f"{n}! = {'*'.join(sequence)}")
        print(f"{n}! = {result}")

    def recursive(self, n):
        if n == 1:
            return 1
        else:
            return n * self.recursive(n - 1)
