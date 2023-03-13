# import the function from your submission "Serial_7.py"
from Serial_69 import lrt
# threshold for likelihood ratio test
T = 3.5
# computing type-I and type-II error rates
alpha, beta = lrt(T)
print(alpha)
print(beta)
