import employee_info 

def test_get_employees_by_age_range():
    ans = [{'age': 23, 'department': 'Marketing', 'name': 'Mary', 'salary': 56000}]
    assert(employee_info.get_employees_by_age_range(0,24)==ans)

def test_calc_average_salary():
    ans = 60166.67
    assert(employee_info.calculate_average_salary()== ans)

def test_get_employees_by_dept():
    ans = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    assert(employee_info.get_employees_by_dept("Sales") == ans)