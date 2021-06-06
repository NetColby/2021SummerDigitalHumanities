# Ruize Li
# May 29, 2021
# visualizes word frequencies trending over years

# dependencies
import numpy as np
import matplotlib.pyplot as plt
import jieba
import os

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']



# read file names in directory
def read(dir):
    f_names = []
    # list of files in data
    for item in os.listdir(dir):
        if not item.startswith('.') and os.path.isfile(os.path.join(dir, item)):
            f_names.append(item)
    return sorted(f_names)

# return a np 2d array of word frequencies
# Input:    f_names: a list of file names to process
#           words: words to be searched for freqeuncies
# Output:   np 2d array, x: file names y: key words
def word_count(dir, f_names, words):
    output = []
    # iterate through all words
    for f in f_names:
        # w_freq in one file
        temp = []
        file = dir + "/" + f
        count = jieba.lcut(open(file).read())
        word_count = {}
        for w in count:
            word_count[w] = word_count.get(w,0) + 1
        # sort words by frequencies
        w_freq = list(word_count.items())
        w_freq.sort(key = lambda x : x[1], reverse=True)
        # store results of specified words
        for word in words:
            temp.append(word_count.get(word, 0))
        output.append(temp)
    return np.array(output)
        
# plots the word trend  
def visualize(f_names, key_words, data):
    fig = plt.figure(figsize=(10,10))
    x = np.arange(data.shape[0])
    plt.plot(x, data)

    x_ticks = [f[0:4] for f in f_names]
    plt.xticks(x,x_ticks)
    plt.title("word freq in 国务院公报")
    plt.ylabel("词频/frequency")
    plt.xlabel("年份/year")
    plt.legend(labels = key_words)
    plt.savefig('1.png')
    plt.show()



# main function
# Input: word, year
if __name__ == '__main__':
    dir = "/Users/ruizeli/Documents/Colby18-21/Colby/Summer21/data"
    f_names = read(dir)
    # print(f_names)

    # count word frequencies for all files
    key_words = ["婦女"]
    output = word_count(dir, f_names, key_words)
    print(output.shape)
    visualize(f_names, key_words, output)
    
