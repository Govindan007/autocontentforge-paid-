from langchain.chat_models import ChatOpenAI

def run_writer_agent(topic):
    prompt = f"Write a blog post of around 300 words on the topic: {topic}"
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    return llm.predict(prompt)
