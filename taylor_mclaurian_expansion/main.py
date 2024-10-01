from sympy import symbols, factorial, diff, pprint, exp, log, sin

x = symbols('x')
y = symbols('y')


def taylorexpansion(func, a, n, var):
    t_y = symbols('t_y')
    expansion = func.subs(var, a)
    d = func
    if (expansion == 0):
        n += 1
    try:
        k = 1
        while (k < n):
            d = diff(d, var)
            term = (d*((t_y-a)**k))/factorial(k)
            term = term.subs(var, a)
            if (term == 0):
                continue
            term = term.subs(t_y, var)
            expansion = term+expansion
            k += 1
            if (d == 0 and k < n):
                print("only ", k-1, " terms present")
        if (n < 1):
            print("3rd argument is for no. of terms, provide a natural number")
            return ''
        expansion = expansion.subs(t_y, var)
        return expansion
    except TypeError:
        print("3rd argument denotes number of terms, provide a natural number")
        return ''


def taylorvalue(func, a, n, x):
    f = taylorexpansion(func, a, n, x)
    return f.evalf(subs={x: a})


def mclaurianexpansion(func, steps, variable):
    taylorexpansion(func, 0, steps, variable)


def mclaurianvalue(func, steps, variable):
    taylorvalue(func, 0, steps, variable)


def examples():
    # e^x expansion at x=0 with 5 terms differentiating with respect to x
    pprint(taylorexpansion(exp(x), 0, 5, x))

    # e^x approximation at x=1 with 10 terms differentiating with respect to x
    print(taylorvalue(exp(x), 1, 10, x))

    # log(1+x) expansion at x=0 with 5 terms differentiating with respect to x
    pprint(taylorexpansion(log(x+1), 0, 5, x))

    # sin(x) expansion at x=0 with 5 terms differentiating with respect to x
    pprint(taylorexpansion(sin(x), 0, 5, x))

    # expansion for expression at x=0 with 3 terms differentiating wrt to x
    pprint(taylorexpansion((5*x**2)+(3*x)+(7), 0, 3, x))

    # e^(xy) expansion at x=1 with 5 terms differentiating with respect to x
    pprint(taylorexpansion(exp(x*y), 1, 5, x))


examples()
