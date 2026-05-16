from sympy import *
from sympy.plotting import plot3d
from math import log

def _베이즈_정리():
    p_coffee_drinker = 0.65
    p_cancer = 0.005
    p_coffee_drinker_given_cancer = 0.85

    p_cancer_given_coffee_drinker = (p_coffee_drinker_given_cancer *
                                     p_cancer / p_coffee_drinker)

    print(p_cancer_given_coffee_drinker)

if __name__ == '__main__':
    _베이즈_정리()