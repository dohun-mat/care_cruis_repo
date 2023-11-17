from openai import OpenAI
import config
import os

api_key = config.DevelopmentConfig.OPENAI_KEY

os.environ["NEWS_API_KEY"] = api_key
os.environ["OPENAI_API_KEY"] = api_key

news_api_key = os.getenv("NEWS_API_KEY")
api_key = api_key


def generateChatResponse(prompt):
    messages = []
    messages.append({"role": "system", "content": "You are a helpful assistant."})
    messages.append({"role": "user", "content": f'{prompt}'})
    
    
    # question = {}
    # question['role'] = 'user'
    # question['content'] = prompt
    # messages.append(question)
    
    client = OpenAI()
    response = None
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = messages
        )
        answer = response.choices[0].message.content.replace('\n', '<br>')
    except Exception as e:
        print(e)
        answer = 'Oops you best the AI, try a different question, if the problem persists, com back later.'
        
    return answer


    
        # messages=[
      #   {"role": "system", "content": "You are a helpful assistant."},
        # {"role": "user", "content": "Who won the world series in 2020?"},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        # {"role": "user", "content": "Where was it played?"}
      # ]
    

