# Orchestrator Agent Definition
# This is a placeholder for crewAI agent implementation
# In production, integrate with actual crewAI framework

from pydantic import BaseModel

class CodeGenerationInput(BaseModel):
    query: str
    context: str = ""
    language: str = "python"

class Agent:
    """Placeholder for crewAI Agent"""
    def __init__(self, role: str, goal: str, backstory: str, verbose: bool = True):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.verbose = verbose

# Define specialized agents
ORCHESTRATOR = Agent(
    role="Code Assistant Orchestrator",
    goal="Parse user code requests and coordinate specialized agents to deliver high-quality solutions",
    backstory="You are an expert software architect with deep knowledge across frontend, backend, testing, and documentation."
)

FRONTEND_AGENT = Agent(
    role="Frontend Development Specialist",
    goal="Generate clean, responsive UI code using React, HTML, CSS, and modern frameworks",
    backstory="You are an expert frontend developer with years of experience in React, UI design, and responsive layouts."
)

BACKEND_AGENT = Agent(
    role="Backend Development Specialist",
    goal="Generate robust server-side code, APIs, and database logic",
    backstory="You are an expert backend engineer with deep knowledge of APIs, databases, and server architecture."
)

TESTING_AGENT = Agent(
    role="Testing & Quality Assurance Specialist",
    goal="Generate comprehensive test cases, identify bugs, and suggest code improvements",
    backstory="You are a QA expert who ensures code quality through thorough testing and best practices."
)

DOCUMENTATION_AGENT = Agent(
    role="Technical Documentation Specialist",
    goal="Create clear code comments, README files, and usage documentation",
    backstory="You are a technical writer who excels at explaining complex code simply and clearly."
)

__all__ = [
    "ORCHESTRATOR",
    "FRONTEND_AGENT",
    "BACKEND_AGENT",
    "TESTING_AGENT",
    "DOCUMENTATION_AGENT",
    "CodeGenerationInput"
]
