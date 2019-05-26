from time import time
from linkedbst import LinkedBST
import random

def read_from_file(filename):
    words = []
    file = open(filename, 'r')
    for line in file:
        words.append(line[:-1])
    file.close()
    return words

def random_10000(words):
    words_10000 = []
    random.shuffle(words)
    for i in range(0, 10000):
        words_10000.append(words[i])
    return words_10000

def create_tree(words):
    tree = LinkedBST()
    for word in words:
        tree.add(word)
    return tree

def search_word(tree, words_10000):
    for word in words_10000:
        try:
            tree.find(word)
        except:
            pass

def search_list(words, words_10000):
    for word in words_10000:
        word in words


if __name__ == '__main__':
    words = read_from_file('words.txt')
    words_10000 = random_10000(words)

    now = time()
    search_list(words, words_10000)
    difference = time() - now
    print('The time of searching the list: ', end = '')
    print(difference)

    random.shuffle(words)
    tree = create_tree(words)

    now = time()
    search_word(tree, words_10000)
    difference = time() - now
    print('The time of searching in binary tree: ', end = '')
    print(difference)


    tree = tree.rebalance()
    now = time()
    search_word(tree, words_10000)
    print('The time of searching in balanced binary tree: ', end = '')
    print(difference)
