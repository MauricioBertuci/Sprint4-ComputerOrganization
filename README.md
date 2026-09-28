# GoodWe Smart Charging Station

**Sprint 4 – Computer Organization | FIAP**

## 1. Sobre o projeto

O GoodWe Smart Charging Station é uma simulação de uma estação inteligente de recarga de veículos elétricos, desenvolvida utilizando Raspberry Pi Pico, MicroPython e o simulador Wokwi.

O projeto é inspirado no conceito de gerenciamento inteligente de energia da GoodWe, demonstrando como um controlador pode distribuir uma quantidade limitada de potência entre diferentes veículos elétricos.

O sistema gerencia três veículos conectados simultaneamente, considerando a potência disponível, a potência solicitada e o percentual de bateria de cada veículo.

## 2. Objetivos

- Simular uma estação de recarga inteligente.
- Gerenciar a distribuição de potência entre três veículos.
- Priorizar veículos em situações de baixa disponibilidade.
- Demonstrar diferentes condições energéticas.
- Representar os estados de recarga por LEDs.
- Apresentar informações pelo Monitor Serial.
- Aplicar conceitos de Arquitetura de Computadores.

## 3. Tecnologias utilizadas

| Tecnologia        | Finalidade                        |
|-------------------|-----------------------------------|
| Raspberry Pi Pico | Unidade central de processamento  |
| MicroPython       | Desenvolvimento do algoritmo      |
| Wokwi             | Simulação do circuito             |
| LEDs              | Indicação dos estados de recarga  |
| Pushbutton        | Alternância dos cenários          |
| Monitor Serial    | Visualização das informações      |

## 4. Funcionamento

A estação possui três veículos elétricos simulados:

| Veículo | Bateria | Potência solicitada |
|---------|---------|---------------------|
| EV1     | 25%     | 2.000 W             |
| EV2     | 45%     | 2.500 W             |
| EV3     | 70%     | 3.000 W             |

A demanda total é de 7.500 W.

O Raspberry Pi Pico recebe os dados, calcula a disponibilidade energética e determina a potência destinada a cada veículo.

O botão permite alternar entre três cenários.

### Cenário 1 — Alta disponibilidade

Potência disponível: 8.000 W.

Todos os veículos recebem a potência solicitada.

| Veículo | Potência recebida | LED |
|---|---:|---|
| EV1 | 2.000 W | Verde |
| EV2 | 2.500 W | Verde |
| EV3 | 3.000 W | Verde |

### Cenário 2 — Disponibilidade limitada

Potência disponível: 5.000 W.

O controlador aplica uma distribuição proporcional à demanda de cada veículo.

| Veículo | Potência recebida | LED |
|---|---:|---|
| EV1 | 1.334 W | Amarelo |
| EV2 | 1.666 W | Amarelo |
| EV3 | 2.000 W | Amarelo |

### Cenário 3 — Baixa disponibilidade

Potência disponível: 2.000 W.

O veículo com menor percentual de bateria recebe prioridade. Os demais permanecem aguardando.

| Veículo | Potência recebida | LED |
|---|---:|---|
| EV1 | 2.000 W | Verde |
| EV2 | 0 W | Vermelho |
| EV3 | 0 W | Vermelho |

## 5. Algoritmo de gerenciamento

O sistema utiliza uma estratégia híbrida de distribuição energética.

Quando a potência disponível é suficiente, todos os veículos recebem a potência solicitada.

Quando existe disponibilidade limitada, mas suficiente para atender pelo menos 50% da demanda total, a potência é distribuída proporcionalmente.

Quando a disponibilidade é inferior a 50% da demanda, os veículos são ordenados pelo percentual de bateria, priorizando aqueles com menor carga.

O algoritmo garante que a soma das potências distribuídas não ultrapasse a potência disponível.

## 6. Componentes e conexões

O circuito utiliza:

- 1 Raspberry Pi Pico;
- 9 LEDs;
- 9 resistores de 220 Ω;
- 1 botão Pushbutton.

### Mapeamento dos pinos

| Componente         | Pino |
|--------------------|------|
| EV1 – LED verde    | GP2  |
| EV1 – LED amarelo  | GP3  | 
| EV1 – LED vermelho | GP4  |
| EV2 – LED verde    | GP5  |
| EV2 – LED amarelo  | GP6  |
| EV2 – LED vermelho | GP7  | 
| EV3 – LED verde    | GP8  |
| EV3 – LED amarelo  | GP9  |
| EV3 – LED vermelho | GP10 |
| Botão              | GP15 |

O botão utiliza o resistor pull-up interno do microcontrolador.

## 7. Arquitetura de Computadores

O projeto demonstra a integração dos principais conceitos estudados na disciplina.

**Entrada:** botão e dados simulados dos veículos.

**Processamento:** execução do algoritmo no microcontrolador RP2040 do Raspberry Pi Pico.

**Memória:** armazenamento das variáveis, informações dos veículos e estados da simulação durante a execução.

**Representação de dados:** utilização de valores inteiros para potência e percentual de bateria.

**Saída:** acionamento dos LEDs e apresentação das informações pelo Monitor Serial.

**Comunicação:** utilização dos pinos GPIO e da comunicação serial.

### Representação numérica

Exemplo utilizando a potência disponível de 5.000 W:

| Sistema     | Representação |
|-------------|---------------|
| Decimal     | 5000          |
| Binário     | 1001110001000 |
| Hexadecimal | 0x1388        |      

## 8. Relação com a GoodWe

A solução é inspirada no conceito de gerenciamento inteligente de energia da GoodWe.

Assim como os sistemas inteligentes de gerenciamento energético, o projeto utiliza informações de disponibilidade e demanda para controlar a utilização dos recursos.

A implementação possui finalidade educacional e não reproduz integralmente os equipamentos ou algoritmos comerciais da empresa.

## 9. Como executar

1. Acesse o projeto no Wokwi.
2. Inicie a simulação.
3. Observe os LEDs e o Monitor Serial.
4. Pressione o botão para alterar a disponibilidade de potência.
5. Verifique a distribuição realizada pelo controlador.

A sequência de cenários é:

8.000 W → 5.000 W → 2.000 W → 8.000 W.

## 10. Links

**Simulação Wokwi:**  
https://wokwi.com/projects/476445026680481793

**Vídeo demonstrativo:**  
Inserir link do YouTube.

## 11. Integrantes

- Mauricio Bertuci Saletti - RM571229
- Lucas Caram Bueno - RM570158
- ⁠Rhuan Pacheco Carreri - RM570129
- Leonardo Fortini Marcelo - RM572566
- ⁠Nicolas Andrade Rodrigues - RM572782

---

Projeto acadêmico desenvolvido para a Sprint 4 da disciplina de Computer Organization – FIAP.