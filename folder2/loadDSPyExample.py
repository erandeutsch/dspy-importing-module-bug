import dspy
from folder1.ExtractInfo import ExtractInfo

lm = dspy.LM('ollama_chat/qwen3:4b', api_base='http://localhost:11434', api_key='')
dspy.configure(lm=lm)


# Running the module directly works
module = dspy.Predict(ExtractInfo)
print("Running the module directly in folder2:")
print(module(document="This document is about the city of Paris."))


# Running the module with load doesn't work in a different directory
# ModuleNotFoundError: No module named 'ExtractInfo'
print("Loading and running the module in folder2:")
loaded_module = dspy.load("testModule")
print(loaded_module(document="This document is about the city of Paris."))