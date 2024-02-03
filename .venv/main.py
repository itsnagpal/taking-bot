import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
import datetime
from new import apikey

openai.api_key=apikey

speaker = win32com.client.Dispatch("SAPI.SpVoice")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pa/use_threshold = 0.6
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            return query
        except Exception as e:
            error1="OOPS!! Some Eror Occured"
            speaker.Speak(error1)
conversation_history=[]
a=True
speaker.Speak("I am Ishpreet's Chat bot")
while a:
    print("Listening you")
    speaker.speak("Listening you")
    query = takeCommand()
    print(query)

    sites = [
        ["Youtube", "https://www.youtube.com"],
        ["Google", "https://www.google.com"],
        ["GitHub", "https://github.com"],
        ["LinkedIn", "https://www.linkedin.com"],
        ["Twitter", "https://twitter.com"],
        ["Stack Overflow", "https://stackoverflow.com"],
        ["Medium", "https://medium.com"],
        ["Wikipedia", "https://www.wikipedia.org"],
        ["Reddit", "https://www.reddit.com"],
        ["Amazon", "https://www.amazon.in"],
        ["LeetCode", "https://leetcode.com"],
        ["Flipkart", "https://www.flipkart.com"],
        ["WhatsApp", "https://web.whatsapp.com"],
        ["Telegram", "https://web.telegram.org"]
    ]

    b = False
    if query is not None:
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower() or f"Open my {site[0]}".lower() in query.lower():
                speaker.speak(f"Opening {site[0]}")
                webbrowser.open(site[1])
                b = True


        if "play music".lower() in query.lower():
            music_path = r"\Users\Ishpreet Singh\Downloads\Behja Behja - Dilpreet Dhillon.mp3"
            #os.system(f"open {music_path}")
            speaker.Speak("Playing music")
            os.startfile(music_path)
            

        elif "Bye-bye".lower() in query.lower():
            speaker.Speak("Goodbye Dear")
            a = False
            break

        elif "the date".lower() in query.lower():
            hour=datetime.datetime.now().strftime("%H")
            minute=datetime.datetime.now().strftime("%M")
            speaker.Speak(f"{hour} hours and {minute} minutes")

        elif "Open chrome".lower() in query.lower():
            chrome_path=r"\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
            #os.startfile(chrome_path)
            os.system(f'start "" "{chrome_path}')
        else:
            if b is False:
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
                speaker.Speak(f"{assistant_response}")
                # Add assistant's response to the conversation history for the next turn
                assistant_message = {"role": "assistant", "content": assistant_response}
                conversation_history.append(assistant_message)