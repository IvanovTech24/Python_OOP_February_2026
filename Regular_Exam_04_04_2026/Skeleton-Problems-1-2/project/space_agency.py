from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    def __init__(self):
        self.astronauts: list[BaseAstronaut] = []
        self.stations: list[BaseStation] = []


    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        valid_astronauts = {
            "EngineerAstronaut": EngineerAstronaut,
            "ScientistAstronaut": ScientistAstronaut
        }

        if astronaut_type not in valid_astronauts:
            raise ValueError("Invalid astronaut type!")

        if any(a.id_number == astronaut_id_number for a in self.astronauts):
            raise ValueError(f"{astronaut_id_number} has been already added!")

        new_astronaut = valid_astronauts[astronaut_type](astronaut_id_number, astronaut_salary)
        self.astronauts.append(new_astronaut)
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."


    def add_station(self, station_type: str, station_name: str):
        valid_stations = {
            "ResearchStation": ResearchStation,
            "MaintenanceStation": MaintenanceStation
        }

        if station_type not in valid_stations:
            raise ValueError("Invalid station type!")

        if any(s.name == station_name for s in self.stations):
            raise ValueError(f"{station_name} has been already added!")

        new_station = valid_stations[station_type](station_name)
        self.stations.append(new_station)
        return f"{station_name} is successfully added as a {station_type}."


    def assign_astronaut(self, station_name: str, astronaut_type: str):
        exist_station = next((s for s in self.stations if s.name == station_name), None)
        exist_astronaut = next((a for a in self.astronauts if a.specialization == astronaut_type), None)

        if not exist_station:
            raise ValueError(f"Station {station_name} does not exist!")

        if not exist_astronaut:
            raise ValueError("No available astronauts of the type!")

        if exist_station.capacity == 0:
            return "This station has no available capacity."

        self.astronauts.remove(exist_astronaut)
        exist_station.astronauts.append(exist_astronaut)
        exist_station.capacity -= 1
        return f"{exist_astronaut.id_number} was assigned to {station_name}."


    def train_astronauts(self, station: BaseStation, sessions_number: int):
        for _ in range(sessions_number):
            for a in station.astronauts:
                a.train()

        total_stamina = sum(a.stamina for a in station.astronauts)
        return f"{station.name} astronauts have {total_stamina} total stamina after {sessions_number} training session/s."



    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):
        astronaut = next((a for a in station.astronauts if a.id_number == astronaut_id_number), None)

        if not astronaut or astronaut.stamina == 100:
            return "The retirement process was canceled."

        if astronaut.stamina < 100:
            station.astronauts.remove(astronaut)
            station.capacity += 1
            return f"Retired astronaut {astronaut_id_number}."


    def agency_update(self, min_value: float):
        for s in self.stations:
            s.update_salaries(min_value)

        sorted_stations = sorted(self.stations, key=lambda station: (-len(station.astronauts), station.name))

        total_capacity = sum(s.capacity for s in self.stations)
        stations_info = "\n".join(s.status() for s in sorted_stations)
        result = (f"*Space Agency Up-to-Date Report*\n"
                  f"Total number of available astronauts: {len(self.astronauts)}\n"
                  f"**Stations count: {len(self.stations)}; Total available capacity: {total_capacity}**\n"
                  f"{stations_info}")
        return result
