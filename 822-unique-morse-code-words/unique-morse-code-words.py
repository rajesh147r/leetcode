class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha="abcdefghijklmnopqrstuvwxyz"
        morse_dict=dict(zip(alpha,morse))
        word1=[]
        for word in words:
            k=""
            for i in word:
                k+=morse_dict[i]
            word1.append(k)
        return len(set(word1))
