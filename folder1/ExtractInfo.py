import dspy

class ExtractInfo(dspy.Signature):
    """Extract structured information from text."""

    document: str = dspy.InputField()
    cityName: str = dspy.OutputField(desc="The name of the city referred to in the text.")