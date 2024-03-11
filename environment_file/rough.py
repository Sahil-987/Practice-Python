import os
from dotenv import load_dotenv
load_dotenv()

print(os.environ.get("api_key"))

print(os.getenv("api_key"))




from decouple import config 


print(config("api_key"))