import ollama

inventory_db = {
        "laptop": {"stock": 5, "base_price": 1200},
        "monitor": {"stock": 0, "base_price": 300},
        "keyboard": {"stock": 25, "base_price": 80}
    }


def check_inventory(product_name):
    product_name = product_name.lower()

    if product_name in inventory_db:
        return inventory_db[product_name]

    return {"stock": 5, "base_price": None}


def calculate_loyalty_discount(base_price, years_as_customer):
    discount = min(int(years_as_customer) * 0.05, 0.30)  # max 30%
    final_price = int(base_price) * (1 - discount)
    return round(final_price, 2)

available_functions = {
    'check_inventory': check_inventory,
    'calculate_loyalty_discount': calculate_loyalty_discount,
}

# defining tool

#DEFINING SCHEMA
tools = [
    {
        "type": "function",
        "function": {
            "name": "check_inventory",
            "description": "Get stock and price for a product",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {"type": "string"}
                },
                "required": ["product_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_loyalty_discount",
            "description": "Calculate final price based on loyalty years",
            "parameters": {
                "type": "object",
                "properties": {
                    "base_price": {"type": "number"},
                    "years_as_customer": {"type": "integer"}
                },
                "required": ["base_price", "years_as_customer"]
            }
        }
    }
]

message = [
            {"role": "user", "content": "I am a customer for 5 years. What will be the final price of a laptop?"}
        ]

response = ollama.chat(
    model= "llama3.2:1b",
    messages = message,
    tools= tools
)

tool_calls = response.message.tool_calls
if(tool_calls):
    for tool_call in tool_calls:
        tool_name = tool_call['function']['name']
        tool_args = tool_call['function']['arguments']

        function_to_call = available_functions[tool_name]

        print("function_to_call", function_to_call, tool_args)

        result = function_to_call(**tool_args)

        message.append(response.message)
        message.append({
            "role" : "tool",
            'content': str(result)
        })


final_response = ollama.chat(
    model='llama3.2:1b',
    messages=message
)

print(final_response['message']['content'])