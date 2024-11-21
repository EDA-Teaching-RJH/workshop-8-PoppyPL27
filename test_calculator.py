#main entry point
def main():
    test_add()
    test_subtract()
    test_multiply()
    test_divide()


#test adding function:
from calculator import add
def test_add():
    #positive tests
    try:
        assert add(2,4) == 6
    except AssertionError:
        print("2 add 4 is not 6")
    

    # tests with negatives
    try:
        assert add(-2,4) == 2
    except AssertionError:
        print("-2 add 4 is not 2")
    try:
        assert add(2,-4) == -2
    except AssertionError:
        print("2 add -4 is not -2")
    try:
        assert add(-2,-4) == -6
    except AssertionError:
        print("-2 add -4 is not -6")
    

    #tests of boundary cases
    try:
        assert add(0,4) == 4
    except AssertionError:
        print("0 add 4 is not 4")
    try:
        assert add(2,0) == 2
    except AssertionError:
        print("2 add 0 is not 2")

#test subrtacting function:
from calculator import subtract
def test_subtract():
    #positive tests
    try:
        assert subtract(2,4) == -2
    except AssertionError:
        print("2 subtract 4 is not -2")
    

    # tests with negatives
    try:
        assert subtract(-2,4) == -6
    except AssertionError:
        print("-2 subtract 4 is not -6")
    try:
        assert subtract(2,-4) == 6
    except AssertionError:
        print("2 subtract -4 is not 6")
    try:
        assert subtract(-2,-4) == 2
    except AssertionError:
        print("-2 subtract -4 is not 2")
    

    #tests of boundary cases
    try:
        assert subtract(0,4) == -4
    except AssertionError:
        print("0 subtract 4 is not -4")
    try:
        assert subtract(2,0) == 2
    except AssertionError:
        print("2 subtract 0 is not 2")

#test multiplication function:
from calculator import multiply
def test_multiply():
   #positive tests
    try:
        assert multiply(2,4) == 8
    except AssertionError:
        print("2 multiply 4 is not 8")
    

    # tests with negatives
    try:
        assert multiply(-2,4) == -8
    except AssertionError:
        print("-2 multiply 4 is not -8")
    try:
        assert multiply(2,-4) == -8
    except AssertionError:
        print("2 multiply -4 is not -8")
    try:
        assert multiply(-2,-4) == 8
    except AssertionError:
        print("-2 multiply -4 is not 8")
    

    #tests of boundary cases
    try:
        assert multiply(0,4) == 0
    except AssertionError:
        print("0 multiply 4 is not 0")
    try:
        assert multiply(2,0) == 0
    except AssertionError:
        print("2 multiply 0 is not 0")

#test division function:
from calculator import divide
def test_divide():
        #positive tests
    try:
        assert divide(2,4) == 0.5
    except AssertionError:
        print("2 divide 4 is not 0.5")
    

    # tests with negatives
    try:
        assert divide(-2,4) == -0.5
    except AssertionError:
        print("-2 divide 4 is not -0.5")
    try:
        assert divide(2,-4) == -0.5
    except AssertionError:
        print("2 divide -4 is not -0.5")
    try:
        assert divide(-2,-4) == 0.5
    except AssertionError:
        print("-2 divide -4 is not 0.5")
    

    #tests of boundary cases
    try:
        assert divide(0,4) == 0
    except AssertionError:
        print("0 divide 4 is not 4")
    try:
        assert divide(2,0) == "dividing by zero error"
    except AssertionError:
        print("2 divided by 0 is not error")


if __name__ == "__main__":
    main()