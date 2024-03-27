import calculator
def test_addition():
    a = 2
    b = 3
    assert calculator.add(2, 3) == 5

def test_subtraction():
    a = 2
    b = 3
    assert calculator.subtract(2, 3) == -1

def test_division():
    assert calculator.devide(6, 3) == 2
    assert calculator.devide(6, 0) == "Error"
