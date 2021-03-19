

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

twitterData = open('files/project_twitter_data.csv', 'r')
posWords = open('files/positive_words.txt', 'r')
negWords = open('files/negative_words.txt', 'r')
#print(posWords.read())

'''
for i in posWords:
    if i.startswith(";"):
        continue
    else:
        print(i)
'''
def strip_punctuation(str): 
    filteredLetters = []
    newSentence = ""
    #split string into list of words
    splitLine = str.split()
    #iterate list of words
    for i in splitLine:
        #check to see if list is empty, if not then add space (between words)
        if filteredLetters:
            filteredLetters.append(" ")
        #split word in to list of letters
        splitLetters = list(i)
        #iterate through that list of letters
        for i in splitLetters:
            if i in punctuation_chars:
                continue
            else:
                filteredLetters.append(i)
    return "".join(filteredLetters)

'''for i in splitStr:
        if i in punctuation_chars:'''

str = "hey what's going on y'all??"

print(strip_punctuation(str))