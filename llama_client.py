# llama_client.py
from groq import Groq
from config import api_key

# Initialize client with the API key
client = Groq(api_key=api_key)

def get_sector_weights(prompt):
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    
    # Print the completion object to understand its structure
    print(completion)
    
    # Assuming the response format can vary, try accessing the content directly
    # Replace the following line based on actual structure after printing completion
    return completion.choices[0].message.content if hasattr(completion.choices[0].message, 'content') else completion.choices[0].message
