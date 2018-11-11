import requests
import json
import random
import math

#pull input word from alexa command

inputWord = "jar"
inputHTTPS = "https://api.datamuse.com/words?ml=" + inputWord

response = json.loads(requests.get(inputHTTPS).text)


#get related words

NUMRELATEDWORDS = 6

relatedWords = [None] * NUMRELATEDWORDS
relatedWords[0] = inputWord
index = -1
for x in range (1,len(relatedWords)):
    index += random.randint(1,3)
    #print(index)
    while " " in  response[index]['word']:
        index += 1
    relatedWords[x] = response[index]['word']

#find rhyming words with the above

lastWords = []
for word in relatedWords:
    index = -1
    lastWords.append(word)

    inputHTTPS = "https://api.datamuse.com/words?rel_rhy=" + word
    response = json.loads(requests.get(inputHTTPS).text)

    # if the word as at least 5 rhymes, try to find a rhyme, otherwise find a word that sounds similar
    if len(response) > 5:
        index = random.randint(0, len(response)-1)

        counter = 0
        while " " in response[index]['word']:
            # if we already tried to find 5 rhymes, just find a word that sounds similar
            if counter > 5:
                inputHTTPS = "https://api.datamuse.com/words?sl=" + word
                response = json.loads(requests.get(inputHTTPS).text)
                index += random.randint(1,3)
                while " " in  response[index]['word']:
                    index += 1
            # word has a space in it, find a new one
            else:
                index = random.randint(0, len(response)-1)
                counter += 1
        # add whatever word was found to the list
        lastWords.append(response[index]['word'])
        continue
    
    # if there weren't enough rhymes, find a word that sounds similar
    inputHTTPS = "https://api.datamuse.com/words?sl=" + word
    response = json.loads(requests.get(inputHTTPS).text)
    index += random.randint(1,3)
    # if the word found has a space, find a new one
    while " " in  response[index]['word']:
        index += 1
    lastWords.append(response[index]['word'])



for i in range (0, len(lastWords), 2):
    print(lastWords[i] + ", " + lastWords[i+1])


#for i in range(len(relatedWords))

#parse SOMETHING? to develop lines ending in those given words

lines = [["a1","a2"], ["b1","b2"], ["c1","c2"], ["d1","d2"], ["e1", "e2"], ["f1", "f2"]]

#Put lines together into a good scheme

out = ""
for i in range(3):
    j = random.randint(1,3)
    startIndex = i*2
    if (j == 1): #AABB
        out = out + lines[startIndex][0] + " " + lines[startIndex][1] + " " + lines[startIndex + 1][0] + " " + lines[startIndex + 1][1] + " "
    elif (j == 2): #ABBA
        out = out + lines[startIndex][0] + " " + lines[startIndex + 1][0] + " " + lines[startIndex + 1][1] + " " + lines[startIndex][1] + " "
    else: #ABAB
        out = out + lines[startIndex][0] + " " + lines[startIndex + 1][0] + " " + lines[startIndex][1] + " " + lines[startIndex + 1][1] + " "


print(out)
#send output back to alexa to read out.
