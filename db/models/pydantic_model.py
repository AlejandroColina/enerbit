from pydantic import BaseModel

class Metric(BaseModel):
    device: int
    consumo: str
    date: float

    class Config:
        orm_mode = True