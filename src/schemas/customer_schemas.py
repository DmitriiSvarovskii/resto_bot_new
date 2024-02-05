from pydantic import BaseModel, ConfigDict
from typing import Optional


class CustomerBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    resourse: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None


class CreateCustomer(CustomerBase):
    pass


class ReadCustomerInfo(CustomerBase):
    id: int
    is_active: bool


class ReadCustomerAdResourse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    customer_count: int
