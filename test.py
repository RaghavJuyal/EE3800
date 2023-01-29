import numpy as np
# import the function from your submission "Serial_69.py"
from Serial_69 import mutual_information
# generating a probability mass function ‘pmf’
# pmf = np.random.rand(10_000)
# pmf = pmf / sum(pmf)
pmf = np.load('Sample_pmf.npy')

# computing the mutual information between
# two random variables X_i and X_j, i not equal to j
# i, j belong to the set {0,1,2,3}
i = 2
j = 3
MI = mutual_information(pmf, i, j)
print(MI)
