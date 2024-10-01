import time

try:
    from models.gemma2 import Gemma2
    from models.llama3 import Llama3
    from models.mistral import Mistral
except ModuleNotFoundError:
    from LocalLlama.models.gemma2 import Gemma2
    from LocalLlama.models.llama3 import Llama3
    from LocalLlama.models.mistral import Mistral


def test_model_variation(prompt: str):
    start = time.time()
    g = Gemma2()
    l = Llama3(version="3.1", params="latest")
    m = Mistral()

    gr = g.get_result(prompt)
    lr = l.get_result(prompt)
    mr = m.get_result(prompt)
    end = time.time()
    elapse = end - start
    print(
        f"======================================\n[Gemma2]:\n{gr}\n======================================\n[Llama3]:\n{lr}\n======================================\n[Mistral]:\n{mr}\n\n[Total Elapse]: {elapse}"
    )


def test_model_versions(prompt):
    start = time.time()
    l0 = Llama3(version="3", params="latest")
    l1 = Llama3(version="3.1", params="latest")
    l2 = Llama3(version="3.2", params="latest")

    r0 = l0.get_result(prompt)
    r1 = l1.get_result(prompt)
    r2 = l2.get_result(prompt)
    end = time.time()
    elapse = end - start
    elapse = "{:,.2f}".format(elapse)
    print(
        f"======================================\n[{l0.model_name}]:\n{r0}\n======================================\n[{l1.model_name}]:\n{r1}\n======================================\n[{l2.model_name}]:\n{r2}\n\n[Total Elapse]: {elapse} seconds"
    )


if __name__ == "__main__":

    prompt = "Sally (a girl) has 3 brothers. Each brother has 2 sisters. How many sisters does Sally have? Answer in one sentence."

    # test_model_variation(prompt)
    test_model_versions(prompt)
