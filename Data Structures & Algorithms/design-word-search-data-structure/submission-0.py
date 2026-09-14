class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char]=WordDictionary()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):

            if i == len(word):
                return node.end

            char = word[i]

            if char != ".":
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)

            if char == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

        return dfs(self, 0)
