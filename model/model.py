import dataclasses
from typing import List


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

    def answer(self, request: Request):
        return self.Response('answer', ['https://www.wikipedia.org/'])
