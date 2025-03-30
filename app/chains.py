## import all the neceaasry modules
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
## pip install python-dotenv
## dotenv is used to manage environment variables
## It allows us to store senstive configuration settings like (API KEYS, database URL's and secret tokens) in a .env file
## we can then load these into our python application
## this also allows exposing secrets in version control in GitHub
## also we want to add our .env files to our gitignore file
load_dotenv() # it finds the .env file and will set the environment variables

api_key = os.getenv("GROQ_API_KEY")

if __name__=="__main__":
    print(api_key)



