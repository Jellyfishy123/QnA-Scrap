from datasets import load_dataset

# Load the CommonsenseQA dataset
dataset = load_dataset("commonsense_qa")

# Access the train, validation, and test splits
train_data = dataset["train"] #9741
val_data = dataset["validation"] #1221
test_data = dataset["test"] #1140

# Example usage: Print the first question and its answer from the training set
with open("questions.txt", "w") as file:
    for i in range(len(train_data)):
        question = train_data[i]["question"]
        file.write(f"Question {i+1}: {question}\n")

print("Output saved to 'questions.txt' file.")

