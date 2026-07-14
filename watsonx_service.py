import os
from dotenv import load_dotenv
from ibm_watsonx_ai.foundation_models import Model

load_dotenv()

API_KEY = os.getenv("API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
URL = os.getenv("URL")
MODEL_ID = os.getenv("MODEL_ID")


credentials = {
    "url": URL,
    "apikey": API_KEY
}


parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 800,
    "temperature": 0.7
}


model = Model(
    model_id=MODEL_ID,
    params=parameters,
    credentials=credentials,
    project_id=PROJECT_ID
)


def generate_study_plan(prompt):
    response = model.generate_text(prompt=prompt)
    return response