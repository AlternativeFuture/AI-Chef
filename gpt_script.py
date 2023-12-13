from openai import OpenAI
import config
from decorators import timeit


@timeit
def gpt_response(model: str, prompt: dict, max_tokens: int, temperature: float, key: str) -> tuple:
    """
        Get a response from the OpenAI GPT model based on the given parameters.

        Args:
            model (str): The name of the OpenAI GPT model to use.
            prompt (dict): A dictionary containing system information and user prompt.
            max_tokens (int): The maximum number of tokens to generate in the response.
            temperature (float): Controls the randomness of the generated response.
            key (str): The API key for accessing the OpenAI GPT service.

        Returns:
            tuple: A tuple containing the generated response content and usage information.
                - response_content (str): The content of the generated response.
                - usage (dict): Information about API usage from the response.
        """
    try:
        client = OpenAI(api_key=key)

        response = client.chat.completions.create(
            model=model,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": prompt['system_json']},
                {"role": "system", "content": prompt['system_chef']},
                {"role": "user", "content": prompt['user']}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        return response.choices[0].message.content, response.usage
    except Exception as e:
        # app.logger.info(e)
        return None, None


res_content, spend_tokens = gpt_response(config.GPT_MODEL, config.PROMPT, config.MAX_TOKENS, config.TEMPERATURE, config.API_KEY)

print("Response Content:", res_content)
print("Token Size:", spend_tokens)
# print("Response Time:", response_time)
