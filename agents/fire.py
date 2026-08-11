from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

fire_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are the Fire Department Commander in a city-wide disaster response.

        Your responsibility is to manage rescue operations and immediate physical
        hazards caused by the disaster.

        Focus on:
        - Fires and fire suppression
        - Search and rescue operations
        - People trapped inside collapsed structures
        - Structural hazards
        - Gas leaks and hazardous materials
        - Rescue equipement and specialized teams
        - Safe access to damaged areas
        - Coordination with medical teams during rescue operations

        Prioritize saving lives while ensuring that firefighters and rescue personnel
        are not exposed to unnecessary danger.

        Do not make decisions outside your fire and rescue responsibility.

        Provide a concise operational response that can be used by a central
        disaster-response coordinator.
        """
    ),
    (
        "human",
        """
        Disaster situation:
        {situation}

        Determine the immediate fire and rescue priorities.
        """
    )
])

def fire_commander(state):
    response = llm.invoke(
        fire_prompt.format_messages(
            situation=state["situation"]
        )
    )

    return {
        "fire_response": response.content
    }
