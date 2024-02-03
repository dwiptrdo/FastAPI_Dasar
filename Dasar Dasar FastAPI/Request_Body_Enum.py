from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from enum import Enum

aplication = FastAPI()

transaction = []

class Tipe(str, Enum):
    def __str__(self):
        return str(self.value)
    INCOME = "INCOME"
    PURCHASE = "PURCHASE"
    INVEST = "INVEST"

class Method(str, Enum):
    def __str__(self):
        return str(self.value)
    CASH = "CASH"
    EWALLET = "E-WALLET"
    BANK = "BANK"

class Input(BaseModel):
    tipe:Tipe
    amount:int
    notes:Optional[str]
    method:Method


@aplication.post("/transaction")
def insert_transaction(input_transaction:Input):
    transaction.append(input_transaction)
    return transaction