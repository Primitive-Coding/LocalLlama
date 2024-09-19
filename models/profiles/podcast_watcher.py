from LocalLlama.models.llama3 import Llama3


podcast_watcher_template = """

You are given transcripts for a video. You will be asked specific questions about topics of the video.

Here is the transcripts: {transcript}

Answer:  

"""


class PodcastWatcher:
    def __init__(self) -> None:
        self.llama3 = Llama3()

    def get_result(self, prompt: str):
        invoke_intructions = {"transcript": prompt}
        result = self.llama3.get_chain_result(
            invoke_instructions=invoke_intructions, template=podcast_watcher_template
        )
        return result

    def summarize(self, prompt: str):
        summarize_template = """
        Summarize the transcripts that are given to you. List bullet points of notable topics discussed. 
        
        Here is the transcripts: {transcript}
        
        Answer: 
        """
        invoke_intructions = {"transcript": prompt}
        result = self.llama3.get_chain_result(
            invoke_instructions=invoke_intructions, template=summarize_template
        )
        return result

    def handle_conversation(self, transcript):
        # print(f"Transcript: {transcript.values}")
        # exit()
        context = ""

        print("\n\n-- Starting Chat --\n\n Type 'exit' at any time to quit.\n\n")
        index = 0
        while True:

            if index == 0:
                invoke_instructions = {
                    "context": context,
                    "question": transcript,
                }
                result = self.llama3.handle_chat(
                    invoke_instructions=invoke_instructions
                )

                context += f"User: I'm providing you this transcript. You'll will be asked questions about it's content: {transcript}\nAI: "
                user_input = ""
            else:
                user_input = input("\n-----------------------------------\n[User]: ")
                if user_input.lower() == "exit":
                    break
                invoke_instructions = {"context": context, "question": user_input}
                result = self.llama3.handle_chat(
                    invoke_instructions=invoke_instructions
                )
                print(f"\n[Podcast Watcher Bot]: {result}")
                context += f"\nUser: {user_input}\nAI: {result}"
            index += 1
