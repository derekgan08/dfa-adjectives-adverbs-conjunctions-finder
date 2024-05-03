class DFA:
    def __init__(self, alphabet, states, transitions, start_state, final_state):
        self.alphabet = alphabet
        self.states = states
        self.transitions = transitions
        self.start_state = start_state
        self.final_state = final_state

    def run(self, input_string):
        """
        Runs the DFA to detect for the languages defined.

        :param input_string: String to be processed
        :return: A list of detected strings
        """
        detected_words = []
        i = 0
        # Starting index of a word that is possible to be detected by the DFA.
        j = 0
        string_length = len(input_string)
        current_state = self.start_state

        while True:
            # If i is already at the last character, exit the function and return the detected words.
            if i == string_length:
                if current_state in self.final_state:
                    detected_words.append(input_string[j:i])
                return detected_words

            # If the character is not part of the accepted alphabet set. We just skip it, and move the j index.
            if input_string[i] not in self.alphabet:
                i = input_string.find(' ', i) + 1
                # If the i is 0 after searching for the index of the next space character, that means we have reached
                # the end of the string. So we will just need to exit and return the list of detected words.
                if i == 0:
                    return detected_words
                j = i
                continue

            # Try-catch structure here is because when the current state is a final state, there will no longer be any
            # transition to other states. The program will throw a KeyError for not being able to find the next state
            # from the transition dictionary.
            #
            # Hence, when there is a KeyError, the program will check if it is in a final state. And to make sure the
            # program will not accept substrings of a string, (for example, "new" is an adjective, and it is also a
            # substring of "newly". So if not handled properly, it will accept "new" in "newly") the program will check
            # if the current state is in a final state and the next character is a space. (to make sure it is the last
            # character of the word)
            #
            # If both conditions are met, then only it will accept the string.
            try:
                current_state = self.transitions[current_state].get(input_string[i], None)
            except KeyError:
                if current_state in self.final_state and input_string[i] == " ":
                    detected_words.append(input_string[j:i])
                i = input_string.find(' ', i) + 1
                current_state = self.start_state
                j = i
                # If the i is 0 after searching for the index of the next space character, that means we have reached
                # the end of the string. So we will just need to exit and return the list of detected words.
                if i == 0:
                    return detected_words
                continue

            if current_state is None:
                i = input_string.find(' ', i) + 1
                # If the i is 0 after searching for the index of the next space character, that means we have reached
                # the end of the string. So we will just need to exit and return the list of detected words.
                if i == 0:
                    return detected_words
                current_state = self.start_state
                j = i
                continue
            i += 1



def generate_dfa(words):
    """
    Generates a DFA based on the list of words of a language passed in.

    :param words: List[String] A list of strings to generate a DFA.
    :return: A DFA class.
    """
    alphabet = set("abcdefghijklmnopqrstuvwxyz ")
    states = {0}
    transitions = {}
    start_state = 0
    final_state = set()

    for i, word in enumerate(words):
        current_state = 0
        for char in word:
            # If the character in the word is not part of the language, then we do not need to build a DFA for it.
            if char not in alphabet:
                continue

            # Get the next state in the DFA of the current state based on the character available for transition
            next_state = transitions.get(current_state, {}).get(char, None)

            # If the next state is not in the DFA, then create one for it.
            if next_state is None:
                next_state = len(states)
                transitions.setdefault(current_state, {})[char] = next_state
                states.add(next_state)
            current_state = next_state
        final_state.add(current_state)

    return DFA(alphabet, states, transitions, start_state, final_state)
