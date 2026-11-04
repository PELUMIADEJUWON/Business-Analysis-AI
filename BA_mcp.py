from mcp.server.fastmcp import FastMCP

# 1. Create our MCP server
mcp = FastMCP("Business Idea Reality Check")


# 2. Create our business analysis tool
@mcp.tool()
def prepare_business_analysis(
    business_idea: str,
    location: str,
    target_customers: str
) -> str:
    """
    Prepare business details for the CrewAI business analyst.
    """

    analysis_information = f"""
    BUSINESS IDEA: {business_idea}

    LOCATION: {location}

    TARGET CUSTOMERS: {target_customers}

    Analyse these details by considering:

    1. Potential customer needs and problems.
    2. Possible business opportunities.
    3. Potential challenges and risks.
    4. Questions the entrepreneur should investigate.
    5. Factors that could affect business feasibility.
    """

    return analysis_information


# 3. Start the MCP server
if __name__ == "__main__":
    mcp.run(transport="sse")