from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "26043952"))
    API_HASH = getenv("API_HASH", "96b8dea447ef580b5b75b01ccc3ab710")
    BOT_TOKEN = getenv("BOT_TOKEN", "7633669044:AAHiS9PWSZkyZeHdTA6m8-6PYNf9DKitfvQ")
    FSUB = getenv("FSUB", "AMBOTYT")
    CHID = int(getenv("CHID", "-1000112234"))
    
sudo_env = os.getenv("SUDO", "").strip()
SUDO = list(map(int, sudo_env.split())) if sudo_env else []

    MONGO_URI = getenv("MONGO_URI", "mongodb://mongo:XTKWKCzhppgfmcSoenGawpAdLxDdKAOE@mongodb.railway.internal:27017")
    
cfg = Config()
