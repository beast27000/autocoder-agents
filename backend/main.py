from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List
import logging
import time
import traceback
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import configuration
from config import settings

# Initialize FastAPI
app = FastAPI(
    title="AutoCoder Agents API",
    description="Multi-agent AI code assistant using crewAI",
    version="1.0.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allow_methods,
    allow_headers=settings.cors_allow_headers,
)

# ============ Pydantic Models ============

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=5, max_length=1000, description="Code request")
    context: Optional[str] = Field(default="", max_length=2000, description="Additional context")
    language: Optional[str] = Field(default="python", description="Programming language")
    
    @validator('query')
    def query_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Query cannot be empty")
        return v
    
    @validator('language')
    def language_valid(cls, v):
        valid_languages = ['python', 'javascript', 'typescript', 'java', 'cpp', 'go', 'csharp', 'rust']
        if v.lower() not in valid_languages:
            raise ValueError(f"Language must be one of: {', '.join(valid_languages)}")
        return v.lower()

class CodeGenerationOutput(BaseModel):
    code: str = Field(..., description="Generated code")
    explanation: str = Field(..., description="Explanation of the code")
    language: str = Field(..., description="Language used")
    complexity: str = Field(default="medium", description="Code complexity")

class QueryResponse(BaseModel):
    success: bool
    data: Optional[CodeGenerationOutput] = None
    error: Optional[str] = None
    agents_involved: List[str] = []
    processing_time_ms: float
    timestamp: str

class HealthResponse(BaseModel):
    status: str
    version: str
    environment: str
    timestamp: str

class AgentInfo(BaseModel):
    name: str
    role: str
    specialty: str

class AgentsListResponse(BaseModel):
    total: int
    agents: List[AgentInfo]

# ============ Mock Orchestrator (Replace with actual crewAI) ============

class MockOrchestrator:
    """AI-powered orchestrator using OpenRouter API"""
    
    def __init__(self):
        self.api_key = settings.openrouter_api_key
        self.model = settings.primary_model
        self.base_url = settings.openrouter_base_url
    
    def process_query(self, query_request: QueryRequest) -> CodeGenerationOutput:
        """Process user query and generate code using OpenRouter API"""
        try:
            # Create the prompt for the AI
            prompt = f"""You are an expert software developer. Generate high-quality, production-ready code for the following request:

Request: {query_request.query}
Language: {query_request.language}
Context: {query_request.context if query_request.context else 'No additional context provided'}

Please provide:
1. Complete, working code that solves the request
2. Brief explanation of the solution
3. Code complexity level (low/medium/high)

Focus on:
- Clean, readable code
- Proper error handling
- Best practices for the chosen language
- Complete implementation (not just templates)

Return the response in this exact JSON format:
{{
    "code": "the complete code here",
    "explanation": "brief explanation of the solution",
    "complexity": "low|medium|high"
}}"""

            # Make API call to OpenRouter
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://autocoder-agents.onrender.com",
                "X-Title": "AutoCoder Agents"
            }
            
            payload = {
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.3,
                "max_tokens": 2000
            }
            
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code != 200:
                raise Exception(f"OpenRouter API error: {response.status_code} - {response.text}")
            
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            
            # Try to parse JSON response
            try:
                parsed = json.loads(content)
                code = parsed.get("code", content)
                explanation = parsed.get("explanation", "Generated code solution")
                complexity = parsed.get("complexity", "medium")
            except json.JSONDecodeError:
                # If not JSON, use the raw content as code
                code = content
                explanation = "Generated code solution using AI"
                complexity = "medium"
            
            return CodeGenerationOutput(
                code=code.strip(),
                explanation=explanation,
                language=query_request.language,
                complexity=complexity
            )
        
        except Exception as e:
            logger.error(f"Error in process_query: {str(e)}", exc_info=True)
            # Fallback to basic template if API fails
            return self._get_fallback_code(query_request)
    
    def _get_fallback_code(self, query_request: QueryRequest) -> CodeGenerationOutput:
        """Fallback method that returns basic code template when API fails"""
        language = query_request.language
        
        code_templates = {
            "python": f"""# Python Solution for: {query_request.query}
# Context: {query_request.context if query_request.context else 'None specified'}

def solution():
    '''
    {query_request.query}
    '''
    # TODO: Implement solution
    pass

if __name__ == "__main__":
    solution()
""",
            "javascript": f"""// JavaScript Solution for: {query_request.query}
// Context: {query_request.context if query_request.context else 'None specified'}

function solution() {{
    // {query_request.query}
    // TODO: Implement solution
}}

solution();
""",
            "typescript": f"""// TypeScript Solution for: {query_request.query}
// Context: {query_request.context if query_request.context else 'None specified'}

interface Config {{
    // {query_request.query}
}}

function solution(): void {{
    // TODO: Implement solution
}}

solution();
""",
            "java": f"""// Java Solution for: {query_request.query}
// Context: {query_request.context if query_request.context else 'None specified'}

public class Solution {{
    // {query_request.query}
    
    public static void main(String[] args) {{
        // TODO: Implement solution
    }}
}}
""",
            "cpp": f"""// C++ Solution for: {query_request.query}
// Context: {query_request.context if query_request.context else 'None specified'}

#include <iostream>
using namespace std;

// {query_request.query}

int main() {{
    // TODO: Implement solution
    return 0;
}}
""",
            "go": f"""// Go Solution for: {query_request.query}
// Context: {query_request.context if query_request.context else 'None specified'}

package main

import "fmt"

// {query_request.query}

func main() {{
    // TODO: Implement solution
}}
""",
        }
        
        code = code_templates.get(language, code_templates["python"])
        
        return CodeGenerationOutput(
            code=code,
            explanation=f"Generated {language.upper()} code template for: {query_request.query}. (Note: This is a fallback template - the AI service may be temporarily unavailable)",
            language=language,
            complexity="low"
        )

