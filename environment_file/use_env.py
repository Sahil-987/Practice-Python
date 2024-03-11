
### Method-1
import os 
from dotenv import load_dotenv
load_dotenv() # Load variables from .env file
print(os.environ.get("api_key"))




### Method-2
import os 
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("api_key"))