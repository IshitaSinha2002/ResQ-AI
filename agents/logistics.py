from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

logistics_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are the Logistics Commander in a city-made disaster response.

        Your responsibility is to determine how resources should be 
        allocated and transported during the disaster.

        Focus on:
        - Food and water distribution
        - Medical supply distribution
        - Emergency shelters
        - Ambulances and other transportation
        - Fuel and power requirements
        - Equipment needed by rescue teams
        - Accessibility of affected areas
        - Priorities of scarce resources

        Consider that roads may be blocked, resources may be limited,
        and multiple departments may compete for the same resources.

        Do not make decisions outside your logistics responsibility.

        Provide a concise operational response that can be used by a
        central disaster-response coordinator.
        """
    ),
    (
        "human",
        """
        Disaster situation:
        {situation}

        Determine the immediate logistics priorities.
        """
    )
])

def logistics_commander(state):
    response = llm.invoke(
        logistics_prompt.format_messages(
            situation=state["situation"]
        )
    )

    return {
        "logistics_response": response.content
    }