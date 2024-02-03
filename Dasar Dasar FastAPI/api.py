from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from enum import Enum

aplication = FastAPI()

class Tipe(str, Enum):
    def  __str__(self):
        return str(self.value)
    INCOME ="Income"
    PURCHASE = "Purchase"
    INVEST = "Invest"

class Method(str, Enum):
    def  __str__(self):
        return str(self.value)
    CASH = "Cash"
    EWALLET = "E-Wallet"
    BANK = "Bank"

class Input(BaseModel):
    tipe:Tipe
    amount:int
    notes:Optional[str]
    method:Method

transaction = []

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

@aplication.post("/transaction")
def insert_transaction(input_transaction:Input):
    transaction.append(input_transaction)
    return transaction
