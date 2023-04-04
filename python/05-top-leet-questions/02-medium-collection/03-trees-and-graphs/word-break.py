from typing import List, Set


# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
# sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.chars = set()

    def insert(self, word: str) -> None:
        # update chars set
        for c in word:
            self.chars.add(c)

        # traverse from root
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        if not set(word).issubset(self.chars):
            return False

        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        fail_memo = set()
        return self.wb(s, word_set, fail_memo)

    def wb(self, s: str, word_set: Set[str], fail_memo: Set[str]) -> bool:
        if len(s) == 0:
            return True

        if s in fail_memo:
            return False

        for i in range(1, len(s) + 1):
            if s[:i] in word_set and self.wb(s[i:], word_set, fail_memo):
                return True

        fail_memo.add(s)
        return False

    def wordBreakDP(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]

    def wordBreakNaive(self, s: str, wordDict: List[str]) -> bool:
        # base case
        if len(s) == 0:
            return True

        # build trie from wordDict
        word_trie = self.build_trie(wordDict)

        if not set(s).issubset(word_trie.chars):
            return False

        # traverse through s and check if there are candidate words
        for i in range(1, len(s) + 1):
            if word_trie.search(s[:i]) and self.wordBreak(s[i:], wordDict):
                return True

        return False

    def build_trie(self, wordDict: List[str]) -> Trie:
        t = Trie()
        for w in wordDict:
            t.insert(w)
        return t


if __name__ == "__main__":
    ...
