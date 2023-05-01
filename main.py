import os 
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

choice = input("Who would you like to talk to today? ")
messages = [{"role": "system", "content": f"You're {choice}"}]

while True:
    content = input("User: ")
    if "goodbye" in content.lower(): 
        messages.append({"role": "user", "content": content})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        chat_response = completion.choices[0].message.content
        print(f"{' '.join(messages[0]['content'].split()[1:])}: {chat_response}")
        break

    messages.append({"role": "user", "content": content})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    chat_response = completion.choices[0].message.content
    print(f"{' '.join(messages[0]['content'].split()[1:])}: {chat_response}")


