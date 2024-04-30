import Lab2.Lab2 as Lab2 


def test_find_min_max():
    list=[1,2,4,3,5]
    assert(Lab2.calc_min_max_temperature(list)==[1,5])

def test_calc_average():
    list=[1,2,3,4,5]
    assert(Lab2.calc_average_temperature(list)==3)

def test_find_median():
    list=[1,2,3,4,5]
    assert(Lab2.calc_median_temperature(list)==3)