from fastapi import FastAPI

aplication = FastAPI()

# membuat endpoint simple menggunakan get

@aplication.get("/transaction")
def get_transaction ():
    return "kembalikan"