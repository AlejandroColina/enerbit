from db.models.metric import Metric
from db.datebase import SessionLocal


db = SessionLocal()


def get_all():
    return db.query(Metric).all()


def get_a_metric(id_metric):
    response = db.query(Metric).filter(Metric.id == id_metric).first()

    if not response:
        return {'msg': 'Dont exist the id in DB'}
    else:
        return response


def create_metric(metric):
    m = Metric(device=metric.device, consumo=metric.consumo, date=metric.date)
    db.add(m)
    db.commit()
    return m


def update_metric(id_metric, parameters):
    response = db.query(Metric).filter(Metric.id == id_metric).first()
    if not response:
        return {'msg': 'Dont exist the id in DB'}
    else:
        if len(parameters.consumo) and len(parameters.date) and len(parameters.device):
            response.consumo = parameters.consumo
            response.device = parameters.device
            response.date = parameters.date
            db.commit()
            info = db.query(Metric).filter(Metric.id == id_metric).first()
            return info

        elif len(parameters.consumo) and len(parameters.date) == 0 and len(parameters.device) == 0  :
            response.consumo = parameters.consumo
            db.commit()
            info = db.query(Metric).filter(Metric.id == id_metric).first()
            return info

        elif len(parameters.device) and len(parameters.date) == 0 and len(parameters.consumo) == 0:
            response.device = parameters.device
            db.commit()
            info = db.query(Metric).filter(Metric.id == id_metric).first()
            return info

        else:
            response.date = parameters.date
            db.commit()
            info = db.query(Metric).filter(Metric.id == id_metric).first()
            return info


def delete_metric(id_metric):
    response = db.query(Metric).filter(Metric.id == id_metric).first()
    if not response:
        return {'msg': 'Dont exist the id in DB'}
    else:
        db.delete(response)
        db.commit()
        return {'msg':'deleted!'}