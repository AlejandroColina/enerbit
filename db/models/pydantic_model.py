from pydantic import BaseModel, Field

class Metric(BaseModel):
    device: str = Field(example="777")
    consumo: str = Field(example="104 kW")
    date: str = Field(example="2022-07-09 16:16:17.671227")

    class Config:
        orm_mode = True