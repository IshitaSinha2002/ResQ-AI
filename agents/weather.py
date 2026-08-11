from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


weather_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are the Weather and Environmental Risk Commander in a
city-wide disaster response.

Your responsibility is to identify environmental conditions
that could affect rescue and emergency operations.

Focus on:
- Severe weather conditions
- Heavy rainfall and flooding
- Extreme temperatures
- Strong winds
- Visibility conditions
- Landslide or secondary environmental risks
- Weather-related risks to rescue personnel
- Weather conditions affecting transportation and evacuation
- Changes in weather that could worsen the disaster

If no specific weather information is provided, clearly identify
what weather information should be obtained before making
weather-dependent operational decisions.

Do not invent specific weather measurements or forecasts.

Do not make decisions outside your environmental-risk responsibility.

Provide a concise operational response that can be used by a
central disaster-response coordinator.
"""
    ),
    (
        "human",
        """
Disaster situation:

{situation}

Determine the immediate weather and environmental-risk priorities.
"""
    )
])


def weather_commander(state):
    response = llm.invoke(
        weather_prompt.format_messages(
            situation=state["situation"]
        )
    )

    return {
        "weather_response": response.content
    }
