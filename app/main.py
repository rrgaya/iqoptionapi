from auth import API


par = "EURUSD"
entrada = 2
direcao = "call"
timeframe = 1

_, id = API.buy_digital_spot(par, entrada, direcao, timeframe)

if isinstance(id, int):
    while True:
        status, lucro = API.check_win_digital_v2(id)

        if status:
            if lucro > 0:
                print("RESULTADO: WIN / VALOR: " + str(round(lucro, 2)))
            else:
                print("RESULTADO: LOSS / VALOR: -" + str(entrada))
            break


# Entradas na binaria
status, id = API.buy(entrada, par, direcao, timeframe)

if status:
    resultado, lucro = API.check_win_v3(id)

    print("RESULTADO: " + resultado + " / LUCRO: " + str(round(lucro, 2)))
