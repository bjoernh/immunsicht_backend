from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from enum import Enum
from .database import Base


class BiologicalGender(Enum):
    woman = 1
    man = 2
    unknown = 3


class InsuranceCompany(Base):
    __tablename__ = "insurance_company"
    id = Column(Integer, primary_key=True, index=True)
    official_id = Column(Integer, unique=True)
    name = Column(String)


class Citizen(Base):
    __tablename__ = "citizen"
    id = Column(Integer, primary_key=True, index=True)
    citizen_id = Column(Integer, unique=True, index=True)
    insurance_company = Column(Integer, ForeignKey("insurance_company.id"))
    first_name = Column(String)
    last_name = Column(String)
    street = Column(String)
    postcode = Column(String)
    city = Column(String)
    birthday = Column(Date, index=True)
    biological_gender = Column(Enum(BiologicalGender))
    test_cases = relationship("TestCase", back_populates="patient")


class TestMethod(Base):
    __tablename__ = "test_method"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    reliability_score = Column(Integer)
    test_cases = relationship("TestCase", back_populates="test_method")


class TestCase(Base):
    __tablename__ = "test_case"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("citizen.id"))
    patient = relationship("Citizen", back_populates="test_cases")
    date_of_test Column(Date, index=True)
    result_positve = Colum(Boolean, index=True)
    test_method_id = Column(Integer, ForeignKey("test_method.id"))
    test_method = relationship("TestMethod", back_populates="test_cases")

