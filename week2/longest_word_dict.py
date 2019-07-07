from collections import  defaultdict
from functools import reduce
def longestWord(words):
    Trie = lambda: defaultdict(Trie)
    trie = Trie()
    END = True

    for i, word in enumerate(words):
        reduce(dict.__getitem__, word, trie)[END] = i

    stack = trie.values()
    ans = ""
    while stack:
        cur = stack.pop()
        if END in cur:
            word = words[cur[END]]
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                ans = word
            stack.extend([cur[letter] for letter in cur if letter != END])

    return ans
print(longestWord(["w","wo","wor","worl", "world"]))