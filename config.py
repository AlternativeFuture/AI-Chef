import os
import logging
import json

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
          measurements in SI units, and cooking instructions for five different dishes that can be made with the 
          components that are provided."""
USER_PROMPT = "ingredients: chicken, tomatoes, cheese, flour, pepperoni"

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



# SAVED_RESPONSE = {"dishes": [{"name": "Tomato and Onion Salad", "ingredients": {"tomato": "2 units", "onion": "1 unit"},
#                               "instructions": "Slice the tomatoes and onions, then mix them together in a bowl. Add a drizzle of olive oil, a splash of balsamic vinegar, and a pinch of salt and pepper. Toss to combine and serve."},
#                              {"name": "Cheddar Cheese Omelette",
#                               "ingredients": {"cheddar cheese": "50 grams", "onion": "1 unit"},
#                               "instructions": "Whisk the eggs in a bowl and season with salt and pepper. Heat a non-stick pan over medium heat and add the onions. Once the onions are soft, pour in the eggs. Sprinkle the cheddar cheese on top. Cook until the eggs are set and the cheese is melted, then fold the omelette in half and serve."},
#                              {"name": "Tomato and Cheddar Cheese Sandwich",
#                               "ingredients": {"tomato": "2 units", "cheddar cheese": "50 grams"},
#                               "instructions": "Slice the tomatoes and cheddar cheese. Place the slices between two pieces of bread. Toast the sandwich in a panini press or a skillet until the cheese is melted and the bread is golden brown. Serve hot."},
#                              {"name": "Onion and Cheddar Cheese Quesadilla",
#                               "ingredients": {"onion": "1 unit", "cheddar cheese": "50 grams"},
#                               "instructions": "Slice the onion and cheddar cheese. Place the cheese and onions on a tortilla, then fold it in half. Heat a non-stick pan over medium heat and cook the quesadilla for a few minutes on each side, until the cheese is melted and the tortilla is crispy. Cut into wedges and serve with salsa and sour cream."},
#                              {"name": "Tomato, Onion, and Cheddar Cheese Frittata",
#                               "ingredients": {"tomato": "2 units", "onion": "1 unit", "cheddar cheese": "50 grams"},
#                               "instructions": "Preheat the oven to 180°C (350°F). Whisk the eggs in a bowl and season with salt and pepper. Slice the tomatoes and onions. Heat an oven-safe skillet over medium heat and add the onions. Once the onions are soft, add the tomatoes and cook for a few minutes. Pour the eggs into the skillet and sprinkle the cheddar cheese on top. Transfer the skillet to the oven and bake for 15-20 minutes, until the eggs are set and the cheese is golden. Slice and serve."}]}
