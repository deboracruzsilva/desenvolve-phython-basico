from datetime import datetime
data_atual = datetime.now()
data_em_texto = data_atual.strftime('%d/%m/%Y')
hora_em_texto = data_atual.strftime('%H:%M')
print("Data: ",data_em_texto)
print("Hora: ",hora_em_texto)