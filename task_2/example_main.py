from linkedbst import LinkedBST
import random
from time import time


def get_words(file_name):
    """
    Reading file and shuffling word list
    """
    words_list = []
    f = open(file_name, "r")
    for line in f:
        words_list.append(line[:-1])
    return words_list


def get_1000_random(words_list):
    lst = []
    random.shuffle(words_list)
    for counter in range(10000):
        lst.append(word_list[counter])
    return lst


def build_tree(word_list):
    """
    Creating a Binary tree with the words in the given list
    """
    tree = LinkedBST()
    for word in word_list:
        tree.add(word)
    return tree


def search_tree(tree, random_1000):
    """
    Searching words in the binary Tree
    """
    for el in random_10000:
        tree.find(el)


def search_lst(word_list, random_10000):
    """
    Searchind in the word list
    """
    for el in random_10000:
        el in word_list


if name == "main":
    word_list = get_words("words.txt")
    random_10000 = get_1000_random(word_list)

    before = time()
    search_lst(word_list, random_10000)
    print(time() - before, "seconds result of lst finder")

    random.shuffle(word_list)
    tree = build_tree(word_list)

    before = time()
    search_tree(tree, random_10000)
    print(time() - before, "result of BinarySearchTree")

    tree = tree.rebalance()
    before = time()
    search_tree(tree, random_10000)
    print(time() - before, "result of Balansed BinarySearchTree")
