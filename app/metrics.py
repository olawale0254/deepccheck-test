from .models import Metric, Alert
from .database import SessionLocal
import os

THRESHOLD_VALUE = float(os.getenv('THRESHOLD_VALUE', '100.0'))
OUTLIER_FACTOR = float(os.getenv('OUTLIER_FACTOR', '2.0'))

def calculate_metrics(interaction):
    metrics = []

    try:
        input_length = len(interaction.input)
        output_length = len(interaction.output)

        metrics.append(Metric(interaction_id=interaction.id, metric_name="input_length", input_value=input_length))
        metrics.append(Metric(interaction_id=interaction.id, metric_name="output_length", output_value=output_length))

    except Exception as e:
        print(f"Error calculating metrics for interaction ID: {interaction.id}: {e}")

    return metrics

def check_for_alerts(metric):
    alerts = []
    db = SessionLocal()
    
    # Threshold Alert
    if metric.input_value and metric.input_value > THRESHOLD_VALUE:
        alerts.append(Alert(
            interaction_id=metric.interaction_id,
            metric_name=metric.metric_name,
            element="input",
            alert_type="threshold",
            value=metric.input_value
        ))

    if metric.output_value and metric.output_value > THRESHOLD_VALUE:
        alerts.append(Alert(
            interaction_id=metric.interaction_id,
            metric_name=metric.metric_name,
            element="output",
            alert_type="threshold",
            value=metric.output_value
        ))

    # Outlier Alert
    metrics = db.query(Metric).filter(Metric.metric_name == metric.metric_name).all()
    if metrics:
        input_values = [m.input_value for m in metrics if m.input_value is not None]
        output_values = [m.output_value for m in metrics if m.output_value is not None]
        
        if input_values:
            avg_input = sum(input_values) / len(input_values)
            if metric.input_value and metric.input_value > avg_input * OUTLIER_FACTOR:
                alerts.append(Alert(
                    interaction_id=metric.interaction_id,
                    metric_name=metric.metric_name,
                    element="input",
                    alert_type="outlier",
                    value=metric.input_value
                ))

        if output_values:
            avg_output = sum(output_values) / len(output_values)
            if metric.output_value and metric.output_value > avg_output * OUTLIER_FACTOR:
                alerts.append(Alert(
                    interaction_id=metric.interaction_id,
                    metric_name=metric.metric_name,
                    element="output",
                    alert_type="outlier",
                    value=metric.output_value
                ))

    db.close()
    return alerts
