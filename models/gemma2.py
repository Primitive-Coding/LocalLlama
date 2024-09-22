# Logic to fix imports depending on where program is being run from.
try:
    from model import Model
except ModuleNotFoundError:
    from models.model import Model


class Gemma2(Model):
    def __init__(self) -> None:
        model_name = "gemma2"
        super().__init__(model_name)


if __name__ == "__main__":

    g = Gemma2()

    r = g.get_result("This is a test")
    print(f"R: {r}")
