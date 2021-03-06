import collections
import string


def findLadders(beginWord, endWord, wordList):
    wordList = set(wordList)
    res = []
    layer = {}
    layer[beginWord] = [[beginWord]]

    while layer:
        newlayer = collections.defaultdict(list)
        for w in layer:
            if w == endWord:
                res.extend(k for k in layer[w])
            else:
                for i in range(len(w)):
                    for c in string.ascii_lowercase:
                        neww = w[:i] + c + w[i + 1:]
                        if neww in wordList:
                            newlayer[neww] += [j + [neww] for j in layer[w]]

        wordList -= set(newlayer.keys())
        layer = newlayer

    return res

if __name__ == '__main__':
    print(findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))