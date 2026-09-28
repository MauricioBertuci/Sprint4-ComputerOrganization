from machine import Pin
from time import sleep_ms

veiculos = [
    {
        "id": "EV1",
        "bateria": 25,
        "solicitada": 2000,
        "pinos": (2, 3, 4)
    },
    {
        "id": "EV2",
        "bateria": 45,
        "solicitada": 2500,
        "pinos": (5, 6, 7)
    },
    {
        "id": "EV3",
        "bateria": 70,
        "solicitada": 3000,
        "pinos": (8, 9, 10)
    }
]

cenarios = [8000, 5000, 2000]
cenario_atual = 0

botao = Pin(15, Pin.IN, Pin.PULL_UP)

leds = []

for veiculo in veiculos:
    conjunto = []

    for numero_pino in veiculo["pinos"]:
        conjunto.append(Pin(numero_pino, Pin.OUT))

    leds.append(conjunto)



# ALGORITMO DE GERENCIAMENTO
def distribuir_energia(disponivel):

    distribuicao = [0] * len(veiculos)

    ativos = [
        i for i, v in enumerate(veiculos)
        if v["bateria"] < 100 and v["solicitada"] > 0
    ]

    demanda = sum(
        veiculos[i]["solicitada"]
        for i in ativos
    )

    if disponivel <= 0 or demanda == 0:
        return distribuicao

    if disponivel >= demanda:

        for i in ativos:
            distribuicao[i] = veiculos[i]["solicitada"]

        return distribuicao

    if disponivel * 2 >= demanda:

        restante = disponivel

        for i in ativos:

            solicitada = veiculos[i]["solicitada"]

            potencia = (
                disponivel * solicitada // demanda
            )

            potencia = min(potencia, restante)

            distribuicao[i] = potencia
            restante -= potencia

        for i in ativos:

            folga = (
                veiculos[i]["solicitada"]
                - distribuicao[i]
            )

            extra = min(folga, restante)

            distribuicao[i] += extra
            restante -= extra

        return distribuicao

    prioridade = sorted(
        ativos,
        key=lambda i: veiculos[i]["bateria"]
    )

    restante = disponivel

    for i in prioridade:

        solicitada = veiculos[i]["solicitada"]

        potencia = min(solicitada, restante)

        distribuicao[i] = potencia
        restante -= potencia

        if restante == 0:
            break

    return distribuicao



# CONTROLE DOS INDICADORES
def atualizar_leds(distribuicao):

    for i, veiculo in enumerate(veiculos):

        potencia = distribuicao[i]
        solicitada = veiculo["solicitada"]

        if potencia == 0:
            cor = 2
            status = "AGUARDANDO"

        elif potencia >= solicitada:
            cor = 0
            status = "RECARGA ATIVA"

        else:
            cor = 1
            status = "RECARGA REDUZIDA"

        if veiculo["bateria"] >= 100:
            status = "RECARGA CONCLUIDA"

        for j in range(3):
            leds[i][j].value(1 if j == cor else 0)

        print(
            "{} | Bateria: {}% | Solicitada: {} W"
            .format(
                veiculo["id"],
                veiculo["bateria"],
                solicitada
            )
        )

        print(
            "Recebida: {} W | Status: {}"
            .format(potencia, status)
        )

        print("--------------------------------")


# MONITORAMENTO SERIAL
def executar_cenario():

    disponivel = cenarios[cenario_atual]

    demanda = sum(
        v["solicitada"]
        for v in veiculos
        if v["bateria"] < 100
    )

    distribuicao = distribuir_energia(disponivel)

    utilizada = sum(distribuicao)

    print("\n")
    print("================================")
    print(" GOODWE SMART CHARGING STATION ")
    print("================================")

    print("Cenario:", cenario_atual + 1)

    print("Energia disponivel:", disponivel, "W")
    print("Demanda total:", demanda, "W")
    print("Potencia utilizada:", utilizada, "W")
    print("Potencia restante:", disponivel - utilizada, "W")

    print("\nREPRESENTACAO NUMERICA")

    print("Decimal:", disponivel)
    print("Binario:", bin(disponivel))
    print("Hexadecimal:", hex(disponivel))

    print("\nSTATUS DOS VEICULOS")
    print("--------------------------------")

    atualizar_leds(distribuicao)

    assert utilizada <= disponivel

    print("Limite energetico respeitado: SIM")
    print("================================")


# LOOP PRINCIPAL
print("Sistema inicializado.")

executar_cenario()

estado_anterior = 1

while True:
    estado_atual = botao.value()
    if estado_anterior == 1 and estado_atual == 0:

        cenario_atual = (
            cenario_atual + 1
        ) % len(cenarios)
        executar_cenario()
        sleep_ms(180)

    estado_anterior = botao.value()

    sleep_ms(20)
