#문자열의 길이만큼 탐색하면 찾을 수 있음
#trie의 insert, search, startsWith 메소드 구현하라
import collections


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word:str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True
    
    def search(self, word:str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True