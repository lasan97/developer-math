from sympy import *

def _07():
    x = symbols('x')
    f = E**(2*x-1)

    dx_f = diff(f)
    print(dx_f)

def _08():
    x = symbols('x')
    f = log(x**2 - 1)
    dx_f = diff(f)
    print(dx_f)

def _09():
    p = 1000    # 원금
    r = 0.05    # 이자율
    t = 3       # 연도
    n = 12      # 연간 복리 적용 횟수

    a = p * (1 + (r/n)) ** (n * t) # 원금 * 1달이자 ** 3년복리적용횟수
    print(a)

def _10():
    p = 1000  # 원금
    r = 0.05  # 이자율
    t = 3  # 연도

    a = p * exp(r * t)
    print(a)

def _11():
    x = symbols('x')
    f = 3*x**2+1
    dx_f = diff(f)
    print(dx_f)
    print(dx_f.subs(x, 3))

def _12():
    x, y = symbols('x y')
    _y = x**3-1
    z = log(y) + 2

    dz_dy = diff(z)
    dy_dx = diff(_y)

    print(dz_dy)
    print(dy_dx)

    print(dz_dy * dy_dx)

def _13():
    x = symbols('x')

    f = 3*x**2+1
    area = integrate(f, (x, 0, 2))
    print(area)

if __name__ == '__main__':
    _13()