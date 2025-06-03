import dspy
import ExtractInfo

dspy.configure(lm=dspy.LM('ollama_chat/qwen3:4b', api_base='http://localhost:11434', api_key=''))


module = dspy.Predict(ExtractInfo.ExtractInfo)
print("Running the module directly in folder1:")
print(module(document="This document is about the city of Paris."))


# Save the imported module to a file
module.save("testModule", save_program=True, modules_to_serialize=[ExtractInfo])


# Running the module in the same directory works
print("Loading and running the module in folder1:")
loaded_module = dspy.load("testModule")
print(loaded_module(document="This document is about the city of Paris."))