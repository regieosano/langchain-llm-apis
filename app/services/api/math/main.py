from ....openai.openai_model import model
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.pydantic_v1 import BaseModel, Field


class ChatQuery(BaseModel):
	answer: str = Field(description="Answer to the user question")


class MathService:
	def get_ai_agent_answer(self, question: str):
		tools = load_tools(["llm-math"], llm=model)
		
		agent = initialize_agent(
			tools, model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

		result = agent.run(question)

		return result
