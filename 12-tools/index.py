from typing import Type

from langchain_community.tools import DuckDuckGoSearchRun, ShellTool, tool, StructuredTool, BaseTool
from pydantic import BaseModel, Field

searchTool = DuckDuckGoSearchRun()
shellTool = ShellTool()

# result  = searchTool.invoke("Virat Kohli")

# # print(result)

# result2 = shellTool.invoke({"commands": "whoami"})


# custom tool
# 1
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a": "3", "b": "2"})

# print(result)

# 2

class MultiplyInput(BaseModel):
    a: int = Field(required = True, description="The first number")
    b: int = Field(required = True, description="The second number")


def multiply(a: int, b: int) ->int:
    return a*b

multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({"a": 3, "b": 5})

# print(result)

# 3

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiple two numbers"
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a*b

multiply_tool = MultiplyTool()

res = multiply_tool.invoke({"a" : 5, "b" : 5})

print(res)