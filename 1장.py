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

def _x에대한_z도함수():
    # ㅇ
    x = symbols('x')
    z = (x**2 + 1)**3 -2
    dz_dx = diff(z, x)
    print(dz_dx)

def _연쇄법칙_유무와_상관없이_dz_dx_계산결과는_같음():
    x, y = symbols('x y')

    # 첫 번째 함수의 도함수
    # 충돌을 피하기 위해 _y
    _y = x**2 + 1
    dy_dx = diff(_y)

    # 두 번째 도함수
    z = y**3 - 2
    dz_dy = diff(z)

    # 연쇄 벅칙을 사용한 경우와
    # 대체 방식을 사용한 경우
    dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
    dz_dx_no_chain = diff(z.subs(y, _y))

    # 두 값이 같다는 것을 보임으로써 연쇄 법칙 증명
    print(dz_dx_chain)
    print(dz_dx_no_chain)

def _적분_근사():

    def approximate_integral(a, b, n, f):
        delta_x = (b - a) / n
        total_sum = 0

        for i in range(1, n + 1):
            midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
            total_sum += f(midpoint)

        return total_sum * delta_x

    def my_function(x):
        return x**2 + 1

    area = approximate_integral(a=0, b=1, n=5, f=my_function)
    print(area)

    area = approximate_integral(a=0, b=1, n=500, f=my_function)
    print(area)

    area = approximate_integral(a=0, b=1, n=1000, f=my_function)
    print(area)

    area = approximate_integral(a=0, b=1, n=1000000, f=my_function)
    print(area)

def _적분():
    x = symbols('x')

    f = x**2 + 1

    # 적분 계산
    area = integrate(f, (x, 0, 1))

    print(area) # 유리수 4/3

def _극한사용_적분():
    x, i, n = symbols('x i n')

    f = x**2 + 1
    lower, upper = 0,1

    delta_x = ((upper - lower) / n)
    x_i = (lower + delta_x * i)
    fx_i = f.subs(x, x_i)

    # n개의 직사각형을 순환하며 면적을 합산
    n_rectangles = Sum(delta_x * fx_i, (i,1,n)).doit()

    # 직사각형의 개수 n을 무한대로 늘려 면적을 계산
    area = limit(n_rectangles, n, oo)

    print(area)

if __name__ == '__main__':
    _극한사용_적분()