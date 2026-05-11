from sympy import *
from sympy.plotting import plot3d
from math import log

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

def _자연로그():
    l = log(10)
    print(l)

def _극한():
    n = symbols('n')
    f =  (1 + (1/n))**n
    result = limit(f, n, oo)

    print(result)
    print(result.evalf())

def _미분():
    def derivative_x(f, x, step_size):
        m = (f(x + step_size) - f(x)) / ((x + step_size) - x)
        return m

    def my_function(x):
        return x ** 2

    slope_at_2 = derivative_x(my_function, 2, 0.00001)

    print(slope_at_2)

def _도함수():
    x = symbols('x')

    f = x**2

    # 이 함수의 도함수를 계산합니다.
    dx_f = diff(f)
    print(dx_f)
    print(dx_f.subs(x, 2))

def _미분_계산기():
    def f(x):
        return x ** 2
    def d_f(x):
        return x * 2
    slope_at_2 = d_f(2.0)

    print(slope_at_2)

def _편도함수():
    x,y = symbols('x y')

    f = 2*x**3 + 3*y**3

    # x와 y에 대한 편도함수 계산
    dx_f = diff(f, x)
    dy_f = diff(f, y)

    print(dx_f)
    print(dy_f)

    plot3d(f)

def _극한_기울기():
    x,s = symbols('x s')

    f = x**2
    slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)

    slope_2 = slope_f.subs(x, 2)

    result = limit(slope_2, s, 0)

    print(result)

def _극한_도함수():
    x,s = symbols('x s')

    f = x**2

    slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)

    # s 가 0에 무한히 가까워질 때 도함수를 계산
    result = limit(slope_f, s, 0)

    print(result)

if __name__ == '__main__':
    _극한_도함수()