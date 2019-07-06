class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse_letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                         "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        eng_alpa = [chr(i) for i in range(97, 97 + 26)]
        word_dict = dict(zip(eng_alpa, morse_letters))
        set_word = set()
        for word in words:
            convertedstr = ''
            for letter in word:
                convertedstr += ''.join(word_dict[letter])
            set_word.add(convertedstr)
        return len(set_word)


'''
Ideas/thoughts:
create a dict , with ardinal of 97, and put value from the Morse code list.
just iterate now thru the values of dict and return sum.
'''