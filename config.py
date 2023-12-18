import os
import logging

import prompt

from dotenv import load_dotenv

load_dotenv()

FLASK_SECRET_KEY = 'super secret key'
FLASK_HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
FLASK_PORT = os.environ.get('FLASK_PORT', 80)
DEBUG = True

LOG_LEVEL = logging.ERROR
if os.environ.get('FLASK_ENV') == 'development':
    LOG_LEVEL = logging.DEBUG

GPT_DEBUG = False
GPT_3 = 'gpt-3.5-turbo-1106'
GPT_4 = 'gpt-4-1106-preview'

GPT_CONFIG = {'gpt_model': GPT_3,
              'api_key': os.environ.get('GPT_API_SECRET_KEY', 'dev'),
              'response_format': {'type': 'json_object'},
              'max_tokens': 1000,
              'temperature': 0.2,
              'system_prompt_json': prompt.SYSTEM_JSON,
              'system_prompt_chef': prompt.SYSTEM_CHEF,
              'user_prompt': prompt.USER}

if GPT_DEBUG:
    GPT_CONFIG['response_example'] = prompt.RESPONSE_EXAMPLE
