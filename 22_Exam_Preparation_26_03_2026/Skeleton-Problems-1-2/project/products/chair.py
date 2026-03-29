from project.products.base_product import BaseProduct


class Chair(BaseProduct):
    MATERIAL: str = "Wood"
    SUB_TYPE: str = "Furniture"
    DISCOUNT = 0.9

    def __init__(self, model: str, price: float):
        super().__init__(model, price, self.MATERIAL, self.SUB_TYPE)

    def discount(self):
        self.price *= self.DISCOUNT