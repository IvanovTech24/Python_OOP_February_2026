from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []


    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        valid_types = {
            "RenaissanceArtifact": RenaissanceArtifact,
            "ContemporaryArtifact": ContemporaryArtifact
        }

        if artifact_type not in valid_types.keys():
            raise ValueError("Unknown artifact type!")

        if any(a.name == artifact_name for a in self.artifacts):
            raise ValueError(f"{artifact_name} has been already registered!")

        new_artifact = valid_types[artifact_type](artifact_name, artifact_price, artifact_space)
        self.artifacts.append(new_artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."


    def register_collector(self, collector_type: str, collector_name: str):
        valid_collector = {
            "Museum": Museum,
            "PrivateCollector": PrivateCollector
        }

        if collector_type not in valid_collector:
            raise ValueError("Unknown collector type!")

        if any(c.name == collector_name for c in self.collectors):
            raise ValueError(f"{collector_name} has been already registered!")

        new_collector = valid_collector[collector_type](collector_name)
        self.collectors.append(new_collector)
        return f"{collector_name} is successfully registered as a {collector_type}."


    def perform_purchase(self, collector_name: str, artifact_name: str):

        collector = next((c for c in self.collectors if c.name == collector_name), None)
        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)

        if not  collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."
        else:
            self.artifacts.remove(artifact)
            collector.purchased_artifacts.append(artifact)
            collector.available_money -= artifact.price
            collector.available_space -= artifact.space_required
            return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        existing_artifact = next((a for a in self.artifacts if a.name == artifact_name), None)

        if not existing_artifact:
            return "No such artifact."

        self.artifacts.remove(existing_artifact)
        result = "Removed "
        result += existing_artifact.artifact_information()

        return result


    def fundraising_campaigns(self, max_money: float):
        collectors = [c for c in self.collectors if c.available_money <= max_money]

        for c in collectors:
            c.increase_money()

        return f"{len(collectors)} collector/s increased their available money."


    def get_auction_report(self):
        sorted_collectors = sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts), c.name))

        total_sold = sum(len(c.purchased_artifacts) for c in self.collectors)

        result = [
            f"**Auction statistics**",
            f"Total number of sold artifacts: {total_sold}",
            f"Available artifacts for sale: {len(self.artifacts)}",
            f"***"
        ]

        for c in sorted_collectors:
            result.append(c.__str__())

        return "\n".join(result)
