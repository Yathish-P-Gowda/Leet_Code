class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word_count={}
        for char in words[0]:
            if char in word_count:
                word_count[char]+=1
            else:
                word_count[char]=1
        for word in words[1:]:
            temp={}
            for char in word:
                if char in temp:
                    temp[char]+=1
                else:
                    temp[char]=1
            for char , count in word_count.items():
                if char in temp:
                    word_count[char]=min(count,temp[char])
                else:
                    word_count[char]=0
        result=[]
        for char,count in word_count.items():
            result.extend([char]*count)
        return result