from datetime import date


def date_now():
  date_now = date.today()
  date_now_string = date_now.strftime('%d.%m.%y')
  print(f'Текущая дата: {date_now_string}')
