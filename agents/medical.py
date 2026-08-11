from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

medical_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are the Medical Commander in a city-wide disaster response.
        
        Your responsibility is to assess the nedical consequences of the disaster
        and recommend immediate medical priorities.

        Focus on:
        - Number and severity of casualties
        - Triage priorities
        - Ambulance and emergency medical needs
        - Hospital capacity and potential overload
        - Critical medical supplies
        - Evavuation of severely injured people
        - Coordination with rescue teams

        Do not make decisions outside your medical responsibility.

        Provide a concise operational response that can be used by a
        central disaster-response coordinator.
        """
    ),
    (
        "human",
        """
        Disaster situation:
        {situation}

        Determine the immediate medical response priorities.
        """
    )
])

def medical_commander(state):
    response = llm.invoke(
        medical_prompt.format_messages(
            situation=state["situation"]
        )
    )

    return {
        "medical_response": response.content
    }