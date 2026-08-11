from typing import TypedDict

class DisasterState(TypedDict):
    situation: str

    medical_response: str
    logistics_response: str
    police_response: str
    fire_response: str
    weather_response: str
    communication_response: str

    final_plan: str