from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from pprint import pprint

fake_db = [{
    "case_code": "345dfgdf4r5",
    "citizen_id": 34554,
    "insurance_company": "Techniker Krankenkasse",
    "first_name": "Hans",
    "last_name": "Mueller",
    "street": "Corona Str. 34",
    "postcode": 99999,
    "city": "City",
    "birthday": "1988-03-20",
    "date_of_test": "2020-03-21",
    "result_positve": True,
    "test_method": "Antikoerper"
  }]



class InsuranceCompany(str, Enum):
    tk = "Techniker Krankenkasse"
    barmer = "Barmer"
    aok = "Aok"

class VirusTestMethod(str, Enum):
    anti = "Antikoerper"
    pcr = "PCR"


class Test(BaseModel):
    case_code : str
    citizen_id : int
    insurance_company : InsuranceCompany
    first_name : str
    last_name : str
    street : str
    postcode : str
    city : str
    birthday : date
    date_of_test : date
    result_positve : bool
    test_method : VirusTestMethod
    #TODO: ADD einwilligung_immunheroes

app = FastAPI()

@app.post("/test_results/")
async def add_test_result(test: Test):
    """Einen neues Testergebnis der Datenbank hinzuzufügen"""
    #test_dict = test.dict()
    #test_dict.update()
    fake_db.append(test)
    #pprint(fake_db)

@app.get("/test_results/")
async def get_results(skip: int = 0, limit: int = 10):
    """Testergebnise abfragen"""
    return fake_db[skip : skip + limit]

