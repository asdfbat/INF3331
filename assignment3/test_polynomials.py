from polynomials import Polynomial

def test_poly_evaluation():
    poly = Polynomial([5, 2, 3])
    assert poly(3) == (3*3**2 + 2*3 + 5)

def test_poly_addition():
    poly1 = Polynomial([2, 0, 2 , 4])
    poly2 = Polynomial([1, 3, 9])
    assert (poly1 + poly2) == [3, 3, 11, 4]

def test_poly_subtraction():
    poly1 = Polynomial([2, 0, 3])
    poly2 = Polynomial([2, 4, 1, 4])
    assert (poly1 - poly2) == [0, -4, 2, -4]
    assert (poly2 - poly1) == [0, 4, -2, 4]

def test_poly_degree():
    poly1 = Polynomial([1])
    poly2 = Polynomial([0, 4, 2, 0])
    poly3 = Polynomial([0, 0, 0])
    assert poly1.degree() == 0
    assert poly2.degree() == 2
    assert poly3.degree() == -1

def test_poly_multiply():
    poly = Polynomial([3, 0, 4, 1])
    assert poly*3 == [9, 0, 12, 3]

def test_poly_string():
    poly = Polynomial([4, -3, 0, -1, 2])
    assert str(poly) == "2x^4 - x^3 - 3x + 4"

test_poly_evaluation()
test_poly_addition()
test_poly_subtraction()
test_poly_degree()
test_poly_multiply()
test_poly_string()
