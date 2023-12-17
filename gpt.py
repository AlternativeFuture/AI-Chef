from openai import OpenAI

import json

import config
from decorator import timeit


@timeit
def gpt_response(gpt_config: dict, ingredients: str, debug: bool) -> tuple:
    if debug:
        return gpt_config['response_example'], ''  # :TODO implement debug mode
    try:
        client = OpenAI(api_key=gpt_config['api_key'])

        response = client.chat.completions.create(
            model=gpt_config['gpt_model'],
            response_format=gpt_config['response_format'],
            messages=[
                {'role': 'system', 'content': json.dumps([gpt_config['system_prompt_json'],
                                                          gpt_config['system_prompt_chef']])},
                {'role': 'user', 'content': json.dumps(gpt_config['user_prompt'].format(ingredients))}
            ],
            max_tokens=gpt_config['max_tokens'],
            temperature=gpt_config['temperature'],
        )

        return response.choices[0].message.content, response.usage
    except Exception as e:
        print(e)
        # app.logger.info(e)
        return None, None


if __name__ == '__main__':
    res_content, spend_tokens = gpt_response(config.GPT_CONFIG, 'cheese, bacon')
    print(type(res_content))
    print('Response Content:', res_content)
    print('Token Size:', spend_tokens)
