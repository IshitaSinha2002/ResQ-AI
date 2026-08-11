<h1>ResQ AI</h1>

<h3>Disaster Response Command Center powered by Multi-Agent AI</h3>

<p>
ResQ AI is an AI-powered disaster response coordination system built using
<strong>LangChain</strong> and <strong>LangGraph</strong>.
</p>

<p>
The system simulates a centralized disaster command center where multiple
specialized AI agents analyze the same disaster situation from different
operational perspectives.
</p>

<p>
Instead of relying on a single AI agent to handle every aspect of a disaster,
ResQ AI assigns different responsibilities to specialized commanders and then
uses a <strong>Central Response Coordinator</strong> to combine their
recommendations into one unified response plan.
</p>

<hr>

<h2>Problem</h2>

<p>
Disaster response involves multiple departments, each with different priorities.
</p>

<ul>
  <li>Medical teams prioritize injured civilians and hospitals.</li>
  <li>Logistics teams prioritize supplies, transportation, and shelters.</li>
  <li>Police prioritize public safety, evacuation, and traffic control.</li>
  <li>Fire departments prioritize rescue operations and physical hazards.</li>
  <li>Weather teams monitor environmental conditions and secondary risks.</li>
  <li>Communication teams coordinate emergency information and public alerts.</li>
</ul>

<p>
These priorities can sometimes conflict.
</p>

<p>
A medical team may need immediate ambulance access, while the police department
may need to restrict access to the same area. Logistics may need to transport
supplies through a route that weather conditions make unsafe.
</p>

<p>
A centralized system is therefore needed to <strong>coordinate these different
perspectives and produce one actionable response plan</strong>.
</p>

<hr>

<h2>Solution</h2>

<p>
ResQ AI uses a <strong>multi-agent architecture</strong> where each AI agent
acts as a specialized emergency commander.
</p>

<p>
The agents independently analyze the disaster situation according to their
responsibilities.
</p>

<p>
Their recommendations are stored in a shared <strong>LangGraph state</strong>.
</p>

<p>
A final <strong>Central Disaster Response Coordinator</strong> then analyzes
all departmental recommendations, resolves conflicts, prioritizes actions,
and generates a unified disaster response plan.
</p>

<hr>

<h2>AI Agents</h2>

<h3>Medical Commander</h3>

<p>Focuses on:</p>

<ul>
  <li>Casualty assessment</li>
  <li>Triage priorities</li>
  <li>Ambulance requirements</li>
  <li>Hospital capacity</li>
  <li>Medical supplies</li>
  <li>Emergency medical operations</li>
</ul>

<h3>Logistics Commander</h3>

<p>Focuses on:</p>

<ul>
  <li>Food and water</li>
  <li>Medical supplies</li>
  <li>Emergency shelters</li>
  <li>Transportation</li>
  <li>Fuel</li>
  <li>Rescue equipment</li>
  <li>Resource allocation</li>
</ul>

<h3>Police Commander</h3>

<p>Focuses on:</p>

<ul>
  <li>Evacuation</li>
  <li>Crowd control</li>
  <li>Traffic management</li>
  <li>Emergency routes</li>
  <li>Security</li>
  <li>Restricted areas</li>
  <li>Protection of critical infrastructure</li>
</ul>

<h3>Fire Department Commander</h3>

<p>Focuses on:</p>

<ul>
  <li>Search and rescue</li>
  <li>Fire suppression</li>
  <li>Collapsed structures</li>
  <li>Gas leaks</li>
  <li>Hazardous materials</li>
  <li>Rescue equipment</li>
  <li>Structural risks</li>
</ul>

<h3>Weather Commander</h3>

<p>Focuses on:</p>

<ul>
  <li>Severe weather</li>
  <li>Rainfall and flooding</li>
  <li>Wind conditions</li>
  <li>Temperature</li>
  <li>Visibility</li>
  <li>Secondary environmental risks</li>
  <li>Weather-related threats to responders</li>
</ul>

<h3>Communications Commander</h3>

<p>Focuses on:</p>

<ul>
  <li>Emergency communication channels</li>
  <li>Public safety announcements</li>
  <li>Evacuation instructions</li>
  <li>Emergency alerts</li>
  <li>Coordination between departments</li>
  <li>Preventing misinformation</li>
  <li>Communication failures</li>
</ul>

<hr>

<h2>Central Response Coordinator</h2>

<p>
The Central Response Coordinator receives the recommendations from all six
specialized agents.
</p>

<p>It is responsible for:</p>

<ul>
  <li>Identifying the most urgent life-safety priorities</li>
  <li>Resolving conflicts between departments</li>
  <li>Prioritizing limited resources</li>
  <li>Identifying dependencies between departments</li>
  <li>Considering environmental risks</li>
  <li>Establishing an action sequence</li>
  <li>Creating one coordinated response plan</li>
</ul>

