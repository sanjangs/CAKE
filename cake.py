from knowledge import *

def rmSym(input):
    result = ''
    for char in input.lower():
        if 'a' <= char and char <= 'z':
            result += char
    return result

def rmNoiseWords(input):
    result = []
    for item in input:
        if not item in noise_words:
            result.append(item)
    return result

def compare(input, keywords):
    result = 0
    for item in input:
        for keyword in keywords:
            if item is keyword:
                result += 1
    return result

def search(input):
    input = rmNoiseWords(rmSym(input).split())
    temp = []
    for i in range(len(knowledge_base)):
        temp.append(compare(input, knowledge_base[i][0]))
    return knowledge_base[temp.index(max(temp))][1]
