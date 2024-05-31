from datetime import date, datetime, time

data = date(2023, 7, 10) # data
print(data)

print(date.today()) # data de hoje

data_hora = datetime(2023, 7, 10, 10, 30, 20) # hora minuto e segundo
print(data_hora)

data_hora2 = datetime(2023, 7, 10) # hora minutos e segundos zerados por padrão
print(data_hora2)

print(datetime.today()) # data atual, hora minuto e segundos atual

hora = time(10, 20, 0)
print(hora)