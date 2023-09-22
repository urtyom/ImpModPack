from application.salary import calculate_salary
from application.date_now import date_now
from application.db.people import get_employees


if __name__ == '__main__':
  date_now()
  calculate_salary()
  get_employees()
