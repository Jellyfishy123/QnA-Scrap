import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Define function to generate a response from OpenAI
def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content

# Main program loop
while True:
    user_input = input("User: ")

    if user_input.lower() == 'exit':
        break

    # Generate a response from OpenAI
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]
    response = generate_response(messages)

    print("ChatGPT:", response)


