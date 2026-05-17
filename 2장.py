from scipy.stats import binom

def _베이즈_정리():
    p_coffee_drinker = 0.65
    p_cancer = 0.005
    p_coffee_drinker_given_cancer = 0.85

    p_cancer_given_coffee_drinker = (p_coffee_drinker_given_cancer *
                                     p_cancer / p_coffee_drinker)

    print(p_cancer_given_coffee_drinker)

def _이항분포_with_사이파이():

    n = 20
    p = 0.9

    for k in range(n + 1):
        probability = binom.pmf(k, n, p)
        print("{0} - {1}".format(k, probability))

if __name__ == '__main__':
    _이항분포_with_사이파이()