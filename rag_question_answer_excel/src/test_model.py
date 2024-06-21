import giskard
import pandas as pd
from Rag import *

rag = Rag()

def model_predict(df: pd.DataFrame):
    """Wrap the LLM call in a simple Python function.
    
    The function takes a pandas.DataFrame containing the input variables needed
    by your model, and must return a list of the outputs (one for each row).
    """
    responses = [rag.query(question, history = [message_init]) for question in df["question"]]
    return responses

#Don't forget to fill the 'name' and 'description' : they are used by Giskard
# to generate domain specific tests.
giskard_model = giskard.Model(
    model=model_predict,
    model_type="text_generation",
    name="Flowers Questions Answering",
    description="This model answers any question about flowers on a given corpus",
    feature_names=["question"],
)

examples = [
    "Example of a japan flower ?",
    "Flower with a greek name ?"
]
giskard_dataset = giskard.Dataset(pd.DataFrame({"question": examples}), target=None)

print(giskard_model.predict(giskard_dataset).prediction)
