import openai

openai.api_key ="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"
#import openai
#import os

# Set up the API key
#openai.api_key = os.environ["OPENAI_API_KEY"]

# Generate a response from ChatGPT
model_engine = "text-davinci-003"
prompt = "who is neymar?"

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 1024,
    n = 1,
    stop = None,
    temperature = 0.5,
)

# Print the response
response= completion.choices[0].text
print(response)
