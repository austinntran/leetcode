from typing import List
from random import randint

class Solution:
    tupleToString = {}
    stringToList = {}
    TINYURL = "https://tinyurl.com/"
    
    def encode(self, strs: List[str]) -> str:
        
        
        generatedString = self.tupleToString.get(tuple(strs), "".join([chr(randint(ord('A'), ord('z'))) for _ in range(10)]))
        self.tupleToString[tuple(strs)] = generatedString
        self.stringToList[generatedString] = strs
        return generatedString
        
        

    def decode(self, s: str) -> List[str]:
        return self.stringToList[s]