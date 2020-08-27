import time
from iqoptionapi.stable_api import IQ_Option
from decouple import config


API = IQ_Option(config("USER"), config("PASS"))
API.connect()
API.change_balance("PRACTICE")  # PRACTICE / REAL


while True:
    if API.check_connect() == False:
        print("Erro ao se conectar")
        API.connect()
    else:
        print("Conectado com sucesso")
        break
    time.sleep(1)
