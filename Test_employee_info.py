import employee_info

def test_get_employees_by_age_range():
    assert(employee_info.get_employees_by_age_range(0,24)==[{'age': 23, 'department': 'Marketing', 'name': 'Mary', 'salary': 56000}])

def test_calc_average_salary():
    assert(employee_info.calculate_average_salary()==60166.67)

def test_get_employees_by_dept():
    assert(employee_info.get_employees_by_dept("Sales")=={"name": "Peter", "age": 40, "department": "Sales", "salary": 60000},
{"name": "John", "age": 30, "department": "Sales", "salary": 50000})