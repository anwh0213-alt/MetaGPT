"""
This script demonstrates how to use the SearchEnhancedQA action to answer questions
by leveraging web search results. It showcases a simple example of querying about
the current weather in Beijing.

The SearchEnhancedQA action combines web search capabilities with natural language
processing to provide informative answers to user queries.
"""

import asyncio

from metagpt.actions.search_enhanced_qa import SearchEnhancedQA
import os
os.environ['HTTP_PROXY'] = 'http://172.23.80.1:7890'
os.environ['HTTPS_PROXY'] = 'http://172.23.80.1:7890'


async def main():
    """Runs a sample query through SearchEnhancedQA and prints the result."""

    action = SearchEnhancedQA()

    query = "What is the weather like in Beijing today?"
    answer = await action.run(query)

    print(f"The answer to '{query}' is:\n\n{answer}")


async def test_ddg():
    import requests
    try:
        response = requests.get("https://duckduckgo.com", timeout=10)
        print(f"连接成功: {response.status_code}")
    except Exception as e:
        print(f"连接失败: {e}")



if __name__ == "__main__":
    asyncio.run(test_ddg())
    asyncio.run(main())
    
