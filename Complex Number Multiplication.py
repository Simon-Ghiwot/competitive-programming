class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1[0 : len(num1) - 1]
        num1Real, num1Imaginary = map(int, num1.split("+"))

        num2 = num2[0 : len(num2) - 1]
        num2Real, num2Imaginary = map(int, num2.split("+"))

        resultReal = num1Real * num2Real
        resultReal -= num1Imaginary * num2Imaginary

        resultImaginary = num1Real * num2Imaginary
        resultImaginary += num1Imaginary * num2Real
        
        return str(resultReal) + "+" + str(resultImaginary) + "i"
