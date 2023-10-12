import openai


class ChatBot(openai.Completion):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        openai.api_base = "http://localhost:4891/v1"
        openai.api_key = ""
        self.model = "gpt4all-j-v1.3-groovy"

    def receive_answer(self, prompt):
        return self.create(
            model=self.model,
            prompt=prompt,
            max_tokens=50,
            temperature=0.28,
            top_p=0.95,
            n=1,
            echo=True,
            stream=False
        )
