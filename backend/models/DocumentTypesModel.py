import json

from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.dialects.mysql import TINYINT

from shared.database import base
from .QueriesMixin import QueriesMixin

class DocumentTypesModel(QueriesMixin, base):
    __tablename__ = "document_types"
    
    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    name = Column(String, nullable=False)
    active = Column(TINYINT, nullable=False, default=1)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    def __init__(self, payload: dict = {}):
        self.code = payload.get("code", "")
        self.description = payload.get("description", "")
        self.name = payload.get("name", "")
        
    def __repr__(self) -> str:
        return json.dumps(
            {
                "id": self.id,
                "code": self.code,
                "description": self.description,
                "name": self.name,
                "active": self.active,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)
            }
        )