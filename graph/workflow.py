from langgraph.graph import StateGraph, START, END

from graph.state import DisasterState

from agents.medical import medical_commander
from agents.logistics import logistics_commander
from agents.police import police_commander
from agents.fire import fire_commander
from agents.weather import weather_commander
from agents.communications import communications_commander
from agents.coordinator import response_coordinator


def build_graph():
    workflow = StateGraph(DisasterState)

    workflow.add_node("medical", medical_commander)
    workflow.add_node("logistics", logistics_commander)
    workflow.add_node("police", police_commander)
    workflow.add_node("fire", fire_commander)
    workflow.add_node("weather", weather_commander)
    workflow.add_node("communications", communications_commander)
    workflow.add_node("coordinator", response_coordinator)

    workflow.add_edge(START, "medical")
    workflow.add_edge("medical", "logistics")
    workflow.add_edge("logistics", "police")
    workflow.add_edge("police", "fire")
    workflow.add_edge("fire", "weather")
    workflow.add_edge("weather", "communications")
    workflow.add_edge("communications", "coordinator")
    workflow.add_edge("coordinator", END)

    return workflow.compile()