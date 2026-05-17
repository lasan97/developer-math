from scipy.stats import binom
from scipy.stats import beta

def _베이즈_정리():
    p_coffee_drinker = 0.65
    p_cancer = 0.005
    p_coffee_drinker_given_cancer = 0.85

    p_cancer_given_coffee_drinker = (p_coffee_drinker_given_cancer *
                                     p_cancer / p_coffee_drinker)

    print(p_cancer_given_coffee_drinker)

def _이항분포():

    n =  10 # 전체 시도 횟수
    k = 8 # 성공 횟수
    p = 0.9 # 한 번 성공할 확률

    # P(X) = C(n,k) * p**k * (1-p)**(n-k)
    probability = binom.pmf(k, n, p)
    print(probability)


def _이항분포_with_사이파이():

    n = 20
    p = 0.9

    for k in range(n + 1):
        probability = binom.pmf(k, n, p)
        print("{0} - {1}".format(k, probability))

def _베타분포_with_사이파이():

    a = 8
    b = 2

    # 최대 90%, 0.0 에서 0.9까지의 면적
    p = beta.cdf(0.90, a,b)

    # 그래프 왼쪽 면적
    print(p)

    # 그래프 오른쪽 면적
    # 0.9 에서 1까지의 면적
    print(1 - p)

    a = 30 # 30번 성공
    b = 6 # 6번 실패
    p = 1.0 - beta.cdf(0.90, a,b)

    # 더 많은 시도
    print(p)

if __name__ == '__main__':
    _베타분포_with_사이파이()
