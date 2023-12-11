import g4f

g4f.debug.logging = True  # Enable logging
g4f.check_version = False  # Disable automatic version checking
# print(g4f.version)  # Check version
# print(g4f.Provider.Ails.params)  # Supported args

# Automatic selection of provider #Imagine you are one of the best chefs in the world.
prompt = '''Give me a recipe for 5 dishes that can be prepared
 with the following ingredients: cheese, tomatoes, eggs, flour. Respond in json format.'''

# Streamed completion
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "assistant", "content": prompt}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')


# response = g4f.ChatCompletion.create(
#     model=g4f.models.gpt_4,
#     messages=[{"role": "user", "content": "ապե Հայ ես՞"}],
# )  # Alternative model setting

# print()
# # print(dict(response))
# print(type(response))
