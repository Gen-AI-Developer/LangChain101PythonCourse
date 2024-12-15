import os
from langchain_community.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, api_key):
    llm = OpenAI(temperature=0.7, openai_api_key=api_key)  # Updated import
    prompt = f"Please suggest five cool names for a pet {animal_type}."
    name = llm.invoke(prompt)  # Use invoke instead of calling directly
    return name

if __name__ == "__main__":
    print("Welcome to the pet name generator!")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OpenAI API key not found. Please set it in the .env file.")
    else:
        print(generate_pet_name("cat", api_key))
