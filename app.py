from flask import Flask
import os
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

@app.route("/")
def home():
    return "✅ ¡Asistente de cocina funcionando en Render!"

@app.route("/llamar-mesero")
def llamar_mesero():
    mensaje = "📢 La mesa ha llamado al mesero. ¡Atención!"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensaje
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return "✅ Mensaje enviado al mesero."
        else:
            return f"❌ Error al enviar mensaje: {response.text}"
    except Exception as e:
        return f"❌ Excepción al enviar mensaje: {e}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
