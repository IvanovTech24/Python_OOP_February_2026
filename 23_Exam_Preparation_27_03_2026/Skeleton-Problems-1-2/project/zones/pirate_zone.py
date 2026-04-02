from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        sorted_ships = self.get_ships()
        pirate_ships = [s for s in sorted_ships if s.__class__.__name__ == "RoyalBattleship"]
        pirates_count = len(pirate_ships)

        result = [
            f"@Pirate Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Pirate Zone: {len(sorted_ships)}, {pirates_count} out of them are Royal Battleships."
        ]

        if sorted_ships:
            ship_name = ", ".join(s.name for s in sorted_ships)
            result.append(f"#{ship_name}#")

        return "\n".join(result)