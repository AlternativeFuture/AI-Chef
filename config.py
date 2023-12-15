import os
import logging


from dotenv import load_dotenv

load_dotenv()

FLASK_HOST = os.environ.get("FLASK_HOST", "127.0.0.1")
FLASK_PORT = os.environ.get("FLASK_PORT", 5000)
DEBUG = True

LOG_LEVEL = logging.ERROR
if os.environ.get("FLASK_ENV") == "development":
    LOG_LEVEL = logging.DEBUG

# chicken, tomatoes, cheese, flour, pepperoni

GPT_3 = "gpt-3.5-turbo-1106"
GPT_4 = "gpt-4-1106-preview"

SYSTEM_PROMPT_JSON = "You are a helpful assistant designed to response JSON object."
SYSTEM_PROMPT_CHEF = """You are a useful helper that can supply the name of the meal, the ingredient 
          measurements in SI units, and cooking instructions for three different dishes that can be made with the 
          components that are provided."""
USER_PROMPT = "ingredients: {}."
# Current data is{}.
GPT_CONFIG = {"gpt_model": GPT_3,
              "api_key": os.environ.get("GPT_API_SECRET_KEY", "dev"),
              "response_format": {"type": "json_object"},
              "max_tokens": 1000,
              "temperature": 0.2,
              "system_prompt_json": SYSTEM_PROMPT_JSON,
              "system_prompt_chef": SYSTEM_PROMPT_CHEF,
              "user_prompt": USER_PROMPT}

# PROMPT = [json.dumps({"role": "system", "content": SYSTEM_PROMPT_JSON}),
#           json.dumps({"role": "system", "content": SYSTEM_PROMPT_CHEF}),
#           json.dumps({"role": "user", "content": USER_PROMPT})]
