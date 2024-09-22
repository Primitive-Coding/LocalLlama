from models.gemma2 import Gemma2
from models.llama3 import Llama3
from models.mistral import Mistral


if __name__ == "__main__":

    g = Gemma2()
    l = Llama3()
    m = Mistral()

    prompt = ""

    gr = g.get_result(prompt)
    lr = l.get_result(prompt)
    mr = m.get_result(prompt)

    print(
        f"======================================\n[Gemma2]:\n{gr}\n======================================\n[Llama3]:\n{lr}\n======================================\n[Mistral]:\n{mr}"
    )
