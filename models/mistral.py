# Logic to fix imports depending on where program is being run from.
try:
    from model import Model
except ModuleNotFoundError:
    from models.model import Model


class Mistral(Model):
    def __init__(self) -> None:
        model_name = "mistral"
        super().__init__(model_name)


if __name__ == "__main__":

    m = Mistral()

    r = m.get_result("This is a test")
    print(f"R: {r}")
