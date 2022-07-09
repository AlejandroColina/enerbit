from pydantic import BaseModel

class Metric(BaseModel):
    id:int
    device: str
    consumo: str
    date: str

    class Config:
        orm_mode = True