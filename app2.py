import chainlit as cl
import openai
import os
import langchain
from langchain import ChatOpenAI

openai.api_key = ""

template = """SQL tables (and columns):
* Customers(customer_id, signup_date)
* Streaming(customer_id, video_id, watch_date, watch_minutes)

A well-written SQL query that {input}:
```"""

settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": ["```"],
}


@cl.on_message
async def main(message: str):
    # Create the prompt object for the Prompt Playground
    prompt = langchain. Prompt(
        provider=langchain.ChatOpenAI.id,
        messages=[
            langchain.PromptMessage(
                role="user",
                template=template,
                formatted=template.format(input=message)
            )
        ],
        settings=settings,
        inputs={"input": message},
    )

    msg = cl.Message(
        content="",
        language="sql",
    )

    async for stream_resp in await openai.ChatCompletion.acreate(
        messages=[m.to_openai() for m in prompt.messages], stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    prompt.completion = msg.content
    msg.prompt = prompt

    # Send and close the message stream
    await msg.send()
