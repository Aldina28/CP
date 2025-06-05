class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        window = len(word)-numFriends+1
        res = -1
        max_word = ""
        for i in range(len(word)):
            if word[i:i+window]>max_word:
                max_word = word[i:i+window]
                res = i
        return word[res:res+window]