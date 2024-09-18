# from models.llama3 import Llama3
import time

from models.profiles.financial_analyst import FinancialAnalyst

from test import prompt

test_prompt = """NVIDIA (NASDAQ: NVDA) today reported revenue for the second quarter ended July 28, 2024, of $30.0 billion, up 15% from the previous quarter and up 122% from a year ago.

For the quarter, GAAP earnings per diluted share was $0.67, up 12% from the previous quarter and up 168% from a year ago. Non-GAAP earnings per diluted share was $0.68, up 11% from the previous quarter and up 152% from a year ago.

“Hopper demand remains strong, and the anticipation for Blackwell is incredible,” said Jensen Huang, founder and CEO of NVIDIA. “NVIDIA achieved record revenues as global data centers are in full throttle to modernize the entire computing stack with accelerated computing and generative AI.”

“Blackwell samples are shipping to our partners and customers. Spectrum-X Ethernet for AI and NVIDIA AI Enterprise software are two new product categories achieving significant scale, demonstrating that NVIDIA is a full-stack and data center-scale platform. Across the entire stack and ecosystem, we are helping frontier model makers to consumer internet services, and now enterprises. Generative AI will revolutionize every industry.”

During the first half of fiscal 2025, NVIDIA returned $15.4 billion to shareholders in the form of shares repurchased and cash dividends. As of the end of the second quarter, the company had $7.5 billion remaining under its share repurchase authorization. On August 26, 2024, the Board of Directors approved an additional $50.0 billion in share repurchase authorization, without expiration.

NVIDIA will pay its next quarterly cash dividend of $0.01 per share on October 3, 2024, to all shareholders of record on September 12, 2024.

On June 7, 2024, NVIDIA completed a ten-for-one forward stock split. All share and per-share amounts presented have been retroactively adjusted to reflect the stock split."""


if __name__ == "__main__":

    start = time.time()
    fa = FinancialAnalyst()
    # de = fa.get_result(prompt)
    url = "https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2025"
    fa.llama3.scrape_website(url)
    # fa.handle_conversation()
    end = time.time()
    elapse = end - start
    elapse = "{:,.2f}".format(elapse)
    # print(f"Result: {de}\n\nElapse: {elapse} seconds")
    # print(f"TAG1")
    # model = Llama3()
    # print(f"TAG2")
    # result = model.get_chain_result(test_prompt)
    # print(f"Result: {result}")
    # print(f"TAG3")
