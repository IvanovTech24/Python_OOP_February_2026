from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []


    def add_zone(self, zone_type: str, zone_code: str) -> str:
        zone_classes = {
            "RoyalZone": RoyalZone,
            "PirateZone": PirateZone
        }

        if zone_type not in zone_classes:
            raise Exception("Invalid zone type!")

        all_existing_code = [z.code for z in self.zones]
        if zone_code in all_existing_code:
            raise Exception("Zone already exists!")

        new_zone = zone_classes[zone_type](zone_code)
        self.zones.append(new_zone)

        return f"A zone of type {zone_type} was successfully added."


    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int) -> str:
        ship_classes = {
            "RoyalBattleship": RoyalBattleship,
            "PirateBattleship": PirateBattleship
        }

        if ship_type not in ship_classes:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        new_ship = ship_classes[ship_type](name, health, hit_strength)
        self.ships.append(new_ship)

        return f"A new {ship_type} was successfully added."


    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship):
        ship_type = ship.__class__.__name__
        zone_type = zone.__class__.__name__

        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if (ship_type.startswith("Royal") and zone_type.startswith("Royal")) \
            or (ship_type.startswith("Pirate") and zone_type.startswith("Pirate")):
        # if (isinstance(ship, RoyalBattleship) and isinstance(zone, RoyalZone)) or \
        # (isinstance(ship, PirateBattleship) and isinstance(zone, PirateZone)):
            ship.is_attacking = True
        else:
            ship.is_attacking = False

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."


    def remove_battleship(self, ship_name: str):
        ship = next((s for s in self.ships if s.name == ship_name ), None)

        if not ship:
            return "No ship with this name!"

        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)

        return f"Successfully removed ship {ship_name}."


    def start_battle(self, zone: BaseZone):
        attackers = [s for s in zone.ships if s.is_attacking]
        targets = [s for s in zone.ships if not s.is_attacking]

        if not attackers or not targets:
            return "Not enough participants. The battle is canceled."

        attacker = max(attackers, key=lambda s: s.hit_strength)
        target = max(targets, key=lambda s: s.health)

        attacker.attack()
        target.take_damage(attacker)

        if target.health <= 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."

        elif attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [s for s in self.ships if s.is_available]
        result = [f"Available Battleships: {len(available_ships)}"]

        if available_ships:
            available_ships_names = ", ".join(s.name for s in available_ships)
            result.append(f"#{available_ships_names}#")

        result.append(f"***Zones Statistics:***")
        result.append(f"Total Zones: {len(self.zones)}")

        for zone in sorted(self.zones, key=lambda z: z.code):
            result.append(zone.zone_info())

        return "\n".join(result)
