from .DFA import *
from .NFA import *
from .Regex import *


SINK_STATE = frozenset()

class Lexer:

#   The variable that has the role of retaining my DFA associated with this Lexer
    lexer_dfa: DFA

#   The variable that has the role of providing me with a link between the index of each final state 
# and the associated token for each individual regex
    convert_state_to_token: dict[int, str]
    
    def __init__(self, spec: list[tuple[str, str]]) -> None:

        lexer_nfa = self.build_lexer_nfa(spec)

        self.lexer_dfa = lexer_nfa.subset_construction()

        pass

#   The function builds all the NFAs based on the received regexes. It creates an independent state 
# for me, which it joins with epsilon cost edges from each initial state of the previous NFAs.
    def build_lexer_nfa(self, spec: list[tuple[str, str]]) -> NFA:

        q0 = -1
        S = set()
        K = set()
        K.add(q0)
        d = {}
        F = set()
        self.convert_state_to_token = {}

        list_of_start_state = []
        for tuple in spec:
            regex = parse_regex(tuple[1])
            nfa = regex.thompson()
            S |= nfa.S
            K |= nfa.K
            list_of_start_state.append(nfa.q0)
            d.update(nfa.d)
            F |= nfa.F
            
            token = tuple[0]
            for nr in nfa.F:
                self.convert_state_to_token[nr] = token

        d[(q0,'')] = set(list_of_start_state)

        return NFA(S,K,q0,d,F)
    
    
    def lex(self, word: str) -> list[tuple[str, str]] | None:
        # this method splits the lexer into tokens based on the specification and the rules described in the lecture
        # the result is a list of tokens in the form (TOKEN_NAME:MATCHED_STRING)

        left = 0
        right = 1
        token = None
        wordAccepted = None
        indexLastAcceptedToken = 0
        lex_list = []
        nrLines = 0

        while right < len(word)+1:
            
            # I check if the currently searched word is accepted by the DFA
            isThisWordAccepted = self.lexer_dfa.accept(word[left:right])

            # I take the state from the DFA that I reached with the current searched word
            state = self.lexer_dfa.stateForWord(word[left:right])

            # I check if I receive a letter that is not in my DFA
            if word[right-1] not in self.lexer_dfa.S:
                return [("", f"No viable alternative at character {right-1}, line {nrLines}")]
            
            # The case in which I reach a state accepted by my DFA
            if isThisWordAccepted:
                indexLastAcceptedToken = right
                indexToken = min(element for element in state if element in self.convert_state_to_token)
                token = self.convert_state_to_token[indexToken]
                wordAccepted = word[left:right]

            # If I reached "SINK STATE" I will add the last accepted token. Otherwise, I will just add a new letter
            if state == SINK_STATE:

                # I am checking the case where I have reached "SINK STATE" and no word has been accepted so far
                if token == None:
                    return [("", f"No viable alternative at character {right-1}, line {nrLines}")]
                    
                lex_list.append((token, wordAccepted))

                # When I read the specific letter for "New Line" I add the token to the list and delete 
                # the left part of the word separated by this character
                if token == "NEWLINE":
                    word = word[right-1:]
                    left = 0
                    right = 1
                    token = None
                    wordAccepted = None
                    nrLines += 1
                    continue

                left = indexLastAcceptedToken
                right = left + 1
                token = None
                wordAccepted = None
            else:
                right += 1

        # I check after going through the whole word if I have found a token so far. Otherwise I will return an error
        if token == None:
            return [("", f"No viable alternative at character EOF, line {nrLines}")]
        

        lex_list.append((token, word[left:right]))
                
        return lex_list

