import dataclasses
import os
from typing import List, Optional
import requests

API_URL = os.getenv('API_URL')


class Model:
    def __init__(self):
        pass

    @dataclasses.dataclass
    class Request:
        prompt: str

    @dataclasses.dataclass
    class Response:
        answer: str
        sources: List[str]
        error: Optional[str]

    async def scrape(self, prompt: str) -> str:
        url = f'{API_URL}/scrape'
        request_body = {'prompt': prompt}
        resp = requests.post(url, json=request_body, timeout=30)
        print('scraping: ', request_body)
        return resp.json()['scraped_info']

    async def summarize(self, text: str) -> str:
        url = f'{API_URL}/summarize'
        request_body = {'prompt': text}
        print(request_body)
        resp = requests.post(url, json=request_body, timeout=30)
        return resp.json()['generated_text']

    async def answer(self, request: Request):
        if request.prompt == '':
            return self.Response('', [], None)
        try:
            text = await self.scrape(request.prompt)
            print('text: ', text)
            if text == '':
                return self.answer(request)

            answer = await self.summarize(text)
            return self.Response(answer, [], None)
        except Exception as e:
            return self.Response('', [], "Some error occurred on our journey to sustainable future")
