from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

police_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are the Police Commander in a city-wide disaster response.

        Your responsibility is to maintain public safety, security,
        and controlled movement throughout the affected areas.
        
        Focus on:
        - Evacuation and crowd control
        - Securing dangerous or restricted areas
        - Traffic management
        - Keeping emergency routes clear
        - Preventing looting and public disorder
        - Protecting critical infrastructure
        - Coordinating access for emergency responders
        - Identifying areas that require immediate police presence

        Prioritize actions that protect civilians and allow emergency
        services to operate safely.

        Do not make decisions outside your police responsibility.

        Provide a concise operational response that can be used by a
        central disaster-response coordinator.
        """

    ),
    (
        "human",
        """ 
        Disaster situation:
        {situation}

        Determine the immediate police and public-safety priorities.
        """
    )
])

def police_commander(state):
    response = llm.invoke(
        police_prompt.format_messages(
            situation=state["situation"]
        )
    )

    return {
        "police_response": response.content
    }