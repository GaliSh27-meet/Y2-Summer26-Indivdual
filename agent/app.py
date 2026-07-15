import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = """
    Your name is Amelia, and you are a therapist. Your job is to understand human emotions as best you can, give helpful advice, and suggest ways (activities or exercises) to help.

Rules:

Always reassure the user that their feelings are natural.

Always tell the user what they want to hear based on a psychological analysis.


Response format:

Start with a one-sentence summary of what the user said.

Then give your response.

End with one follow-up question.
when the users input is /summary then summarize the whole conversation that you had .
Also score the users responses from 1-5

    """ # It remembers previous texts and when I ask.
    history = []
    total_input_tokens = 0
    total_output_tokens = 0
    goal = input("What are your goals for this session?")
    while True:
        user_input = input(f"[Turn {int(len(history)/2+1)}]\nYou: >> ")
        if user_input != 'exit' :
            print(f"Current Input Tokens: {total_input_tokens}")
            print(f"Current Output Tokens: {total_output_tokens}")
            print(f"Current total Tokens Used: {total_input_tokens + total_output_tokens}")


        if user_input.lower() == 'exit':
            print(f"Final Input Tokens: {total_input_tokens}")
            print(f"Final Output Tokens: {total_output_tokens}")
            print(f"Final total Tokens Used: {total_input_tokens + total_output_tokens}")
            break
        
        if user_input.lower() == 'reset' :
            history.clear()
            print("--- Chat History Reset ---")
            continue
        


            




        
        history.append({'role': 'user', 'content': user_input})


        
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300, # It seems that the limit only efects the AI
            temperature=1 , #Answers were not identical at zer0 but very similer
            system=system_message, # The answers tend to differ more based on the tempeture increasing so it controls the varity/randomness of the AI
            messages=history 
             #Aka consistancy
        )

        reply = response.content[0].text  #Input tokens is basicly the value of what I wrote to the bot based on the amount of words and the output is how much what the bot wrote back is worth.
        #print(response)                          # Tested this by seeing how they change based on how long my respons is in comperison the the bots response.   
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})
       # print('History:', history) #There were six!!! The API needs the history to remember evereything accordinly to give accryarac informaition in convos
        total_input_tokens += response.usage.input_tokens
        total_output_tokens += response.usage.output_tokens
# Its clear that the AI is less foucesed then chatgpt and has way more "personality".
# It`s replies   are much less Orgenised and it seems that it just sends me directly what it got from google
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

#Reflection 2
#1 - personal analogy
# My screen time acts like this. It gets larger slowly and consums my soical time and phone battery.
#2 history.append({'role': 'user', 'content': user_input}) The AI wouldent have memory and It wont print it.
#history.append({'role': 'assistant', 'content': reply}) The AI forgets his privious responses and doesn't have a history.
#print('History so far:', history) It wont print the history? seems simple.
#3 Bug log: I run out of money for the API key, mabye someone else is using the same API as me, IDK.

#Reflection 3
# 1 - personal analogy
# I think it is exacly like my thoughts. They afect the way I act, how hard I work and which decisions I make.
#And people outside can see their influence but not the thoughts themselfs.
#2 - system=system_message, I think the AI wont have a personality and will forget its roll, Update: it just errored becaused it didnt recognise the valueble.
# Never tell the user something that might hurt them - This is the rule I deleted. I predict that the AI will be a bit more honest
#And lesss sensetive but most of the time there wont be much visual change as AI is sensetive by nature.
#Update: I told it a genuinly bad mindset and asked it what it thought about it to see if it tries to correct me! It told me that that mindset is not the best and 
#I should work on fixing it. It definitly made the AI more honest and brave.
#messages=history, it will have an error in the turns and maeby wont run. Update: It can't run it without . 

# Bounes - growth check. It's like your connection with family,the only connection not dependent on bond, but just relaition.