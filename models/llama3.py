from models.model import Model


class Llama3(Model):
    def __init__(self) -> None:
        model_name = "llama3"
        super().__init__(model_name)
