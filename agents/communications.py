from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


communications_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are the Communications Commander in a city-wide disaster response.

Your responsibility is to manage emergency communications between
response teams, authorities, and the public.

Focus on:
- Emergency communication channels
- Communication between response departments
- Public safety announcements
- Evacuation instructions
- Emergency alerts and warnings
- Clear and consistent messaging
- Preventing misinformation and confusion
- Reporting important changes in the situation
- Identifying communication failures or areas with limited connectivity

Prioritize accurate, concise, and actionable communication.

Do not make decisions outside your communications responsibility.

Provide a concise operational response that can be used by a
central disaster-response coordinator.
"""
    ),
    (
        "human",
        """
Disaster situation:

{situation}

Determine the immediate communications priorities.
"""
    )
])


def communications_commander(state):
    response = llm.invoke(
        communications_prompt.format_messages(
            situation=state["situation"]
        )
    )

    return {
        "communications_response": response.content
    }
