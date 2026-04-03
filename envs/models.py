from dataclasses import dataclass
from openenv.core.env_server import Action, Observation, State

@dataclass
class ShieldAction(Action):
    command: str  # e.g., "run_deep_scan", "purge_ads", "toggle_privacy"
    parameters: dict = None

@dataclass
class ShieldObservation(Observation):
    spam_count: int
    status: str
    assets_organized: int
    success: bool