import openai
import os
from time import sleep

def get_key(): 
    return open("key.txt", "r").read().strip("\n")
openai.api_key = get_key()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0 # Degree of randomness
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    # Read questions from questions.txt file
    with open("questions.txt", "r") as file:
        questions = file.read().splitlines()
    
    # Create a list to store question-paraphrase pairs
    paraphrases = []

# Generate paraphrases for each question
    for i, question in enumerate(questions, start=1):
        prompt = f"""
        Please give me 5 paraphrases of the sentence below. The generated sentences must be as questions:

        `{question}`
        """
        response = get_completion(prompt.replace("{inp}", question))
        
        sleep(21)
        
        paraphrase_pair = {
            "Question": question,
            "Paraphrase": response
        }
        paraphrases.append(paraphrase_pair)
        

        # Save all paraphrases to a single text file
        with open("paraphrases.txt", "w") as output_file:
            for paraphrase_pair in paraphrases:
                output_file.write(f"{paraphrase_pair['Question']}\n")
                output_file.write(f"{paraphrase_pair['Paraphrase']}\n")

