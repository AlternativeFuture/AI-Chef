import os
import logging

from dotenv import load_dotenv

load_dotenv()

FLASK_HOST = os.environ.get('FLASK_HOST', '127.0.0.1')
FLASK_PORT = os.environ.get('FLASK_PORT', 5000)
DEBUG = True

LOG_LEVEL = logging.ERROR
if os.environ.get('FLASK_ENV') == 'development':
    LOG_LEVEL = logging.DEBUG

# example [{dish_name: {ingredients_measures: (si units), instructions_for_cooking: }}, ]''')
# system_prompt_chef = '''You are a helpful assistant designed to give dish name, measurement of ingredients in SI units
#                   and instruction for cooking for 5 dishes that can be prepared with the provided ingredients.'''
# chicken, tomatoes, cheese, flour, pepperoni

SYSTEM_PROMPT_JSON = 'You are a helpful assistant designed to output JSON.'
SYSTEM_PROMPT_CHEF = '''You are a useful helper that can supply the name of the meal, the ingredient 
          measurements in SI units, and cooking instructions for five different dishes that can be made with the 
          components that are provided.'''
USER_PROMPT = 'ingredients: {}'

GPT_CONFIG = {'gpt_model': 'gpt-3.5-turbo-1106',
              'api_key': os.environ.get('GPT_API_SECRET_KEY', 'dev'),
              'max_tokens': 1000,
              'temperature': 0.2,
              'system_prompt_json': SYSTEM_PROMPT_JSON,
              'system_prompt_chef': SYSTEM_PROMPT_CHEF,
              'user_prompt': USER_PROMPT}
