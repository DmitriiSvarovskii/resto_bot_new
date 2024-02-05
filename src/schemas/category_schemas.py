from pydantic import BaseModel, ConfigDict


class ReadCategory(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    availability: bool
    deleted_flag: bool
