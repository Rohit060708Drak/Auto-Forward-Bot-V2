from os import environ 

class Config:
    API_ID = environ.get("API_ID", "25910703")
    API_HASH = environ.get("API_HASH", "c3973154663a7b3c7d507dc1180b446f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8307441731:AAFZe1vdSOBlJqjsc1VHPttsxreqnLwzs6w") 
    BOT_SESSION = environ.get("BOT_SESSION", "BQGLXa8AZfkAYUrtARA905_5Vss8xR-2yEqmcRAj1LnEPQaiBkm0qvKqo0wfiuQqslXOu8QVU84kogB1JNGLAVq-8OpPH7UrNjgRhQpyFQ_Z6rXWOKqT96HdFgWoh4qZlhzDGlsLoVbsROGblBNHSKYqKw3O6KvCHUsYX1CoIXKz5463Yh7RmXVmMdaI6sQOynzLP8CdNwZgDZcn92CHof8Fvc7ULbQ-tpao5fK-LperStDNG2MVxD3cR07gPKzafR8HyWXfIaPUAHI3iFIo691zBLFgpJvNXAXYsnHmqF0UqI_05y3AMKrn9UeY9T4s531HdXZ7YL_PGfPcQM2ZaJcwf-AUJAAAAAHvKYBDAQ") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://darkeaglemovies_db_user:CDQBNG3HKbePFYQX@cluster0.dmnx8be.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6000662798').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
