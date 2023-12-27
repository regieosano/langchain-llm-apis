from ....openai.prompts.system import system
from ....openai.prompts.human import human
from langchain.prompts import ChatPromptTemplate
from ....pydantic.main import pydantic_parsers
from langchain.pydantic_v1 import BaseModel, Field
from ....templates.main import general_knowledge_system_template
from ....openai.openai_model import model


class ChatQuery(BaseModel):
    answer: str = Field(description="Answer to the user question")


class ChatService:
    def get_ai_generated_answer(self, question: str):
        question_template_text = "{request}/n{format_instructions}"

        pydantic_parser = pydantic_parsers.get_pydantic_output_parser(
            pydantic_object=ChatQuery
        )

        human_prompt = human.get_human_prompt(question_template_text)

        system_prompt = system.get_system_prompt(general_knowledge_system_template)

        chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

        model_request = chat_prompt.format_prompt(
            request=question,
            format_instructions=pydantic_parser.get_format_instructions(),
        ).to_messages()

        data = model(model_request, temperature=0)

        return data
