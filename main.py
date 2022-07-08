from fastapi import FastAPI


from routes.metrics import router
from db.datebase import Base, engine
from db.models.metric import Metric


app = FastAPI()
app.include_router(router, prefix='/metrics')

print('Creating database...')
Base.metadata.create_all(engine)
print('Database created!')