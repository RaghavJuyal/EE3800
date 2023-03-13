import math


def n_digit(number, n):
    return number // 10**n % 10


def mutual_information(pmf, i, j):
    pmf_i = [0] * 10
    pmf_j = [0] * 10
    pmf_ij = [0] * 100
    for k in range(10000):

        pmf_i[n_digit(k, i)] += pmf[k]
        pmf_j[n_digit(k, j)] += pmf[k]
        pmf_ij[10*n_digit(k, i)+n_digit(k, j)] += pmf[k]

    H_i = 0
    for k in range(10):
        if pmf_i[k] == 0:
            continue
        H_i += pmf_i[k] * math.log2(1/pmf_i[k])

    H_j = 0
    for k in range(10):
        if pmf_j[k] == 0:
            continue
        H_j += pmf_j[k] * math.log2(1/pmf_j[k])

    H_ij = 0
    for k in range(100):
        if pmf_ij[k] == 0:
            continue
        H_ij += pmf_ij[k] * math.log2(1/pmf_ij[k])

    H_i_given_j = H_ij - H_j
    MI = H_i - H_i_given_j

    return MI
