# predict.py
import joblib
import pandas as pd

# Carrega o modelo treinado de peso médio
# Certifique-se de que o arquivo modelo_peso_medio_dia_200.pkl
# está na mesma pasta deste arquivo.
model = joblib.load("weigh_fish_prediction.pkl")


def make_prediction(dia, racao_total, biomassa_inicial, cardume_lote):
    """
    Faz a previsão de Peso Médio usando o modelo treinado.

    Parâmetros (numéricos):
        dia: int ou float
        racao_total: float
        biomassa_inicial: float
        cardume_lote: int ou float

    Retorna:
        float -> previsão de Peso Médio (mesma unidade usada no treino, ex: gramas)
    """

    # Monta o DataFrame com os mesmos nomes de colunas usados no treino
    data = pd.DataFrame([{
        "Dia": dia,
        "Ração Total": racao_total,
        "Biomassa Inicial": biomassa_inicial,
        "Cardume Lote": cardume_lote
    }])

    # Predição
    y_pred = model.predict(data)

    # y_pred é um array, pegamos o primeiro valor
    return float(y_pred[0])
