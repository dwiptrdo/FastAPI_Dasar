from fastapi import FastAPI

aplication = FastAPI()

# membuat endpoint simple menggunakan get

# QUERY PARAMETER
@aplication.get('/transaction')
def get_transaction(tipe:str, amount:int):
    print(tipe, amount)
    print(type(tipe), type(amount))
    return f"balikan tipe dengan {tipe} dan {amount}"


# PATH PARAMETER
@aplication.get('/transaction/{tipe}')
def get_transaction(tipe:str):
    return f"balikan tipe dengan {tipe}"