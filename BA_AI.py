
import os

from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai_tools import MCPServerAdapter


load_dotenv()

api_key = os.getenv("API_TOKEN")

if not api_key:
    raise ValueError("API_TOKEN is missing from your .env file")


llm = LLM(
    model="openrouter/openai/gpt-4o-mini",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    temperature=0.2
)


def analyse_business_idea(business_idea, location, target_customers):

    server_params = {
        "url": "http://127.0.0.1:8000/sse"
    }

    # Connect to the MCP server
    with MCPServerAdapter(server_params) as tools:

        business_analyst = Agent(
            role="Business Idea Analyst",

            goal=(
                "Help entrepreneurs examine their business ideas "
                "and understand their potential opportunities and challenges."
            ),

            backstory=(
                "You are a practical business analyst who helps "
                "people think through business ideas. You provide "
                "clear, realistic and useful assessments without "
                "making unsupported claims."
            ),

            tools=tools,
            llm=llm,
            verbose=True
        )

        analysis_task = Task(
            description="""
            Analyse the following business idea:

            Business idea: {business_idea}
            Location: {location}
            Intended customers: {target_customers}

            Use the available MCP tool to prepare the analysis.

            Present your assessment under these headings:

            1. Business Idea Overview
            2. Potential Target Customers
            3. Customer Problems and Needs
            4. Business Opportunities
            5. Potential Challenges and Risks
            6. Questions to Investigate
            7. Preliminary Feasibility Assessment

            Explain your findings in simple, practical language.

            Do not invent statistics or claim that you have
            conducted actual market research.

            Clearly distinguish assumptions from known information.
            """,

            expected_output=(
                "A structured business idea assessment with "
                "practical observations, opportunities, risks "
                "and recommendations for further investigation."
            ),

            agent=business_analyst
        )

        business_crew = Crew(
            agents=[business_analyst],
            tasks=[analysis_task],
            verbose=True
        )

        result = business_crew.kickoff(
            inputs={
                "business_idea": business_idea,
                "location": location,
                "target_customers": target_customers
            }
        )

        return str(result)
