class TrieNode:
    __slots__ = ('children', 'final')
    
    def __init__(self):
        self.children = {}
        self.final = False

    def get_or_add(self, char: str) -> 'TrieNode':
        if char not in self.children:
            self.children[char] = TrieNode()
        return self.children[char]
    
    def get(self, char: str) -> Optional['TrieNode']:
        return self.children.get(char)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self._root
        
        for char in word:
            cur_node = cur_node.get_or_add(char)
        
        cur_node.final = True
        
    def __find(self, s: str) -> Optional['TrieNode']:
        cur_node = self._root
        
        for char in s:
            cur_node = cur_node.get(char)
            if not cur_node:
                break
            
        return cur_node
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.__find(word)
        return cur_node is not None and cur_node.final

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.__find(prefix)
        return cur_node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
