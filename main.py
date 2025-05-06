import os
from agents import Agent, Runner , OpenAIChatCompletionsModel , AsyncOpenAI,set_tracing_disabled
from agents import set_default_openai_client , set_default_openai_api
from dotenv import  load_dotenv,find_dotenv
_:bool = load_dotenv(find_dotenv())
set_tracing_disabled(True)
gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=gemini_api_key,
)

set_default_openai_api("chat_completions")
set_default_openai_client(external_client)

# gemini_model = OpenAIChatCompletionsModel(
#     model = "gemini-2.0-flash",
#     openai_client= external_client
# )
model = "gemini-2.0-flash"
import asyncio
async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in english.", model= model
    )

    result =  await Runner.run ( agent , "what is agentic ai?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

















