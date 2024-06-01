from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_pt_br_DATA = "%d/%m/%Y" # data atual formatada em formato brasileiro
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_pt_br_DATA))

mascara_data_dia_semana = "%d/%m/%Y %a" #sugestão: estudar a documentação de datetime
print(data_hora_atual.strftime(mascara_data_dia_semana))

print(datetime.strptime(data_hora_str, mascara_en))
