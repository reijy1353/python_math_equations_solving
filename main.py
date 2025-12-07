from sympy import sympify

def func(x: int, function: str | None = None):
    if function is None:
        equation_str = input("Enter an expression (e.g., x**3 - x**2 + 2): ")
        expr = sympify(equation_str)
    else:
        expr = sympify(function)
    return expr.subs('x', x)

print(func(5, "x**2 + 2*x + 1"))