import ollama

response = ollama.generate(model= "llama3.2:1b", prompt= "Hi")

print(response.response)