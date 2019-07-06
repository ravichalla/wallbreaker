from collections import Counter
def mostCommonWord( paragraph, banned):

    for i in "!?',;.":
        paragraph= paragraph.replace(i,"")
    para_list = [str(word).lower() for word in paragraph.split(" ")]
    print(para_list)
    cntrpara = Counter(para_list)
    ban_set = set(banned)
    for word in ban_set:
        cntrpara[word]=0
    #cntrpara[""]=0
    return cntrpara.most_common(1)[0][0]   # 1 represents one most common word, and 0 gives list of element and 0 gives key

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))