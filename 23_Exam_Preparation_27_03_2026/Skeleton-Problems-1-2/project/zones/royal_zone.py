from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        sorted_ships = self.get_ships()
        pirate_ships = [s for s in sorted_ships if s.__class__.__name__ == "PirateBattleship"]
        pirates_count = len(pirate_ships)

        result = [
            f"@Royal Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Royal Zone: {len(sorted_ships)}, {pirates_count} out of them are Pirate Battleships."
        ]

        if sorted_ships:
            ship_name = ", ".join(s.name for s in sorted_ships)
            result.append(f"#{ship_name}#")

        return "\n".join(result)