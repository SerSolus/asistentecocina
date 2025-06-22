from flask import Flask, render_template, request
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
    try:
        response = requests.post(url, data=payload)
        return response.status_code == 200, response.text
    except Exception as e:
        return False, str(e)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/llamar-mesero")
def llamar_mesero():
    mesa = request.args.get("mesa", "¿?")
    mensaje = f"📢 Mesa {mesa} ha llamado al mesero. ¡Atención!"
    exito, respuesta = enviar_mensaje(mensaje)
    return "✅ Mensaje enviado." if exito else f"❌ Error: {respuesta}"

@app.route("/otra-cerveza")
def otra_cerveza():
    mesa = request.args.get("mesa", "¿?")
    mensaje = f"🍺 Mesa {mesa} ha pedido otra cerveza."
    exito, respuesta = enviar_mensaje(mensaje)
    return "✅ Pedido enviado." if exito else f"❌ Error: {respuesta}"

@app.route("/incidente")
def incidente():
    mesa = request.args.get("mesa", "¿?")
    mensaje = f"⚠️ Mesa {mesa} reporta un incidente."
    exito, respuesta = enviar_mensaje(mensaje)
    return "✅ Reporte enviado." if exito else f"❌ Error: {respuesta}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
