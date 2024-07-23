from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, index=True)
    input = Column(String, nullable=False)
    output = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Metric(Base):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key=True, index=True)
    interaction_id = Column(Integer, ForeignKey("interactions.id"), nullable=False)
    metric_name = Column(String, nullable=False)
    input_value = Column(Float)
    output_value = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)


class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    interaction_id = Column(Integer, ForeignKey("interactions.id"), nullable=False)
    metric_name = Column(String, nullable=False)
    element = Column(String, nullable=False)
    alert_type = Column(String, nullable=False)
    value = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
