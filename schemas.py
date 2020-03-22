from typing import List

from pydantic import BaseModel


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
    #einwilligung_immunheroes

