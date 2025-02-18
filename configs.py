import os

class Config:
    API_ID = int(os.getenv("API_ID", "26043952"))
    API_HASH = os.getenv("API_HASH", "96b8dea447ef580b5b75b01ccc3ab710")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7633669044:AAHiS9PWSZkyZeHdTA6m8-6PYNf9DKitfvQ")
    FSUB = os.getenv("FSUB", "AMBOTYT")
    CHID = int(os.getenv("CHID", "-1000112234"))

    # Convertir la variable de entorno SUDO en una lista de enteros
    SUDO = list(map(int, os.getenv("SUDO", "").split())) if os.getenv("SUDO") else []

    # URI de MongoDB
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:XTKWKCzhppgfmcSoenGawpAdLxDdKAOE@mongodb.railway.internal:27017")

cfg = Config()
