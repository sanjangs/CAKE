from knowledge import *

def rmSym(input):
    result = ''
    for char in input.lower():
        if ('a' <= char and char <= 'z') or (char == ' '):
            result += char
    return result

def rmNoiseWords(input):
    result = []
    for item in input:
        if not (item in noise_words):
            result.append(item)
    return result

def compare(input, keywords):
    result = 0
    for item in input:
        for keyword in keywords:
            if item == keyword:
                result += 1
    return result

def search(input):
    input = rmNoiseWords(rmSym(input).split(' '))
    temp = []

    for i in range(0, len(knowledge_base)):
        keywords = knowledge_base[i][0]
        if len(input) >= len(keywords):
            temp.append(compare(input, keywords))
        else:
            temp.append(0)

    max_tmp = max(temp)
    if max_tmp != 0:
        return knowledge_base[temp.index(max_tmp)][1]
    else:
        return "Sorry, but i don't know its answer."