# Initialize orchestrator
orchestrator = MockOrchestrator()

# ============ API Endpoints ============

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information"""
    return {
        "name": "AutoCoder Agents API",
        "version": "1.0.0",
        "description": "Multi-agent AI code assistant",
        "documentation": "/api/docs",
        "endpoints": {
            "health": "/health",
            "agents": "/agents",
            "process": "/api/process-query"
        }
    }

@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        environment=settings.environment,
        timestamp=datetime.utcnow().isoformat()
    )

@app.get("/agents", response_model=AgentsListResponse, tags=["Agents"])
async def list_agents():
    """List available agents"""
    agents = [
        AgentInfo(
            name="Orchestrator",
            role="Task Coordinator",
            specialty="Breaking down requests and coordinating agents"
        ),
        AgentInfo(
            name="Frontend Dev Agent",
            role="UI/UX Specialist",
            specialty="React, HTML, CSS, responsive design"
        ),
        AgentInfo(
            name="Backend Dev Agent",
            role="Server-Side Specialist",
            specialty="APIs, databases, business logic"
        ),
        AgentInfo(
            name="Testing Agent",
            role="QA Specialist",
            specialty="Unit tests, bug detection, code review"
        ),
        AgentInfo(
            name="Documentation Agent",
            role="Technical Writer",
            specialty="Code comments, READMEs, API documentation"
        ),
    ]
    
    return AgentsListResponse(
        total=len(agents),
        agents=agents
    )

@app.post("/api/process-query", response_model=QueryResponse, tags=["Processing"])
async def process_query(request: QueryRequest):
    """
    Main endpoint: Process user code query with agent orchestration
    """
    start_time = time.time()
    
    try:
        logger.info(f"Processing query: {request.query[:50]}...")
        
        # Process with orchestrator
        result = orchestrator.process_query(request)
        
        processing_time = (time.time() - start_time) * 1000
        
        return QueryResponse(
            success=True,
            data=result,
            agents_involved=["Orchestrator", "Frontend Dev", "Backend Dev", "Testing", "Documentation"],
            processing_time_ms=processing_time,
            timestamp=datetime.utcnow().isoformat()
        )
    
    except ValueError as e:
        logger.warning(f"Validation error: {str(e)}")
        processing_time = (time.time() - start_time) * 1000
        
        return QueryResponse(
            success=False,
            error=str(e),
            agents_involved=[],
            processing_time_ms=processing_time,
            timestamp=datetime.utcnow().isoformat()
        )
    
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}\n{traceback.format_exc()}")
        processing_time = (time.time() - start_time) * 1000
        
        return QueryResponse(
            success=False,
            data=CodeGenerationOutput(
                code="# Error occurred - please try again",
                explanation="An unexpected error occurred while processing your request.",
                language=request.language,
                complexity="error"
            ),
            error="Internal server error",
            processing_time_ms=processing_time,
            timestamp=datetime.utcnow().isoformat()
        )

# ============ Error Handlers ============

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    """Handle validation errors"""
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "error": str(exc),
            "timestamp": datetime.utcnow().isoformat()
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle general exceptions"""
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal server error",
            "timestamp": datetime.utcnow().isoformat()
        }
    )

# ============ Startup/Shutdown Events ============

@app.on_event("startup")
async def startup_event():
    """Log startup"""
    logger.info(f"🚀 AutoCoder Agents API starting...")
    logger.info(f"Environment: {settings.environment}")
    logger.info(f"Primary Model: {settings.primary_model}")

@app.on_event("shutdown")
async def shutdown_event():
    """Log shutdown"""
    logger.info("🛑 AutoCoder Agents API shutting down...")

# ============ Run Application ============

if __name__ == "__main__":
    import uvicorn
    
    logger.info(f"Starting server on {settings.backend_host}:{settings.backend_port}")
    
    uvicorn.run(
        app,
        host=settings.backend_host,
        port=settings.backend_port,
        log_level=settings.log_level.lower()
    )
