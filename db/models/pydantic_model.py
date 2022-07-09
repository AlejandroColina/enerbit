from pydantic import BaseModel

class Metric(BaseModel):
    device: str
    consumo: str
    date: str

    class Config:
        orm_mode = True