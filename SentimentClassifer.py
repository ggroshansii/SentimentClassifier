

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

twitterData = open('files/project_twitter_data.csv', 'r')
scoreResults = open('files/resulting_data.csv', 'w+')
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


def get_pos(str):
    posCount = 0
    strippedStr = strip_punctuation(str)
    splitLine = strippedStr.split()
    for i in splitLine:
        if i.lower() in positive_words:
            posCount = posCount + 1
    return posCount


def get_neg(str):
    negCount = 0
    strippedStr = strip_punctuation(str)
    splitLine = strippedStr.split()
    for i in splitLine:
        if i.lower() in negative_words:
            negCount = negCount + 1
    return negCount


scoreResults.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")

for line in twitterData.readlines():

    header = 'tweet_text,retweet_count,reply_count'

    if line.strip() == header.strip():
        continue
    else:
        splitData = line.split(",")
        posScore = get_pos(splitData[0])
        negScore = get_neg(splitData[0])
        totalScore = int(posScore) - int(negScore)
        parameter = str(splitData[1]) + "," + str(splitData[2].strip()) + "," + str(posScore) + "," + str(negScore) + "," + str(totalScore) + "\n"
        scoreResults.write(parameter)