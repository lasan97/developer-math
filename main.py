from sympy import *
from sympy.plotting import plot3d

def _선형함수():
    x = symbols('x')
    f = 2*x + 1
    plot(f)

def _2차함수():
    x = symbols('x')
    f = x**2 + 1
    plot(f)

def _3차원그래프():
    x, y = symbols('x y')
    f = 2*x + 3*y
    plot3d(f)

if __name__ == '__main__':
    _3차원그래프()