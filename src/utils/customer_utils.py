from src.models import Customer
from src.schemas.customer_schemas import CreateCustomer


def compare_customer_data(
    customer: Customer,
    data: CreateCustomer
) -> bool:
    if customer is None:
        return False
    if customer.first_name != data.first_name:
        return False
    if customer.last_name != data.last_name:
        return False
    if customer.username != data.username:
        return False
    if customer.resourse != data.resourse:
        return False
    return True
