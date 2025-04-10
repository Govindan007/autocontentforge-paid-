from agents.writer_agent import run_writer_agent
from agents.editor_agent import run_editor_agent
from agents.designer_agent import run_designer_agent
from agents.narrator_agent import run_narrator_agent

def main():
    topic = input("Enter blog topic: ")
    draft = run_writer_agent(topic)
    print("\nDraft:\n", draft)
    edited = run_editor_agent(draft)
    print("\nEdited:\n", edited)
    image_url = run_designer_agent(topic)
    print("\nImage URL:\n", image_url)
    audio_path = run_narrator_agent(edited)
    print("\nAudio File Saved As:\n", audio_path)

if __name__ == '__main__':
    main()
