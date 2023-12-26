from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.prompts import ( SystemMessagePromptTemplate, HumanMessagePromptTemplate)
from langchain.output_parsers import ResponseSchema, PydanticOutputParser
from langchain.pydantic_v1 import BaseModel, Field 
from ....templates.main import general_knowledge_system_template
from ....openai.openai_model import model

class ChatQuery(BaseModel):
    answer: str = Field(description="Answer to the user question")
   

class ChatService():

	def get_ai_generated_answer(self, question: str):
			question_template_text = "{request}/n{format_instructions}"

			pydantic_parser = PydanticOutputParser(pydantic_object=ChatQuery)

			human_prompt = HumanMessagePromptTemplate.from_template(question_template_text)

			system_prompt = SystemMessagePromptTemplate.from_template(general_knowledge_system_template)

			chat_prompt = ChatPromptTemplate.from_messages(
				[human_prompt, system_prompt]
			)

			model_request = chat_prompt.format_prompt(
				request=question,
				format_instructions=pydantic_parser.get_format_instructions()
			).to_messages()

			data = model(model_request, temperature=0)

			return data

			
	



