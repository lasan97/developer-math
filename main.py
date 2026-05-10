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

def _대수_표현식():
    x = symbols('x')
    expr = x**2 / x**5
    print(expr)

def _로그함수():
    x = log(8, 2)
    print(x)

def _복리이자_계산():
    p = 100 # 투자금
    r = 0.20 # 이자율
    t = 2.0 # 연도 수
    n = 12 # 연간 복리 적용 횟수

    a = p * (1 + (r/n))**(n * t) # 원금 + 복리 이자

    print(a)

def _연속_복리이자_계산():
    p = 100  # 원금, 시작 금액
    r = 0.20  # 연이자
    t = 2.0  # 연도 수

    a = p * exp(r*t)

    print(a)

if __name__ == '__main__':
    _연속_복리이자_계산()