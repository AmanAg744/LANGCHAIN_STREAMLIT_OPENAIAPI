from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import chainlit as cl

template = """Question!!! {question} Anwser"""

@cl.LangchainCallbackHandler()
def factory():
    prompt = PromptTemplate(template = template, input_variables=["question"])  
    llm_chain = LLMChain(prompt=prompt,llm=ChatOpenAI(temperature=0, streaming = True))
    return llm_chain
