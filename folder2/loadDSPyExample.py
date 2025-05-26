import dspy
from folder1.ExtractInfo import ExtractInfo

lm = dspy.LM('ollama_chat/qwen3:4b', api_base='http://localhost:11434', api_key='')
dspy.configure(lm=lm)


# Running the module directly works
module = dspy.Predict(ExtractInfo)
print(module(document="This document is about the city of Paris."))


# Running the module with load doesn't work in a different directory
# ModuleNotFoundError: No module named 'ExtractInfo'
loaded_module = dspy.load("testModule")
print(loaded_module)
print(loaded_module(document="This document is about the city of Paris."))