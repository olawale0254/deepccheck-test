from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .database import get_db
from .metrics import calculate_metrics, check_for_alerts
from .models import Alert, Interaction, Metric

router = APIRouter()


class InteractionCreate(BaseModel):
    input: str
    output: str


@router.post("/interactions", response_model=dict)
def log_interaction(interaction: InteractionCreate, db: Session = Depends(get_db)):
    db_interaction = Interaction(input=interaction.input, output=interaction.output)
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)

    metrics = calculate_metrics(db_interaction)
    for metric in metrics:
        db.add(metric)
        db.commit()
        db.refresh(metric)

        alerts = check_for_alerts(metric)
        for alert in alerts:
            db.add(alert)

    db.commit()

    return {"message": "Interaction logged and metrics calculated"}


@router.get("/metrics", response_model=list)
def get_metrics(db: Session = Depends(get_db)):
    metrics = db.query(Metric).all()
    return [
        {
            "interaction_id": m.interaction_id,
            "metric_name": m.metric_name,
            "input_value": m.input_value,
            "output_value": m.output_value,
        }
        for m in metrics
    ]


@router.get("/alerts", response_model=list)
def get_alerts(db: Session = Depends(get_db)):
    alerts = db.query(Alert).all()
    return [
        {
            "interaction_id": a.interaction_id,
            "metric_name": a.metric_name,
            "element": a.element,
            "alert_type": a.alert_type,
            "value": a.value,
        }
        for a in alerts
    ]
