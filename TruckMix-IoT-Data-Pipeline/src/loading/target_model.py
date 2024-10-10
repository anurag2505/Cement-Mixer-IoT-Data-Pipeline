from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TruckMixData(Base):
    __tablename__ = 'truck_mix_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    truck_id = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    cement_weight = Column(Float, nullable=False)
    water_weight = Column(Float, nullable=False)
    sand_weight = Column(Float, nullable=False)
    gravel_weight = Column(Float, nullable=False)
    mixer_speed = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)

    def __repr__(self):
        return f"<TruckMixData(truck_id='{self.truck_id}', timestamp='{self.timestamp}', cement_weight={self.cement_weight}, water_weight={self.water_weight}, sand_weight={self.sand_weight}, gravel_weight={self.gravel_weight}, mixer_speed={self.mixer_speed}, temperature={self.temperature})>"