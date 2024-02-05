from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class CartBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id: int


class CreateCart(CartBase):
    model_config = ConfigDict(from_attributes=True)

    user_id: int


class ReadCart(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    store_id: int


class ReadCartItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id: int
    category_name: Optional[str] = None
    name: str
    quantity: int
    unit_price: int


class ReadCartResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    cart_items: List[ReadCartItem] = None
    total_price: Optional[int] = None


class ReadCartItemTotal(ReadCartItem):
    model_config = ConfigDict(from_attributes=True)

    total_price: int


class ReadCartItemsOrder(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id: int
    quantity: int
    unit_price: int


class CreateOrder(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    store_id: int
    order_type_id: int


class CreateCustomerInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tg_user_name: Optional[str] = None
    table_number: Optional[str] = None
    delivery_address: Optional[str] = None
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None
    customer_comment: Optional[str] = None
