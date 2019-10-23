def test_biggest_guy():
    try:
        assert biggest_guy(1, 3, 2) == 3
        assert biggest_guy(30, 10, 20) == 30
        assert biggest_guy(20, 10, 30) == 30
        assert biggest_guy(2, 1, 9) == 9
        assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'
    except (AssertionError) as e:
        print(e)
        print("Wrong!!")
    print("Correct buddy!!!")


def biggest_guy(number1 , number2 , number3):
        if number1 > number2 and  number1 > number3:
            return number1
        elif number2 > number3 and number2 > number1:
            return number2
        else:
            return number3


test_biggest_guy()

