from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class CreateOrderInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    order_id: int
    order_comment: Optional[str] = None
    customer_phone: Optional[str] = None
    delivery_id: Optional[int] = None
    delivery_latitude: Optional[float] = None
    delivery_longitude: Optional[float] = None
    delivery_comment: Optional[str] = None


class ReadOrderInfo(CreateOrderInfo):
    id: int


class CreateOrderDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    order_id: int
    product_id: int
    quantity: int
    unit_price: float


class CreateCustomerInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    number_phone: Optional[str] = None
    guide: Optional[str] = None


class ReadOrderDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    category_name: Optional[str] = None
    name: str
    quantity: int
    unit_price: int


class ReadSalesSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    category_id: int
    name: str
    quantity: int
    unit_price: int


class ReadSalesSummaryList(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    order_items: List[ReadSalesSummary]
    total_price: float


class ReadOrderList(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    total_price: float


class CreateOrderInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    order_id: int
    order_comment: Optional[str] = None
    customer_phone: Optional[str] = None
    delivery_id: Optional[int] = None
    delivery_latitude: Optional[float] = None
    delivery_longitude: Optional[float] = None
    delivery_comment: Optional[str] = None
