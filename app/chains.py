## import all the neceaasry modules

import httpx
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


class Chain:
    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable not set")

        http_cleint = httpx.Client(verify = False)
        http_async_client = httpx.AsyncClient(verify = False)

        self.llm = ChatGroq(
            model = "llama-3.3-70b-versatile",
            temperature = 0,
            groq_api_key = api_key,
            http_client = http_cleint,
            http_async_client = http_async_client
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scrapped text is form the career's page of a website.
            Your job is to extract the job posting and return them in JSON Format containing
            following keys: 'role', 'experience', 'skills' and 'description'
            The JSON must start with `{{` and end with `}}` with no extra text, quotes, or markdown formatting.
            ### STRICTLY VALID JSON OUTPUT(NO PREAMBLE):
            """
            )

        ## using a pipe operation to form a chain - passing the prompt to the llm
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input = {"page_data":cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION
            {job_description}

            ### INSTRUCTION
            You are Mr.James a business development executive at NewTech. NewTech is an AI & Software 
            consulting company dedicated to facilitating the seamless integration of business process thriugh automated tools.
            Over our experience , we have empowered neumerous enterprices with tailored solutions, fostering scalability,
            process optimization, cost reduction, and heightened overall efficiency.
            Your job is t write a cold email to a client the job mentioned above describing the capability of
            NewTech in fullfilling thier needs.
            Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
            Remember you are Mr.James , BDE at NewTech.
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE)

            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description" :str(job), "link_list" : links})
        return res.content if hasattr(res, 'content') else res

