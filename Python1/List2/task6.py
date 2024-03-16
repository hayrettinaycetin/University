import matplotlib.pyplot as plt
import numpy as np

f = open("word_frequency.txt","r")
text = f.read()

word_frequency = {}

words = text.split()

for word in words:
    word = word.strip('.,?!').lower()
    if word in word_frequency:
        word_frequency[word] +=1
    else:
        word_frequency[word] = 1


x = word_frequency.keys()
y = word_frequency.values() 

plt.bar(x, y,color='green')
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency in Text")
plt.xticks(rotation='vertical')
plt.show()
