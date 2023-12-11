# from openai import OpenAI
# import time
#
# start = time.time()
#
# client = OpenAI()
#
# system_prompt_json = "You are a helpful assistant designed to output JSON."
# system_prompt_chef = '''You are a helpful assistant designed to give a recipe for 5 dishes
#                         that can be prepared with the provided ingredients'''
# user_prompt = '''cheese, tomatoes, eggs, flour.'''
#
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo-1106",
#     response_format={"type": "json_object"},
#     messages=[
#         {"role": "system", "content": system_prompt_json},
#         {"role": "system", "content": system_prompt_chef},
#         {"role": "user", "content": user_prompt}
#     ],
#     max_tokens=1000,
#     temperature=0.2
# )
# print(response.choices[0].message.content)
#
# print("Token Size:", response.usage)
# print("Response time", time.time() - start)

from openai import OpenAI
import time


def get_openai_response(model, system_prompt_json, system_prompt_chef, user_prompt, max_tokens=None, temperature=None):
    start_time = time.time()

    client = OpenAI()

    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt_json},
            {"role": "system", "content": system_prompt_chef},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature,
        )

    res_time = time.time() - start_time

    return response.choices[0].message.content, response.usage, res_time


system_prompt_json = '''You are a helpful assistant designed to output JSON.'''
# example [{dish_name: {ingredients_measures: (si units), instructions_for_cooking: }}, ]''')
# system_prompt_chef = '''You are a helpful assistant designed to give dish name, measurement of ingredients in SI units
#                   and instruction for cooking for 5 dishes that can be prepared with the provided ingredients.'''
system_prompt_chef = '''You are a useful helper that can supply the name of the meal, 
the ingredient measurements in SI units, and cooking instructions for five different dishes that can be made 
with the components that are provided.'''
user_prompt = '''ingredients: chicken, tomatoes, cheese, flour, pepperoni'''

max_tokens = 1000
temperature = 0.2


response_content, spend_tokens, response_time = get_openai_response("gpt-3.5-turbo-1106",
                                                                    system_prompt_json,
                                                                    system_prompt_chef,
                                                                    user_prompt,
                                                                    max_tokens,
                                                                    temperature)

print("Response Content:", response_content)
print("Token Size:", spend_tokens)
print("Response Time:", response_time)
