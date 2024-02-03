import os
import openai
from new import apikey

openai.api_key=apikey
conversation_history=[]
a=True
while a:
    print("Listening you")
    # speaker.speak("Listening you")
    query = input("Enter the query:")
    print(query)

    sites = [
        # ... (rest of your code)
    ]

    b = False
    if query is not None:
        if query=="hi":
            print(hello)
    #     for site in sites:
    #         # ... (rest of your code)
    #
    #     if "play music".lower() in query.lower():
    #         # ... (rest of your code)
    #
    #     elif "Bye-bye".lower() in query.lower():
    #         # ... (rest of your code)
    #
    #     elif "the date".lower() in query.lower():
    #         # ... (rest of your code)
    #
    #     elif "Open chrome".lower() in query.lower():
    #         # ... (rest of your code)

        else:
            if b is False:
                # If the query is not recognized, add a user message with the query to the conversation history
                user_message = {"role": "user", "content": query}
                conversation_history.append(user_message)

                # Call the OpenAI API to generate a completion using the chat-based endpoint
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=conversation_history,
                    max_tokens=100
                )

                # Extract and print the generated text (assistant's response)
                assistant_response = response['choices'][0]['message']['content']
                print(f"Assistant: {assistant_response}")
                # speaker.Speak(f"{assistant_response}")

                # Add assistant's response to the conversation history for the next turn
                assistant_message = {"role": "assistant", "content": assistant_response}
                conversation_history.append(assistant_message)