from pydantic import BaseModel, Field


class Persom (BaseModel):
    name: str | None = None
    age: int = Field(gt=22)


new_P = {"age": "23"}

P1 = Persom(**new_P)

print(dict(P1))