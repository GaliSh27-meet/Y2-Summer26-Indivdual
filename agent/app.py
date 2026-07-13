import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = input("How would you like your AI to be?")
    history = []

    while True:
        user_input = input(f"[Turn {int(len(history)/2+1)}]\nYou: >> ")


        if user_input.lower() == 'exit':
            break
        
        if user_input.lower() == 'reset' :
            history.clear()
            print("--- Chat History Reset ---")
            continue

        
        history.append({'role': 'user', 'content': user_input})


        
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            temperature=0.7 ,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})
# Its clear that the AI is less foucesed then chatgpt and has way more "personality".
# It`s replies are much less Orgenised and it seems that it just sends me directly what it got from google
# When faced with Unclear instructions it try's to guess what the user meant and encoureges me to try again.
# Though even that it does less efficiently then Chatgpt and other Ai's.
run_chat()

# Reflection
#1 - personal analogy
#Well, it's kind of like family. A group of people who without your backround and history together you may not even have anything in commen.
# Family is uniqe in that department in the sense that they are the only people in your life that don't nececerly have to connect to you outside of family connections.
# Basiclly they are like forced connections, the same princible works for childhood friends.
# 2. history.append({'role': 'assistant', 'content': reply})the AI wont be able wont be able to remember and the turns wont work.
#Update: Error!
#load_dotenv() it will erroe before start. Update: I was wrong, it only errored after first chat
#temperature=0.7 It will just change the AI's personality a bit but nothing visible. Update: The AI just wasnt affected by my personality instructions.
#3 - Bug log one bug I encountered was with the reset input, it just didnt seem to work, it didnt have an error,
#It just didnt do what I wanted. I thought that it was the placment of the command and that was part off it but the main thing was to put "continue" in the end.