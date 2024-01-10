with open('data/words.txt', "r") as f:
    listl=[]
    for line in f:
        listl.extend(line.split())
        
print(len(listl))

with open('data/wordle_words.txt', "w") as f:
    for word in listl:
        f.write(word + "\n")