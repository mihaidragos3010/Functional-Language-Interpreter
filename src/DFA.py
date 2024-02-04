from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class DFA[STATE]:
    S: set[str]
    K: set[STATE]
    q0: STATE
    d: dict[tuple[STATE, str], STATE]
    F: set[STATE]

    def accept(self, word: str) -> bool:

        # Check if i received empty word
        if word == '':
            return self.q0 in self.F

        # If i don't have next_state from start_state I return false 
        if (self.q0, word[0]) not in self.d:
            return False

        # Consume the first letter of the word and head through next_state       
        state = self.d[self.q0, word[0]]
        word = word[1:]

        while word:

            # If i don't have next_state from start_state I return false 
            if (state, word[0]) not in self.d:
                    return False
            
            # Consume the first letter of the word and head through next_state
            state = self.d[(state, word[0])]
            word = word[1:]


        return state in self.F
    
    # Function that returns the state reached by the consumption of a word
    def stateForWord(self, word: str) -> STATE:

        if word == '':
            return self.q0

        if (self.q0, word[0]) not in self.d:
            return

        state = self.d[self.q0, word[0]]
        word = word[1:]

        while word:
            if (state, word[0]) not in self.d:
                return

            state = self.d[(state, word[0])]
            word = word[1:]

        return state

    def remap_states[OTHER_STATE](self, f: Callable[[STATE], 'OTHER_STATE']) -> 'DFA[OTHER_STATE]':
        # optional, but might be useful for subset construction and the lexer to avoid state name conflicts.
        # this method generates a new dfa, with renamed state labels, while keeping the overall structure of the
        # automaton.

        # for example, given this dfa:

        # > (0) -a,b-> (1) ----a----> ((2))
        #               \-b-> (3) <-a,b-/
        #                   /     ⬉
        #                   \-a,b-/

        # applying the x -> x+2 function would create the following dfa:

        # > (2) -a,b-> (3) ----a----> ((4))
        #               \-b-> (5) <-a,b-/
        #                   /     ⬉
        #                   \-a,b-/

        pass

