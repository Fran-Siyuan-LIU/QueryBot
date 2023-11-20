import os
import openai
import time

class QueryBot:

    def __init__(self, key, engine = "text-davinci-003", max_tokens = 7, temperature = 0, time_limit = 1):
        '''set up OpenAI api key here to initialize a new prompt object'''
        openai.api_key = key
        self.engine = engine
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.time_limit = time_limit



    def prompt(self, str, x):
        '''
        str: string, the designed prompt command you would like to ask

        x: array-like, the variable different from each other in each prompt

        return: list of answer
        '''
        self.str = str

        response = []

        for var in x:
            response.append(self.get_answer(var))

        return response



    def get_answer(self, x):
        ''' get each answer for the required prompt '''

        prompt = self.str.format(x)

        response = openai.Completion.create(
            engine = self.engine,
            prompt = prompt,
            max_tokens = self.max_tokens,
            temperature = self.temperature
        )
    
        time.sleep(self.time_limit)

        return response.choices[0].text.strip()
