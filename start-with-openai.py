import openai

# Change YOUR_API_KEY with your actual API key
openai.api_key = "YOUR_API_KEY"

# Request is saved in a variable
response = openai.Completion.create(engine="davinci", prompt="Hello, world!")

#Prints out the Response
print(response.choices[0].text)
