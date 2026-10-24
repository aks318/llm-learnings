from turtle import mode
from typing import Annotated, Optional

from pydantic import BaseModel, Field, computed_field, field_validator, model_validator


class Patient(BaseModel):
    name: Annotated[str, Field(max_length= 50, title="Its a name", description="Provide any name", examples=["Aakash", "Shiva"])]
    age: int = Field(gt=2, strict=True)
    weight: float
    height: float
    allergy: Optional[list[str]] = None
    contact: dict[str, str]
    email: str

    @field_validator('email')
    @classmethod
    def email_validation(cls, value: str):
        allowed = ["hdfc.com", "icici.com"]
        extentions = value.split("@")
        print(extentions)
        if extentions[1] not in allowed:
            raise ValueError("wrong domain")

        return value

    @model_validator(mode="after")
    def check_patient_age(cls , model):
        if model.age > 60 and "emergency" not in model.contact:
            raise ValueError("GT 60 age must have contact")
        return model

    @computed_field()
    @property
    def calculate_bmi(self) -> float:
        bmi =  self.weight/(self.height **2)
        return bmi


patient1 = {
            "name": "Aakash", 
            "age": 100, 
            "contact": {"email": "qwdqw@hdfc.com", "phone": "646", "emergency": "232"},
            "email": "akash@hdfc.com",
            "weight": 67,
            "height": 1.72
        }

patient1 = Patient(**patient1)

temp = patient1.model_dump()

print(temp)
print(type(temp))
