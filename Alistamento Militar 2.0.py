import re
import datetime

print('-=-' * 20)
print('Alistamento Militar')
print('-=-' * 20)

# Convertendo data de nascimento completa em ano e em int
dt_nascimento0 = str(input('Qual a sua data de nascimento: '))
dt_nascimento1 = re.sub("\/|\.|\-|\\|\,|\;|\~|\_|\+|\*|\ |","",dt_nascimento0)

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
data_atual0 = date.strftime("%d/%m/%Y")
data_atual1 = re.sub("\/|","",data_atual0)
ano_atual = int(data_atual1[4:])

ano = int(dt_nascimento1[4:])
id_alis = ano_atual - ano

# Alistamento Militar
if id_alis < 17 and id_alis >= 0:
    print(f'Faltam {(17 - id_alis)} anos para você se alistar.')
elif id_alis > 17:
    print(f'Procure uma JSM o quanto antes, você passou {id_alis - 17} anos de se alistar.')
elif id_alis == 17:
    print(f'Você deverá alistar-se esse ano.')