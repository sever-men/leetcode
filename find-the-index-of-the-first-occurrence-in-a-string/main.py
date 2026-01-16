class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        return int(str(self.sqrt(x)).split('.')[0])


    def sqrt(self, number):
        eps = 1e-1
        x = 1

        while (abs(x * x - number) > eps):
            x = (x + number / x) / 2
        return x
