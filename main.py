from sympy import sympify, lambdify
from sympy.core.sympify import SympifyError


def get_function_expr():
    """
    Prompt the user for an expression in x, parse it, and return a callable f(x).
    Keeps asking until a valid expression is provided.
    """
    while True:
        equation_str = input("Enter an expression (e.g., x**3 - x**2 + 2): ")
        try:
            expr = sympify(equation_str)
            func = lambdify("x", expr, "math")
            return func
        except (SympifyError, TypeError) as exc:
            print(f"Invalid expression ({exc}); please try again.\n")


def bisection(f, a: float, b: float, epsilon: float = 0.0001):
    """
    Solve f(x)=0 on [a,b] using the bisection method and return an approximate root.
    """
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        return None

    while abs(b - a) >= epsilon:
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < epsilon:
            return c

        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    return (a + b) / 2


def prompt_intervals():
    """
    Prompt the user for intervals until they press Enter without input.
    Accepts input in the form "a b" or "a,b".
    Returns a list of (a, b) tuples.
    """
    intervals: list[tuple[float, float]] = []
    while True:
        raw = input("Enter interval as 'a b' (or 'a,b'), press Enter to finish: ").strip()
        if raw == "":
            break
        cleaned = raw.replace(",", " ")
        parts = cleaned.split()
        if len(parts) != 2:
            print("Please enter exactly two numbers.\n")
            continue
        try:
            a_val, b_val = float(parts[0]), float(parts[1])
            intervals.append((a_val, b_val))
        except ValueError:
            print("Invalid numbers, please try again.\n")
    return intervals


def main():
    f = get_function_expr()
    intervals = prompt_intervals()

    if not intervals:
        print("No intervals provided. Exiting.")
        return

    for idx, (a, b) in enumerate(intervals, start=1):
        root = bisection(f, a, b, 0.00000001)
        if root is None:
            print(f"[Interval {idx} | {a}, {b}] No root found (f(a) and f(b) do not have opposite signs).")
        else:
            print(f"[Interval {idx} | {a}, {b}] Root ≈ {root:.6f}")


if __name__ == "__main__":
    main()