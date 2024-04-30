import Lab2.bmi as bmi

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.80,66) == 0

def test_bmi_under_weight():
    assert bmi.calculate_bmi(1.8,10) == -1 

def test_bmi_over_weight():
    assert bmi.calculate_bmi(1.8,1000) == 1