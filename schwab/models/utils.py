from pydantic.alias_generators import to_camel
from pydantic import BaseModel, ConfigDict


class SchwabDataModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
