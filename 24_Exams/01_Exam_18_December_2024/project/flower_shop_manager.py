from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    def __init__(self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []


    def add_plant(self, plant_type: str, plant_name: str, plant_price: float,
                  plant_water_needed: int, plant_extra_data: str) -> str:
        if plant_type == "Flower":
            new_plant = Flower(plant_name, plant_price, plant_water_needed, plant_extra_data)
        elif plant_type == "LeafPlant":
            new_plant = LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data)
        else:
            raise ValueError("Unknown plant type!")
        self.plants.append(new_plant)
        return f"{plant_name} is added to the shop as {plant_type}."


    def add_client(self, client_type: str, client_name: str, client_phone_number: str):

        existing_client = next((c for c in self.clients if c.phone_number == client_phone_number), None)

        if existing_client:
            raise ValueError("This phone number has been used!")

        if client_type == "RegularClient":
            new_client = RegularClient(client_name, client_phone_number)
        elif client_type == "BusinessClient":
            new_client = BusinessClient(client_name, client_phone_number)
        else:
            raise ValueError("Unknown client type!")
        self.clients.append(new_client)
        return f"{client_name} is successfully added as a {client_type}."


    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        pass