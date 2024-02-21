from scipy.stats import binom

n = 10
p = 0.9

for k in range(n + 1):
    prawdopodobienstwo = binom.pmf(k, n, p)
    print("{0} - {1}".format(k, prawdopodobienstwo))

# WYNIKI:

# 0 - 9.99999999999996e-11
# 1 - 8.999999999999996e-09
# 2 - 3.644999999999996e-07
# 3 - 8.748000000000003e-06
# 4 - 0.0001377809999999999
# 5 - 0.0014880347999999988
# 6 - 0.011160260999999996
# 7 - 0.05739562800000001
# 8 - 0.19371024449999993
# 9 - 0.38742048900000037
# 10 - 0.34867844010000004