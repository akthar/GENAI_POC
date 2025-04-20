from google import genai

prompt = input("Enter your prompt:")
apikey = input("Enter your API Key:")
client = genai.Client(api_key=apikey)
print("connecting to AI Model to generate the response content...............")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt
)

print(response)
print(response.text)