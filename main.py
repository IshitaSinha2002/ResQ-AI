import os
from dotenv import load_dotenv

load_dotenv()

from graph.workflow import build_graph

def main():
    print("\n" + "=" * 70)
    print("RESQ AI — DISASTER RESPONSE COMMAND CENTER")
    print("=" * 70)

    situation = input("\nDescribe the disaster situation:\n")

    initial_state = {
        "situation": situation,
        "medical_response": "",
        "logistics_response": "",
        "police_response": "",
        "fire_response": "",
        "weather_response": "",
        "communication_response": "",
        "final_plan": ""
    }

    graph = build_graph()

    print("\nGenerating coordinated response...\n")

    result = graph.invoke(initial_state)

    print("=" * 70)
    print("DEPARTMENT RESPONSES")
    print("=" * 70)

    print("\nMEDICAL COMMANDER")
    print("-" * 70)
    print(result["medical_response"])

    print("\nLOGISTICS COMMANDER")
    print("-" * 70)
    print(result["logistics_response"])

    print("\nPOLICE COMMANDER")
    print("-" * 70)
    print(result["police_response"])

    print("\nFIRE DEPARTMENT COMMANDER")
    print("-" * 70)
    print(result["fire_response"])

    print("\nWEATHER COMMANDER")
    print("-" * 70)
    print(result["weather_response"])

    print("\nCOMMUNICATIONS COMMANDER")
    print("-" * 70)
    print(result["communication_response"])

    print("\n" + "=" * 70)
    print("FINAL COORDINATED RESPONSE PLAN")
    print("=" * 70)
    print(result["final_plan"])

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()