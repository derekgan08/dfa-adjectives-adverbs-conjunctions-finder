from typing import Type
import tkinter as tk

import dfa
from dfa import generate_dfa
from collections import Counter


def input_normalization(input_string):
    """
    Normalize input string by removing punctuations and change all alphabets to become lower case.

    :param input_string: String to be normalized
    :return: String, normalized
    """
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    res = ""

    for char in input_string:
        if char not in punc:
            res += char

    return res.lower()


def dfa_data(dfa_obj: Type[dfa.DFA], input_string, language_type=""):
    """
    Function to summarize and print out the words detected by the DFA that the user passes into.

    :param dfa_obj: An object of the DFA class
    :param input_string: The input string to be processed
    :param language_type: [Optional] Specifies what is the name of the language to be printed out. Defaults to "" if not
    specified.
    :return: A dictionary of words detected, and their number of occurrences.
    """
    words_detected = dfa_obj.run(input_string)
    words_dict = Counter(words_detected)
    print(language_type, "detected :", words_detected)
    for key in words_dict:
        print(key, words_dict[key])
    return words_dict


def process(master, adjective_dfa, adverbs_dfa, conjunctions_dfa, input_string):
    """
    Function to be used with Tkinter's button command. It will pass the string from the user input and all the DFAs
    associated with it.

    :param master: Root of the Tkinter window
    :param adjective_dfa: Adjective's DFA generated
    :param adverbs_dfa: Adverb's DFA generated
    :param conjunctions_dfa: Conjunction's DFA generated
    :param input_string: The string variable that was input by the user from the Tkinter Entry widget.
    :return: Void. It will show the outputs on the Tkinter window.
    """

    detected_languages = {
        "Adjectives": dfa_data(adjective_dfa, input_string, language_type="Adjective"),
        "Adverbs": dfa_data(adverbs_dfa, input_string, language_type="Adverbs"),
        "Conjunctions": dfa_data(conjunctions_dfa, input_string, language_type="Conjunction")
    }

    for languages, data in detected_languages.items():
        tk.Label(master, text=languages, font=("calibre", 10, "bold")).pack()
        for key, number in data.items():
            tk.Label(master, text=f"{key}: {number}").pack()


if __name__ == '__main__':
    # Reading in the list of stop words to generate a DFA
    adjectives_file = open("language/adjectives.txt", "r")
    adverbs_file = open("language/adverbs.txt", "r")
    conjunctions_file = open("language/conjunctions.txt", "r")
    try:
        adjectives = adjectives_file.read().split("\n")
        adverbs = adverbs_file.read().split("\n")
        conjunctions = conjunctions_file.read().split("\n")
    finally:
        adjectives_file.close()
        adverbs_file.close()
        conjunctions_file.close()

    adjectives_dfa = generate_dfa(adjectives)
    adverbs_dfa = generate_dfa(adverbs)
    conjunctions_dfa = generate_dfa(conjunctions)

    root = tk.Tk()
    input_var = tk.StringVar()
    root.minsize(500, 500)
    root.title("CPT411 Assignment One Demonstration")
    tk.Entry(root, width=50, textvariable=input_var).pack()
    tk.Button(
        master=root,
        text="Process",
        command=lambda: process(root, adjectives_dfa, adverbs_dfa, conjunctions_dfa, input_normalization(input_var.get()))
    ).pack()
    title_label = tk.Label(root, text="Detected words, and their number of occurences.")
    title_label.pack()
    root.mainloop()
