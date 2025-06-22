from flask import Flask, render_template
import os
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": texto
    }
    response = requests.post(url, data=payload)
    return response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/llamar-mesero")
def llamar_mesero():
    mensaje = "📢 La mesa ha llamado al mesero. ¡Atención!"
    response = enviar_mensaje(mensaje)
    if response.status_code == 200:
        return "✅ Mensaje enviado al mesero."
    else:
        return f"❌ Error al enviar mensaje: {response.text}"

@app.route("/otra-cerveza")
def otra_cerveza():
    mensaje = "🍺 La mesa ha pedido otra cerveza."
    response = enviar_mensaje(mensaje)
    if response.status_code == 200:
        return "✅ Mensaje enviado para otra cerveza."
    else:
        return f"❌ Error al enviar mensaje: {response.text}"

@app.route("/incidente")
def incidente():
    mensaje = "⚠️ La mesa reporta un incidente."
    response = enviar_mensaje(mensaje)
    if response.status_code == 200:
        return "✅ Mensaje de incidente enviado."
    else:
        return f"❌ Error al enviar mensaje: {response.text}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
