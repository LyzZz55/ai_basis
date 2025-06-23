
from dotenv import load_dotenv
import os
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API")

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64

client = genai.Client(api_key=GEMINI_API_KEY)

contents = ('Brand Style: Modern, Simple, Tech Feel, Main Color: #0A7AFF, Auxiliary Color: #FFD60A, Cover Title: 2025 Summer New Product Launch, Category: Technology Products, Subtitle: Smart Technology, Leading the Future, Design Style: Suitable for Social Media Covers')

response = client.models.generate_content(
    model="gemini-2.0-flash-preview-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(
      response_modalities=['TEXT', 'IMAGE']
    )
)

for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO((part.inline_data.data)))
    image.save('gemini-native-image.png')
    image.show()
    