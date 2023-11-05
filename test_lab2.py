import Ex6.lab2 as lab2


def test_find_min_max():
    test_arr = [5, 67, 32]
    pass_arr = [5, 67]

    result = lab2.find_min_max(test_arr)
    assert (result == pass_arr)


def test_calc_average():
    test_arr = [5, 67, 32]
    result = lab2.calc_average(test_arr)
    assert (int(result) == 34)


def test_calc_median_temperature():
    test_arr = [5, 67, 32]
    result = (lab2.calc_median_temperature(test_arr))
    assert (result == 32)

