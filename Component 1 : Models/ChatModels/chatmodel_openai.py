from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Use Case                                          Recommended Temperature
# Factual Answers(Math, Code, Facts)                        0.0 - 0.3
# Balanced Responses(General Questions)                     0.5 - 0.7
# Creative writing, storytelling, jokes, poems              0.9 - 1.2
# Maximum Randomness(Wild ideas, brainstorming)             1.5+
# Temperature  ∝ randomness

chatmodel = ChatOpenAI(model='gpt-4', temperature = 0.9, max_completion_tokens=15)
result = chatmodel.invoke("Tell me a joke?")
print(result.content)