

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

twitterData = open('files/project_twitter_data.csv', 'r')
posWords = open('files/positive_words.txt', 'r')
negWords = open('files/negative_words.txt', 'r')

positive_words = []
negative_words = []


for i in posWords.readlines():
    if i.startswith(";"):
        continue
    else:
        positive_words.append(i.strip())

for i in negWords.readlines():
    if i.startswith(";"):
        continue
    else:
        negative_words.append(i.strip())


def strip_punctuation(str): 
    filteredLetters = []
    splitLine = str.split()
    for i in splitLine:
        if filteredLetters:
            filteredLetters.append(" ")
        splitLetters = list(i)
        for i in splitLetters:
            if i in punctuation_chars:
                continue
            else:
                filteredLetters.append(i)
    return "".join(filteredLetters)


def get_neg(str):
    negCount = 0
    strippedStr = strip_punctuation(str)
    splitLine = strippedStr.split()
    for i in splitLine:
        if i.lower() in negative_words:
            negCount = negCount + 1
    return negCount

