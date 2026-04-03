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
        if client_type == "RegularClient":
            new_client = RegularClient(client_name, client_phone_number)
        elif client_type == "BusinessClient":
            new_client = BusinessClient(client_name, client_phone_number)
        else:
            raise ValueError("Unknown client type!")

        existing_client = next((c for c in self.clients if c.phone_number == client_phone_number), None)

        if existing_client:
            raise ValueError("This phone number has been used!")


        self.clients.append(new_client)
        return f"{client_name} is successfully added as a {client_type}."


    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if not client:
            raise ValueError("Client not found!")

        available_plants = [p for p in self.plants if p.name == plant_name]
        if not available_plants:
            raise ValueError("Plants not found!")

        if len(available_plants) < plant_quantity:
            return "Not enough plant quantity."

        order_amount = (available_plants[0].price * plant_quantity) * (1 - client.discount / 100)
        for _ in range(plant_quantity):
            remove_plant = next((p for p in self.plants if p.name == plant_name))
            self.plants.remove(remove_plant)

        self.income += order_amount
        client.update_total_orders()
        client.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"


    def remove_plant(self, plant_name: str):
        existing_plant = next((p for p in self.plants if p.name == plant_name), None)

        if not existing_plant:
            return "No such plant name."

        details = existing_plant.plant_details()
        self.plants.remove(existing_plant)
        return f"Removed {details}"


    def remove_clients(self):
        clients_with_order = [c for c in self.clients if c.total_orders > 0]
        count = len(self.clients) - len(clients_with_order)
        self.clients = clients_with_order
        return f"{count} client/s removed."


    def shop_report(self):
        counts = {} # {"name": count}
        for p in self.plants:
            if p.name not in counts:
                counts[p.name] = 0
            counts[p.name] += 1
        unique_plant_names = list(counts.keys())

        sorted_plant_names = sorted(unique_plant_names, key=lambda name: (-counts[name], name))
        sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))
        total_orders_count = sum(c.total_orders for c in self.clients)

        result = [
            "~Flower Shop Report~",
            f"Income: {self.income:.2f}",
            f"Count of orders: {total_orders_count}",
            f"~~Unsold plants: {len(self.plants)}~~"
        ]

        for name in sorted_plant_names:
            plant_count = counts[name]
            result.append(f"{name}: {plant_count}")

        result.append(f"~~Clients number: {len(self.clients)}~~")

        for client in sorted_clients:
            details = client.client_details()
            result.append(details)

        return "\n".join(result)
