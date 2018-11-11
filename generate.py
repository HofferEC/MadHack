import requests
from bs4 import BeautifulSoup
import json
import random
import math
import sys
import time
import string
import re

# pull input word from alexa command

inputWord = sys.argv[1]

# get related words

NUMRELATEDWORDS = 6
TOLERANCE = 2


def writeToFile(message):
    with open("lyrics.txt", "w") as the_file:
        the_file.write(message)
    sys.exit()


def queryAPI(word, numWords, tolerance, param):
    inputHTTPS = "https://api.datamuse.com/words?" + param + "=" + word + "&md=f"
    response = json.loads(requests.get(inputHTTPS).text)
    words = []
    words.append(word)
    index = -1
    for x in range(1, numWords):
        index += random.randint(1, 3)
        # print(index))
        try:
            while (
                float(response[index]["tags"][-1].replace("f:", "")) <= tolerance
                or " " in response[index]["word"]
            ):
                index += 1
            words.append(response[index]["word"])
        except IndexError:
            return None

    return words


relatedWords = queryAPI(inputWord, NUMRELATEDWORDS, TOLERANCE, "ml")
if relatedWords is None:
    writeToFile("Could not find enough words related to: " + inputWord)


# find rhyming words with the above
lastWords = []
for word in relatedWords:
    lastWords.append(word)
    rhymes = queryAPI(word, 2, TOLERANCE, "rel_rhy")
    if rhymes is not None:
        lastWords.append(rhymes[1])
    else:
        simRhymes = queryAPI(word, 2, TOLERANCE, "sl")
        if simRhymes is not None:
            lastWords.append(simRhymes[1])
        else:
            writeToFile("Could not find enough rhymes related to: " + inputWord)


def get_line(keyword):
    page = requests.get(
        "https://www.lyrics.com/serp.php?st=" + keyword + "&stype=2"
    )
    soup = BeautifulSoup(page.text, "html.parser")
    lyric_list = soup.find_all("pre")
    filtered_lyrics = []
    filtered_lines = []
    for lyric in lyric_list:
        filtered_lyrics.append(lyric.text.replace("</em>", "").replace("<em>", ""))
    for lines in filtered_lyrics:
        filtered_lines.append(lines.split("\n"))
    random.shuffle(filtered_lines)
    for phrase in filtered_lines:
        for value in phrase:
            value = re.sub(r'[^\w\s]','',value)
            if value.split(" ")[-1].lower().rstrip() == keyword:
                return value



lines = []
output = ""
for word in lastWords:
    lines.append(get_line(word))
    print(word)

for line in lines:
    
    if line is not None:
        output += line.rstrip().replace("\n","") + ".\n"

writeToFile(output)
# lines = [
#     ["a1", "a2"],
#     ["b1", "b2"],
#     ["c1", "c2"],
#     ["d1", "d2"],
#     ["e1", "e2"],
#     ["f1", "f2"],
# ]

# # Put lines together into a good scheme

# out = ""
# for i in range(3):
#     j = random.randint(1, 3)
#     startIndex = i * 2
#     if j == 1:  # AABB
#         out = (
#             out
#             + lines[startIndex][0]
#             + " "
#             + lines[startIndex][1]
#             + " "
#             + lines[startIndex + 1][0]
#             + " "
#             + lines[startIndex + 1][1]
#             + " "
#         )
#     elif j == 2:  # ABBA
#         out = (
#             out
#             + lines[startIndex][0]
#             + " "
#             + lines[startIndex + 1][0]
#             + " "
#             + lines[startIndex + 1][1]
#             + " "
#             + lines[startIndex][1]
#             + " "
#         )
#     else:  # ABAB
#         out = (
#             out
#             + lines[startIndex][0]
#             + " "
#             + lines[startIndex + 1][0]
#             + " "
#             + lines[startIndex][1]
#             + " "
#             + lines[startIndex + 1][1]
#             + " "
#         )


# print(out)
# # send output back to alexa to read out.