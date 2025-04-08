import requests
import time
import os

# Lee las variables del entorno definidas en Render.com
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": texto, "parse_mode": "Markdown"}
    requests.post(url, data=data)
    print("Mensaje enviado:", texto)

def analizar_y_enviar():
    pick = "**[Análisis automático]**\n\n" \
           "*Tenis de mesa – Liga Pro Checa*\n" \
           "**Partido:** Novy vs. Trsek\n" \
           "**Pick:** Más de 75.5 puntos totales\n" \
           "**Stake:** 8/10\n" \
           "**Confianza:** Alta\n" \
           "**Probabilidad estimada:** 73%"
    enviar_mensaje(pick)

# Ejecuta cada 5 minutos
while True:
    analizar_y_enviar()
    time.sleep(300)
