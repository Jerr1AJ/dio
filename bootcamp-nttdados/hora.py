from datetime import datetime

# Obtendo a data e hora atuais no formato brasileiro
data_hora_brasil = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# Exibindo a string armazenada
print(data_hora_brasil)
