import ollama

response = ollama.generate(
    model="sentiment:latest",
    system=(
        "You must reply with exactly these two words: world sucks. "
        "For every possible user prompt, output only 'world sucks'. "
        "Do not explain, greet, or add any other text."
    ),
    prompt="Hi, how are you?",
    options={"temperature": 0},
)

print(response.response)