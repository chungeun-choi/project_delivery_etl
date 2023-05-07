from functools import wraps
from sqlmodel.main import SQLModelMetaclass


from pydantic import BaseModel


class ConvertSchemaToModel:
    def __init__(self, model_class, schema_class):
        self.model_class = (
            model_class() if isinstance(model_class, SQLModelMetaclass) else model_class
        )

        self.schema_class = schema_class

    def __call__(self):
        fields = self.schema_class.__dict__.copy()
        for field_name, field_value in fields.items():
            setattr(self.model_class, field_name, field_value)

        return self.model_class
