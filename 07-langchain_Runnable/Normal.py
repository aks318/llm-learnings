import random
from abc import ABC, abstractmethod

class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass

class Naklillm(Runnable):
    def __init__(self):
        print("LLM Created")

    def invoke(self, prompt):
        list = ["One", "Two", "Three"]
        return {'response': random.choice(list)}

    def predict(self, prompt):
        list = ["One", "Two", "Three"]
        return {'response': random.choice(list)}


class NakliPromptTemple(Runnable):
    def __init__(self, template, inputVariable):
        self.template =  template
        self.inputVariable = inputVariable

    def invoke(self, inputDict):
        return self.template.format(**inputDict)

    def format(self, inputDict):
        return self.template.format(**inputDict)
    
class RunnableConnector(Runnable):
    def __init__(self, runnableList):
        self.runnableList = runnableList

    def invoke(self, input_data):
        for runnable in self.runnableList:
            input_data = runnable.invoke(input_data)
        return input_data



# class NakliLLMChain:
#     def __init__(self, llm, prompt):
#         self.llm = llm
#         self.prompt = prompt
#     def run(self, input_dict):
#         final_prompt = self.prompt.format(input_dict)
#         result = self.llm.predict(final_prompt)

#         return result['response']

llm = Naklillm()

template = NakliPromptTemple(
    template="Hi its {Person}",
    inputVariable=["Person"]
)

nakliLLmChain = RunnableConnector([template, llm])

print(nakliLLmChain.invoke({"Person": "Aakash"}))