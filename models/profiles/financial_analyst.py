from models.llama3 import Llama3


financial_analyst_template = """

You are a financial analyst reviewing earnings reports. 
I need you to tell me if this is a good or bad report and why. Give an answer in short and concise bullet points 


Here is the report in question: {report}

Answer: 
"""


class FinancialAnalyst:
    def __init__(self) -> None:

        self.llama3 = Llama3()

    def get_result(self, prompt: str):
        invoke_intructions = {"report": prompt}
        result = self.llama3.get_chain_result2(
            invoke_instructions=invoke_intructions, template=financial_analyst_template
        )
        return result

    def handle_conversation(self):

        context = ""
        print("\n\n-- Starting Chat --\n\n Type 'exit' at any time to quit.\n\n")
        while True:
            user_input = input("\n[User]: ")
            if user_input.lower() == "exit":
                break
            invoke_instructions = {"context": context, "question": user_input}
            result = self.llama3.handle_chat(invoke_instructions=invoke_instructions)
            print(f"\n[Financial Analyst Bot]: {result}")

            context += f"\nUser: {user_input}\nAI: {result}"
