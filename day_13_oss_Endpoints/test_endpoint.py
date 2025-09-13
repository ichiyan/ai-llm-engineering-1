import os
from dotenv import load_dotenv
from together import Together

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get API key from environment
    api_key = os.getenv('TOGETHER_API_KEY')
    
    if not api_key:
        print("Error: TOGETHER_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key:")
        print("TOGETHER_API_KEY=your_actual_api_key_here")
        return
    
    # Initialize client with API key
    client = Together(api_key=api_key)
    
    try:
        response = client.chat.completions.create(
            model="allanctan_e665/openai/gpt-oss-20b-1eb68dc2",
            messages=[
              {
                "role": "user",
                "content": "What are some fun things to do in New York?"
              }
            ]
        )
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error calling Together AI API: {e}")

if __name__ == "__main__":
    main()