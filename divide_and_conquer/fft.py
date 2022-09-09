"""
Multiplying two polynomials in nlog(n) Complexity
Referenced from the video
https://www.youtube.com/watch?v=h7apO7q16V0
"""
import cmath


def multiply(p1, p2):
    """
    @param p1: list of coefficients of polynomial 1
    @param p2: list of coefficients of polynomial 2
    @return: list of coefficients of polynomial 1 * polynomial 2
    """
    points_1, points_2 = fft(p1), fft(p2)  # O(nlog(n))
    result_points = [item_1 * item_2 for item_1, item_2 in zip(points_1, points_2)]  # O(n)
    print(points_1, points_2, result_points)
    return ifft(result_points)


def fft(p):
    """
    O(nlog(n))
    @param p: p is an array of coefficients of the Polynomial P, length has to be a power of 2
    @return: as set of n values if p is in degree d + 1, where n = d + 1
    """
    n = len(p)  # n has to be a power of 2
    # base case
    if n == 1:
        return p
    omega = cmath.exp(2 * cmath.pi * complex(0, 1) / n)
    y_e, y_o = fft(p[::2]), fft(p[1::2])
    y = [0] * n
    # merge
    for j in range(int(n / 2)):
        y[j] = y_e[j] + omega ** j * y_o[j]
        y[j + int(n / 2)] = y_e[j] - omega ** j * y_o[j]
    return y


def ifft(p):
    """
    Inverse of fft
    O(nlog(n))
    @param p: p is an array of y value of e.g [P(w^0), P(w^1) ..., P(w^(n-1))], which can present a polynomial
    @return: list coefficients of the polynomial
    """
    n = len(p)  # n has to be a power of 2
    # base case
    if n == 1:
        return p
    omega = cmath.exp(-2 * cmath.pi * complex(0, 1) / n)
    y_e, y_o = ifft(p[::2]), ifft(p[1::2])
    y = [0] * n
    # merge
    for j in range(int(n / 2)):
        y[j] = (y_e[j] + omega ** j * y_o[j]) / 2
        y[j + int(n / 2)] = (y_e[j] - omega ** j * y_o[j]) / 2
    return y


if __name__ == '__main__':
    p1 = [1, 2, 0, 0]
    p2 = [2, 1, 0, 0]
    print(multiply(p1, p2))
