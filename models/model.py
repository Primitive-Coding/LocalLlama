import time

# Langchain imports
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


from models.templates import financial_analyst


chat_template = """

Answer the question below. 

Here is the conversation history: {context}

Question: {question}

Answer: """


import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service


class Model:
    def __init__(self, model_name: str) -> None:
        self.model = OllamaLLM(model=model_name)

    def get_result(self, prompt: str):
        result = self.model.invoke(input=prompt)
        return result

    def get_chain_result(self, user_prompt: str):
        prompt = ChatPromptTemplate.from_template(financial_analyst)
        chain = prompt | self.model
        result = chain.invoke({"report": user_prompt})
        return result

    def handle_chat(self, invoke_instructions: dict):
        prompt = ChatPromptTemplate.from_template(chat_template)
        chain = prompt | self.model
        result = chain.invoke(invoke_instructions)
        return result

    def get_chain_result2(self, invoke_instructions: dict, template: str) -> str:
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | self.model
        result = chain.invoke(invoke_instructions)
        return result

    # def scrape_website(self, url):

    #     # chrome_driver_path = "D:\\ChromeDriver\\chromedriver.exe"
    #     options = webdriver.ChromeOptions()
    #     driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    #     try:
    #         driver.get(url)
    #         html = driver.page_source
    #         print(html)

    #     finally:
    #         driver.quit()
