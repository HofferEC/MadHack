import requests
import json
import random
import math

#pull input word from alexa command

inputWord = "man"
inputHTTPS = "https://api.datamuse.com/words?ml=" + inputWord

response = json.loads(requests.get(inputHTTPS).text)


#get related words

NUMRELATEDWORDS = 6

relatedWords = [None] * NUMRELATEDWORDS
relatedWords[0] = inputWord
index = -1
for x in range (1,len(relatedWords)):
    index += random.randint(1,3)
    print(index)
    while " " in  response[index]['word']:
        print (response[index]['word'])
        index += 1
    relatedWords[x] = response[index]['word']

for x in range(0,len(relatedWords)):
    print(x)
    print (relatedWords[x])

#find rhyming words with the above

lastWords = []
for word in relatedWords:
    lastWords.append(word)
    inputHTTPS = "https://api.datamuse.com/words?rel_rhy=" + word
    response = json.loads(requests.get(inputHTTPS).text)
    lastWords.append(response[random.randint(0,4)]['word'])

for i in range (0, len(lastWords)):
    print(lastWords[i])


#for i in range(len(relatedWords))

#parse SOMETHING? to develop lines ending in those given words

lines = [["I'm drivin me mum's car", "Something something something far"], ["a","a"], ["b","b"], ["c","c"], ["d","d"]]

#Put lines together into a good scheme

inputWord = "car"

#send output back to alexa to read out.
