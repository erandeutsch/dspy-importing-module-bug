import dspy
from ExtractInfo import ExtractInfo

dspy.configure(lm=dspy.LM('ollama_chat/qwen3:4b', api_base='http://localhost:11434', api_key=''))


# Save the imported module to a file
module = dspy.Predict(ExtractInfo)
module.save("testModule", save_program=True)


# Running the module in the same directory works
loaded_module = dspy.load("testModule")
print(loaded_module)
print(loaded_module(document="This document is about the city of Paris."))