<p>
The coordinator does <strong>not simply combine the responses</strong>. It
evaluates them and determines which actions should take priority.
</p>

<hr>

<h2>Workflow</h2>

<p>The system follows a LangGraph-based workflow:</p>

<pre>
User Input
    |
    v
Disaster Situation
    |
    v
LangGraph State
    |
    +----------------+----------------+----------------+
    |                |                |
    v                v                v
 Medical         Logistics         Police
 Commander       Commander         Commander
    |                |                |
    +----------------+----------------+
                     |
          +----------+----------+
          |          |          |
          v          v          v
        Fire      Weather   Communications
      Commander   Commander    Commander
          |          |          |
          +----------+----------+
                     |
                     v
          Central Response Coordinator
                     |
                     v
          Unified Response Plan
</pre>

<hr>

<h2>LangGraph State</h2>

<p>
The agents communicate through a shared <code>DisasterState</code>.
</p>

<pre>
DisasterState
|
+-- situation
+-- medical_response
+-- logistics_response
+-- police_response
+-- fire_response
+-- weather_response
+-- communication_response
+-- final_plan
</pre>

<p>
Each specialized agent contributes its recommendation to the state.
</p>

<p>
The Central Response Coordinator then uses these responses to generate the
<code>final_plan</code>.
</p>

<hr>

<h2>Tech Stack</h2>

<ul>
  <li>Python</li>
  <li>LangChain</li>
  <li>LangGraph</li>
  <li>Groq</li>
  <li>Llama 3.3 70B Versatile</li>
  <li>python-dotenv</li>
</ul>

<hr>

<h2>Project Structure</h2>

<pre>
ResQ-AI/
|
+-- .env
+-- .gitignore
+-- requirements.txt
+-- main.py
|
+-- agents/
|   +-- medical.py
|   +-- logistics.py
|   +-- police.py
|   +-- fire.py
|   +-- weather.py
|   +-- communications.py
|   +-- coordinator.py
|
+-- graph/
    +-- state.py
    +-- workflow.py
</pre>

<hr>

<h2>How It Works</h2>

<p>
The user provides a disaster scenario through the command line.
</p>

<pre>
A magnitude 7.2 earthquake has struck a densely populated city.
Several buildings have collapsed, roads are blocked, and hundreds
of people are injured.
</pre>

<p>
The situation is passed into the LangGraph workflow.
</p>

<p>
Each specialized commander analyzes the situation from its own perspective.
</p>

<p>
The resulting recommendations are stored in the shared state.
</p>

<p>
Finally, the Central Response Coordinator analyzes all recommendations and
generates a unified response plan.
</p>

<p>The final output contains:</p>

<ol>
  <li>Department-level recommendations</li>
  <li>Resource priorities</li>
  <li>Coordination requirements</li>
  <li>Public communication priorities</li>
  <li>Risks and contingencies</li>
  <li>Final coordinated response plan</li>
</ol>

<hr>

<h2>Running the Project</h2>

<h3>1. Clone the repository</h3>

<pre>
git clone &lt;repository-url&gt;
cd ResQ-AI
</pre>

<h3>2. Create .env</h3>

<p>Add your Groq API key:</p>

<pre>
GROQ_API_KEY=your_groq_api_key
</pre>

<h3>3. Install dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>4. Run the application</h3>

<pre>
python main.py
</pre>

<h3>5. Enter a disaster situation</h3>

<pre>
Describe the disaster situation:
&gt; A major earthquake has struck a densely populated city...
</pre>

<p>
ResQ AI will then generate responses from each emergency commander and
produce the final coordinated response plan.
</p>

<hr>

<h2>Key Features</h2>

<ul>
  <li>Multi-agent disaster response</li>
  <li>Specialized AI commanders</li>
  <li>Shared LangGraph state</li>
  <li>Centralized response coordination</li>
  <li>Conflict resolution between departments</li>
  <li>Resource prioritization</li>
  <li>Risk-aware decision making</li>
  <li>Dynamic user-provided disaster scenarios</li>
  <li>LLM-powered emergency planning</li>
</ul>

<hr>

<h2>Future Enhancements</h2>

<ul>
  <li>Real-time weather API integration</li>
  <li>Live emergency service data</li>
  <li>Geographic and map-based visualization</li>
  <li>Hospital capacity APIs</li>
  <li>Real-time traffic and road-condition data</li>
  <li>Persistent incident memory</li>
  <li>Human approval checkpoints</li>
  <li>Streaming agent responses</li>
  <li>Web-based command center dashboard</li>
</ul>

<hr>

<h2>Project Objective</h2>

<p>
ResQ AI demonstrates how <strong>LangChain and LangGraph can be used to build
a coordinated multi-agent AI system</strong> where specialized agents
collaborate on complex real-world decision-making problems.
</p>

<p>
The project focuses on moving beyond a single LLM response toward a structured
system of <strong>specialized reasoning, shared state, coordination, and
unified decision-making</strong>.
</p>
