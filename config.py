from os import environ 

class Config:
    API_ID = environ.get("API_ID", "12380656")
    API_HASH = environ.get("API_HASH", "d927c13beaaf5110f25c505b7c071273")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6883904115:AAFzjOFjf30iab7YEh5dMQ5Y1D0V-6bBQ74") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ranjuvishwakarma50:aman@cluster0.jfl45jq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5977931010').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
