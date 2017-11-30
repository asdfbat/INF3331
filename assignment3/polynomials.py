class Polynomial:

    def __init__(self, coefficients):
        self.coef_list = coefficients


    def degree(self):
        deg = -1
        coef_list_inv = [self.coef_list[i] for i in range(len(self.coef_list)-1, -1, -1)]
        for i in range(len(coef_list_inv)):
            if coef_list_inv[i] != 0:
                deg = i

        return deg


    def coefficients(self):
        return self.coef_list


    def __call__(self, x):
        poly_eval_sum = 0
        for order in range(len(self.coef_list)):
            poly_eval_sum += self.coef_list[order]*x**order
        return poly_eval_sum


    def __add__(self, p):
        if isinstance(p, Polynomial):
            p_coef_list = p.coefficients()
            if len(self.coef_list) >= len(p_coef_list):
                poly_add_sum = self.coef_list[:]
                for order in range(len(p_coef_list)):
                    poly_add_sum[order] += p_coef_list[order]
            else:
                poly_add_sum = p_coef_list[:]
                for order in range(len(self.coef_list)):
                    poly_add_sum[order] += self.coef_list[order]
        else:
            raise ArithmeticError

        return poly_add_sum


    def __sub__(self, p):
        if isinstance(p, Polynomial):
            p_coef_list = p.coefficients()
            if self.coef_list >= p.coef_list:
                poly_sub_sum = self.coef_list[:]
                for order in range(len(p.coef_list)):
                    poly_sub_sum[order] -= p.coef_list[order]
            else:
                poly_sub_sum = [-p.coef_list[i] for i in range(len(p_coef_list))]
                for order in range(len(self.coef_list)):
                    poly_sub_sum[order] += self.coef_list[order]
        else:
            raise ArithmeticError

        return poly_sub_sum


    def __mul__(self, c):
        if not type(c) is int:
            raise ArithmeticError("Input argument c must be of type integer")
        poly_mul_sum = [self.coef_list[i]*c for i in range(len(self.coef_list))]

        return poly_mul_sum


    def __repr__(self):
        poly_string = ""
        for order in range(len(self.coef_list)-1, -1, -1):
            if self.coef_list[order] != 0:   # Skip all 0 coefficients.
                if self.coef_list[order] >= 0 and order < len(self.coef_list)-1:
                    # If number > 0, we add a plus. Minus is already there from the number. Also, don't want leading + on first coefficient.
                    poly_string += " +"
                if order >= 2:
                    if self.coef_list[order] == 1:
                        poly_string += " x^%d" % (order)
                    elif self.coef_list[order] == -1:
                        poly_string += " -x^%d" % (order)
                    else:
                        poly_string += " %dx^%d" % (self.coef_list[order], order)
                elif order == 1:
                    if self.coef_list[order] == 1:
                        poly_string += " x"
                    elif self.coef_list[order] == -1:
                        poly_string += " -x"
                    else:
                        poly_string += " %dx" % (self.coef_list[order])
                elif order == 0:
                    poly_string += " %d" % (self.coef_list[order])

        poly_string = poly_string.replace("-", "- ")
        poly_string = poly_string.strip()

        return poly_string


    def __eq__(self, p):
        return (p == self.coefficients())




if __name__ == "__main__":
    p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3


    print("The value of {} at {} is {}".format(p, 7, p(7)))

    print("The coefficients of {} are {}".format(p, p.coefficients()))


    print("\nAdding {} and {} yields {}".format(p, q, p+q))

    p, q, r = map(Polynomial,
                  [
                      [1, 0, 1], [0, 2, 0], [1, 2, 1]
                  ]
    )

    print("\nWill adding {} and {} be the same as {}? Answer: {}".format(
        p, q, r, p+q == r
    ))
    print("\nIs {} - {} the same as {}? Answer: {}".format(
        p, q, r, p-q == r
    ))
