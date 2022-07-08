from fastapi import APIRouter, status, Path
from db   .services.crud import create_metric, get_all, get_a_metric, update_metric, delete_metric
from db.models.pydantic_model import Metric

router = APIRouter()

@router.get('/metrics', status_code=status.HTTP_200_OK)
def all_metrics():
    consult = get_all()
    return consult


@router.get('/metrics/{id_metric}', status_code=status.HTTP_200_OK)
def one_metric(id_metric: int = Path(..., gt=0)):
    return get_a_metric(id_metric)


@router.post('/metrics', status_code=status.HTTP_201_CREATED)
def create_a_metric(metric: Metric):
    create_metric(metric)
    return 'Created!'


@router.put('/metrics/{id_metric}', status_code=status.HTTP_200_OK)
def update_a_metric(metric: Metric, id_metric: int = Path(..., gt=0)):
    if not len(metric.consumo) and not metric.date > 0:
        return {'msg': 'Must be consumo or date.'}
    else:
        return update_metric(id_metric, metric)


@router.delete('/metrics/{id_metric}',
            status_code=status.HTTP_301_MOVED_PERMANENTLY)
def delete_a_metric(id_metric):
    return delete_metric(id_metric)