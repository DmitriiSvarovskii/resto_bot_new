from .cart_callbacks import CartEditCallbackFactory


class ProductIdCallbackFactory(
    CartEditCallbackFactory,
    prefix='pr',
):
    category_id: int


class ProductIdAdminCallbackFactory(
    ProductIdCallbackFactory,
    prefix='prad',
):
    pass
