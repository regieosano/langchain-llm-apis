from ....openai.openai_model import model
from langchain.prompts import ChatPromptTemplate
from ....openai.prompts.system import system
from ....openai.prompts.human import human
from ....pydantic.main import pydantic_parsers
from ....templates.main import joke_template
from langchain.pydantic_v1 import BaseModel, Field


class JokeElicited(BaseModel):
    joke: str = Field(description="The elicited joke!")


class JokeService:
    def get_ai_generated_joke(self, subject):
        template_text = "{request}/n{format_instructions}"

        pydantic_parser = pydantic_parsers.get_pydantic_output_parser(
            pydantic_object=JokeElicited
        )

        human_prompt = human.get_human_prompt(template_text)

        system_prompt = system.get_system_prompt(joke_template)

        chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

        model_request = chat_prompt.format_prompt(
            request=subject,
            format_instructions=pydantic_parser.get_format_instructions(),
        ).to_messages()

        result = model(model_request, temperature=0)

        return result
