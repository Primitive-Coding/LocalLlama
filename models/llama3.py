# Logic to fix imports depending on where program is being run from.
try:
    from model import Model
except ModuleNotFoundError:
    try:
        from models.model import Model
    except ModuleNotFoundError:
        from LocalLlama.models.model import Model


class Llama3(Model):
    def __init__(self, version: str = "3.2", params: str = "latest") -> None:
        if version == "":
            # Default to basic 3.0 llama version.
            model_name = f"llama3:{params}"
        else:
            model_name = f"llama{version}:{params}"

        super().__init__(model_name)


if __name__ == "__main__":

    l = Llama3()

    r = l.get_result("This is a test")
    print(f"R: {r}")
