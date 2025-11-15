# main.py
from flask import Flask, request, jsonify
from predict import make_prediction

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Simple health-check / documentation."""
    body = """
    <html>
      <body style='padding: 10px; font-family: Arial, sans-serif;'>
        <h1>API - Predição de Peso Médio (FishTrader)</h1>
        <p>Use o endpoint <code>/predict</code> via método POST com JSON no corpo.</p>
        <p>Exemplo de JSON:</p>
        <pre>
        {
          "dia": 186,
          "racao_total": 39500,
          "biomassa_inicial": 1096,
          "cardume_lote": 34257
        }
        </pre>
      </body>
    </html>
    """
    return body


@app.route("/predict", methods=["POST"])
def predict():
    """
    Recebe JSON com os campos:
        dia, racao_total, biomassa_inicial, cardume_lote
    e retorna a previsão de peso médio.
    """
    try:
        data_json = request.get_json()

        # Validação simples
        required_fields = ["dia", "racao_total", "biomassa_inicial", "cardume_lote"]
        missing = [f for f in required_fields if f not in data_json]
        if missing:
            return jsonify(
                {
                    "error": "Campos ausentes no JSON",
                    "missing_fields": missing,
                }
            ), 400

        dia = data_json["dia"]
        racao_total = data_json["racao_total"]
        biomassa_inicial = data_json["biomassa_inicial"]
        cardume_lote = data_json["cardume_lote"]

        prediction = make_prediction(
            dia=dia,
            racao_total=racao_total,
            biomassa_inicial=biomassa_inicial,
            cardume_lote=cardume_lote,
        )

        return jsonify(
            {
                "prediction": prediction,
                "units": "mesma unidade usada no treino (ex: g)",
                "inputs": data_json,
            }
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Para rodar localmente: python main.py
    #app.run(host="0.0.0.0", port=8080, debug=True)
    app.run()
