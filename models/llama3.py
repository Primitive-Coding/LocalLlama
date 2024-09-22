# Logic to fix imports depending on where program is being run from.
try:
    from model import Model
except ModuleNotFoundError:
    from models.model import Model


class Llama3(Model):
    def __init__(self) -> None:
        model_name = "llama3"
        super().__init__(model_name)


if __name__ == "__main__":

    l = Llama3()

    r = l.get_result("This is a test")
    print(f"R: {r}")
