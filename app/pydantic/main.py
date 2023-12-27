from langchain.output_parsers import PydanticOutputParser

class PyDanticParsers():

	def get_pydantic_output_parser(self, pydantic_object):
		pydantic_parser = PydanticOutputParser(pydantic_object=pydantic_object)

		return pydantic_parser


pydantic_parsers = PyDanticParsers()