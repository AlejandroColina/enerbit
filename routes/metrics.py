from fastapi import APIRouter, status, Path


from db.services.crud import create_metric, get_all, get_a_metric, update_metric, delete_metric
from db.models.pydantic_model import Metric

router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK)
def all_metrics():
    consult = get_all()
    return consult


@router.get('/{id_metric}', status_code=status.HTTP_200_OK)
def one_metric(id_metric: int = Path(..., gt=0)):
    return get_a_metric(id_metric)


@router.post('/', response_model=Metric, status_code=status.HTTP_201_CREATED)
def create_a_metric(metric: Metric):
    return create_metric(metric)


@router.put('/{id_metric}', status_code=status.HTTP_200_OK)
def update_a_metric(metric: Metric, id_metric: int = Path(..., gt=0)):
    if not len(metric.consumo) and not metric.date > 0:
        return {'msg': 'Must be consumo or date.'}
    else:
        return update_metric(id_metric, metric)


@router.delete('/{id_metric}',
            status_code=status.HTTP_301_MOVED_PERMANENTLY)
def delete_a_metric(id_metric):
    return delete_metric(id_metric)