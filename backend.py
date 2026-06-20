from langchain_openai import ChatOpenAI

api_key=open("api.txt").read().strip()

model=ChatOpenAI(api_key=api_key,model = "gpt-4o-mini",temperature=0.5)

from langchain_core.prompts import PromptTemplate

prompt_input=PromptTemplate.from_template(" You are an expert business email writer. write a email for {purpose} purpose  to {recipient} in {tone}tone.make it more concise and humenlike")



from langchain_core.output_parsers import StrOutputParser

output_parser=StrOutputParser()


chain = prompt_input | model |output_parser
 
def email_generator (purpose,recipient,tone):
      response= chain.invoke ({
            "purpose": purpose,
            "recipient": recipient,
            "tone": tone
      })
      return response

