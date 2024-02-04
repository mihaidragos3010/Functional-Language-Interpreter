from .DFA import DFA

from dataclasses import dataclass
from collections.abc import Callable
from queue import Queue
from typing import List

EPSILON = ''  # this is how epsilon is represented by the checker in the transition function of NFAs


@dataclass
class NFA[STATE]:
    S: set[str]
    K: set[STATE]
    q0: STATE
    d: dict[tuple[STATE, str], set[STATE]]
    F: set[STATE]

    def epsilon_closure(self, state: STATE) -> set[STATE]:
        # compute the epsilon closure of a state (you will need this for subset construction)
        # see the EPSILON definition at the top of this file
        visited = []
        queue = Queue()
        answer = set()

# In this piece of code I use a basic BFS iteration through each next posible epsilon state
        visited.append(state)
        queue.put(state)
        answer.add(state)

        while not queue.empty():
            state_checked = queue.get()
            if (state_checked,'') in self.d:
                list_of_epsilon_state = self.d[(state_checked,'')]
                for state in list_of_epsilon_state:
                    # i = self.__private_getIndex(self.K, state)
                    if state not in visited:
                        # visited[i] = True
                        visited.append(state)
                        queue.put(state)
                        answer.add(state)
        
        return answer


    def subset_construction(self) -> DFA[frozenset[STATE]]:
        # convert this nfa to a dfa using the subset construction algorithm

        K_dfa = set()
        q0_dfa = frozenset(self.epsilon_closure(self.q0))
        d_dfa = {}
        F_dfa = set()

        queue = [] # Use queue to iterate each state ones

        K_dfa.add(q0_dfa)
        queue.append(q0_dfa)

        while queue:
            state = queue.pop()

            for i in self.F: # If one final state in dfa_state add this dfa_state to final_dfa
                 if i in state:
                    F_dfa.add(state)

            for letter in self.S: # Iterate through each letter
                next_state = set()

                for nr in state: # Iterate through each number in dfa_state
                    if (nr, letter) in self.d:
                        
                        for i in self.d[(nr, letter)]: # Iterate through each next number
                            next_state.update(self.epsilon_closure(i))
                
                if next_state: # If next state changed add it to dfa_d, otherwize add void frosenset
                    d_dfa[(frozenset(state), letter)] = frozenset(next_state)
                else:
                    d_dfa[(frozenset(state), letter)] = frozenset()

                if next_state not in K_dfa: # If I haven't iterated through this dfa_state add it to dfa_K and add it to queue to mark it as visited
                    queue.append(frozenset(next_state))
                    K_dfa.add(frozenset(next_state))

        return DFA(self.S, K_dfa, q0_dfa, d_dfa, F_dfa)

    def remap_states[OTHER_STATE](self, f: 'Callable[[STATE], OTHER_STATE]') -> 'NFA[OTHER_STATE]':
        # optional, but may be useful for the second stage of the project. Works similarly to 'remap_states'
        # from the DFA class. See the comments there for more details.

        
        pass
