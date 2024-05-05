# Automata Theory & Formal Languages Assignment 1: DFA-Based Language Recognizer for Adjectives, Adverbs, and Conjunctions
This repository is a university assignment solution for detecting conjunctions, adverbs, and adjectives with Deterministic Finite Automata (DFA).
## Problem Statements
Language detection is an essential component of various text analysis tasks, particularly in Natural Language Processing (NLP) systems. Identifying specific parts of speech like adjectives, adverbs, and conjunctions can be crucial for text classification, content analysis, and sentiment analysis. However, processing text in real time for such tasks can be complex and computationally expensive. This project provides a solution using a Deterministic Finite Automaton (DFA), a powerful and efficient model for recognizing patterns in strings, enabling fast and accurate detection of specific words in input text.

## Project Overview
This project implements a DFA-based system for detecting predefined sets of words from a given input string. Specifically, it identifies adjectives, adverbs, and conjunctions from text by matching the words against DFA models generated for each category. The DFA is created from a list of words representing the language, and once the DFA is constructed, it can process input text, detecting and counting occurrences of each word from the predefined list.

The primary goal of the project is to demonstrate how DFA can be used in practical language processing tasks. It is designed to be highly efficient, processing one character at a time while simulating the state transitions of the finite automaton. Additionally, the application features a graphical user interface (GUI) built with Tkinter, where users can input text, and the program will display the detected words, their occurrences, and highlight the matches in the input.

## Key Features
1. **Automated DFA Generation:**
    - Dynamically generates DFA states and transitions based on predefined word lists for adjectives, adverbs, and conjunctions.
    - Uses a greedy matching strategy for accurate phrase recognition.

2. **Language Class Detection:**
    - Identifies multiple word classes (adjectives, adverbs, conjunctions) in the same text input.

3. **Interactive User Interface:**
    - Simple GUI built with Tkinter for real-time input and output.
    - Outputs detected words, their positions, and occurrences in a user-friendly format.

4. **Customizable Word Lists:**
    - Supports user-defined word lists for extending or adapting the DFA to specific linguistic needs.

5. **Efficient Text Normalization:**
    - Removes punctuation and handles case sensitivity to ensure accurate processing.

6. **Error Handling:**
    - Gracefully manages invalid input or characters not part of the DFA alphabet.

7. **Visualization:**
    - Highlights identified patterns directly in the text output for clarity.

## Technologies Used
- **Python:** Programming language used for the implementation of the DFA and GUI.
- **Tkinter:** Used for building the graphical user interface.
- **DFA (Deterministic Finite Automaton):** A theoretical model used for efficient word detection and state transitions.
- **Counter:** Python’s collections.Counter for counting word occurrences.
- **Text File Processing:** Used to load and process word lists from text files.

## How It Works
The program will work by generating DFA states. For this to work, the user will need to pass in a list of words that is in the DFA. For example, in this repository the list of words for adjectives are `big, small, blue`. The user will need to have the list of words beforehand in order to generate the DFA.

Once the user have generated the DFA based on the list, the user can easily call the `run()` function within the DFA class to let the DFA detect the language defined. The `run()` function will return a list of detected words based on a given input by the user.

The DFA will be able to detect phrases that have more than one word. This is capable because the DFA uses a greedy method to detect words.

It is also worth noting that the DFA in this program is basically a map of characters to their possible next states. Example below.

```json lines
{
    // Current state available options and their respective possible next states.
    0: {
        'a': 1,
        'b': 2,
        'c': 3
    },
    1: {
        't': 4,
    },
    2: {
        ...
    }
}
```
The example above will be able to match the word `"at"` because the starting state *(index 0)* can start with the character `"a"`. `"a"` then have the option to go to *state number 1* which it can transition with the character `"t"`. 

If `"t"` is a final state, then there will be **no state number 4**. Which the program will raise a `KeyError`, and from there will determine if the word will be accepted or not.

## Files and Folders
1. The list of words for conjunctions, adverbs, and adjectives are defined in the ![language](language) folder.

2. The ![demo-text](demo-text) folder contain two text files where the DFA will be tested against.

3. The ![dfa.py](dfa.py) file defines the DFA class which have functions to generate the finite states and perform detection based on the finite states generated.