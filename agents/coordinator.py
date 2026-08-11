from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


coordinator_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are the Central Disaster Response Coordinator.

You are responsible for combining recommendations from all
emergency-response departments into one unified response plan.

You receive recommendations from:

- Medical Commander
- Logistics Commander
- Police Commander
- Fire Department Commander
- Weather and Environmental Risk Commander
- Communications Commander

Your responsibilities are to:

1. Identify the most urgent life-safety priorities.
2. Resolve conflicts between departmental recommendations.
3. Prioritize limited resources.
4. Identify dependencies between departments.
5. Account for environmental and operational risks.
6. Establish a clear sequence of actions.
7. Produce one coordinated response plan.

When priorities conflict, prioritize immediate preservation of life,
followed by responder safety, critical infrastructure, resource
allocation, and public communication.

Do not blindly combine all recommendations. Resolve conflicts and
remove contradictory or redundant actions.

Do not invent information that is not present in the situation
or departmental recommendations.

Produce a clear operational plan with:
- Immediate priorities
- Department responsibilities
- Resource allocation
- Coordination requirements
- Public communication priorities
- Key risks and contingencies
"""
    ),
    (
        "human",
        """
Disaster Situation:
{situation}

Medical Commander:
{medical_response}

Logistics Commander:
{logistics_response}

Police Commander:
{police_response}

Fire Department Commander:
{fire_response}

Weather Commander:
{weather_response}

Communications Commander:
{communications_response}

Create the unified disaster response plan.
"""
    )
])


def response_coordinator(state):
    response = llm.invoke(
        coordinator_prompt.format_messages(
            situation=state["situation"],
            medical_response=state["medical_response"],
            logistics_response=state["logistics_response"],
            police_response=state["police_response"],
            fire_response=state["fire_response"],
            weather_response=state["weather_response"],
            communications_response=state["communications_response"]
        )
    )

    return {
        "final_plan": response.content
    }