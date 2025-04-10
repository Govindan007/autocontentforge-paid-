from langchain.chat_models import ChatOpenAI

def run_editor_agent(draft):
    prompt = f"Improve the grammar, style, and tone of this article:\n\n{draft}"
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.5)
    return llm.predict(prompt)
