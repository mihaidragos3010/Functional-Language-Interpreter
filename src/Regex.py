from .NFA import NFA

class Regex:
    static_indexNumber = 0
    def thompson(self) -> NFA[int]:
        raise NotImplementedError('the thompson method of the Regex class should never be called')

# The class that represents all non-operator characters or parentheses
class Character(Regex):
    character: str

    def __init__(self, character) -> None:
        super().__init__()
        self.character = character

    def thompson(self) -> NFA[int]: 
        
        S = set(self.character)     
        K = set([Regex.static_indexNumber, Regex.static_indexNumber+1])
        q0 = Regex.static_indexNumber
        d = {(Regex.static_indexNumber, self.character): set([Regex.static_indexNumber+1])}
        F = set([Regex.static_indexNumber+1])

        Regex.static_indexNumber += 2

        return NFA(S, K, q0, d, F)

    def __str__(self):
        return f"Char({self.character})"

# The class that represents the capital letters from A to Z
class AllBigCharacters(Regex):
    def thompson(self) -> NFA[int]:
        S = set(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
        K = set([Regex.static_indexNumber, Regex.static_indexNumber+1])
        q0 = Regex.static_indexNumber
        d = {}
        d[(Regex.static_indexNumber, 'A')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'B')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'C')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'D')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'E')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'F')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'G')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'H')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'I')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'J')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'K')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'L')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'M')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'N')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'O')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'P')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'Q')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'R')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'S')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'T')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'U')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'V')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'W')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'X')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'Y')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'Z')] = set([Regex.static_indexNumber+1])
        F = set([Regex.static_indexNumber+1])

        Regex.static_indexNumber += 2
        return NFA(S, K, q0, d, F)

    def __str__(self):
        return "ALL-BIG-LETTER"
    
# The class that represents the lowercase letters from a to z
class AllSmallCharacters(Regex):
    def thompson(self) -> NFA[int]:
        S = set(['a','b','c','d','e','f','g','h','i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        K = set([Regex.static_indexNumber, Regex.static_indexNumber+1])
        q0 = Regex.static_indexNumber
        d = {}
        d[(Regex.static_indexNumber, 'a')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'b')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'c')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'd')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'e')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'f')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'g')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'h')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'i')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'j')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'k')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'l')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'm')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'n')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'o')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'p')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'q')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'r')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 's')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 't')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'u')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'v')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'w')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'x')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'y')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, 'z')] = set([Regex.static_indexNumber+1])
        F = set([Regex.static_indexNumber+1])

        Regex.static_indexNumber += 2
        return NFA(S, K, q0, d, F)
    
    def __str__(self):
        return "ALL-SMALL-LETTER"

# The class that represents a number
class Number(Regex):
    number: str
    def __init__(self, number) -> None:
        super().__init__()
        self.number = number

    def thompson(self) -> NFA[int]:
        
        S = set(self.number)
        K = set([Regex.static_indexNumber, Regex.static_indexNumber+1])
        q0 = Regex.static_indexNumber
        d = {}
        d[(Regex.static_indexNumber, self.number)] = set([Regex.static_indexNumber+1])
        F = set([Regex.static_indexNumber+1])

        Regex.static_indexNumber += 2
        return NFA(S, K, q0, d, F)
        
# The class that represents all the numbers from 0 to 9
class AllNumbers(Regex):
    def thompson(self) -> NFA[int]:
        S = set(['0','1','2','3','4','5','6','7','8','9'])
        K = set([Regex.static_indexNumber, Regex.static_indexNumber+1])
        q0 = Regex.static_indexNumber
        d = {}
        d[(Regex.static_indexNumber, '0')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, '1')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, '2')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, '3')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, '4')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, '5')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, '6')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, '7')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, '8')] = set([Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, '9')] = set([Regex.static_indexNumber+1])
        F = set([Regex.static_indexNumber+1])

        Regex.static_indexNumber += 2
        return NFA(S, K, q0, d, F)
    def __str__(self):
        return "ALL-NUMBERS"

# The class representing the union operator
class Union(Regex):
    nfa1: NFA
    nfa2: NFA

    def __init__(self) -> None:
        super().__init__()

    def thompson(self) -> NFA[int]:
        S = self.nfa1.S.union(self.nfa2.S)
        K = self.nfa1.K.union(self.nfa2.K.union([Regex.static_indexNumber, Regex.static_indexNumber+1]))
        q0 = Regex.static_indexNumber
        d = {**self.nfa1.d, **self.nfa2.d}
        d[(Regex.static_indexNumber, '')] = set([self.nfa1.q0, self.nfa2.q0])
        d[(next(iter(self.nfa1.F)), '')] = set([Regex.static_indexNumber+1, Regex.static_indexNumber+1])
        d[(next(iter(self.nfa2.F)), '')] = set([Regex.static_indexNumber+1])
        F = set([Regex.static_indexNumber+1])

        Regex.static_indexNumber += 2
        return NFA(S, K, q0, d, F)
    
    def __str__(self):
        return "|"

# The class representing the concatenation operator   
class Concat(Regex):
    nfa1: NFA
    nfa2: NFA

    def __init__(self) -> None:
        super().__init__()

    def thompson(self) -> NFA[int]:
        
        S = self.nfa1.S.union(self.nfa2.S)
        K = self.nfa1.K.union(self.nfa2.K)
        q0 = self.nfa1.q0
        d = {**self.nfa1.d, **self.nfa2.d}
        d[(next(iter(self.nfa1.F)), '')] = set([self.nfa2.q0])
        F = self.nfa2.F

        return NFA(S, K, q0, d, F)
    def __str__(self):
        return "."

# The class representing the star operator   
class Star(Regex):
    nfa1: NFA

    def __init__(self) -> None:
        super().__init__()

    def thompson(self) -> NFA[int]:
        S = self.nfa1.S
        K = self.nfa1.K.union([Regex.static_indexNumber, Regex.static_indexNumber+1])
        q0 = Regex.static_indexNumber
        d = self.nfa1.d
        d[(Regex.static_indexNumber, '')] = set([self.nfa1.q0])
        d[(next(iter(self.nfa1.F)), '')] = set([self.nfa1.q0, Regex.static_indexNumber+1])
        d[(Regex.static_indexNumber, '')] = set([self.nfa1.q0, Regex.static_indexNumber+1])
        F = set([Regex.static_indexNumber+1])

        Regex.static_indexNumber += 2
        return NFA(S, K, q0, d, F)
    
    def __str__(self):
        return "*"

# The class representing the plus operator
class Plus(Regex):
    nfa1: NFA

    def __init__(self) -> None:
        super().__init__()

    def thompson(self) -> NFA[int]:
        S = self.nfa1.S
        K = self.nfa1.K.union([Regex.static_indexNumber, Regex.static_indexNumber+1])
        q0 = Regex.static_indexNumber
        d = self.nfa1.d
        d[(Regex.static_indexNumber, '')] = set([self.nfa1.q0])
        d[(next(iter(self.nfa1.F)), '')] = set([self.nfa1.q0, Regex.static_indexNumber+1])
        F = set([Regex.static_indexNumber+1])

        Regex.static_indexNumber += 2
        return NFA(S, K, q0, d, F)
    
    def __str__(self):
        return "+"

# The class representing the question mark operator
class QuestionMark(Regex):
    nfa1: NFA

    def __init__(self) -> None:
        super().__init__()

    def thompson(self) -> NFA[int]:
        S = self.nfa1.S
        K = self.nfa1.K.union([Regex.static_indexNumber, Regex.static_indexNumber+1])
        q0 = Regex.static_indexNumber
        d = self.nfa1.d
        d[(Regex.static_indexNumber, '')] = set([self.nfa1.q0, Regex.static_indexNumber+1])
        d[(next(iter(self.nfa1.F)), '')] = set([Regex.static_indexNumber+1])
        F = set([Regex.static_indexNumber+1])

        Regex.static_indexNumber += 2
        return NFA(S, K, q0, d, F)
    
    def __str__(self):
        return "?"

# The class represented by the bracket on the left
class LeftParenthesis(Regex):
    def __init__(self) -> None:
        super().__init__()
    def thompson(self) -> NFA[int]:
        raise NotImplementedError('the thompson method of the Regex class should never be called')
    def __str__(self):
        return "("

# The class represented by the bracket on the right
class RightParenthesis(Regex):
    def __init__(self) -> None:
        super().__init__()
    def thompson(self) -> NFA[int]:
        raise NotImplementedError('the thompson method of the Regex class should never be called')
    def __str__(self):
        return ")"

# Classes that convert me from a regex in the form of a string to a list of regex
def init_list_of_regex(regex: str) -> [Regex]:
    list = []
    index = 0
    while index < len(regex):

        # The case where I try to get rid of spaces
        if regex[index] == ' ':
            index += 1

        # The case in which I treat all symbols from a start to an end
        elif regex[index] == '[':
            if regex[index+1].isupper():
                list.append(AllBigCharacters())
            elif regex[index+1].islower():
                list.append(AllSmallCharacters())
            elif regex[index+1].isdigit():
                list.append(AllNumbers())
            index += 5

        # Below I convert each string character into a regex type subclass
        elif regex[index] == '(':
            list.append(LeftParenthesis())
            index += 1

        elif regex[index] == ')':
            list.append(RightParenthesis())
            index += 1

        elif regex[index] == '\\':
            list.append(Character(regex[index+1]))
            index += 2
        
        elif regex[index] == '|':
            list.append(Union())
            index += 1

        elif regex[index] == '*':
            list.append(Star())
            index += 1
        
        elif regex[index] == '+':
            list.append(Plus())
            index += 1

        elif regex[index] == '?':
            list.append(QuestionMark())
            index += 1

        else:
            list.append(Character(regex[index]))
            index += 1
    
    return list

#   Function that checks if an element in the list is of neutral type. I considered an element to be of neutral 
# type that can have the "Concat" operator both on the left and on the right
def isNeutralObjects(regexObject: Regex) -> bool:
    neutralObjects = [Character, AllBigCharacters, AllSmallCharacters, AllNumbers]
    for obj_class in neutralObjects:
        if isinstance(regexObject, obj_class):
            return True
    return False



#   Function that checks if an element in the list is of left side type. I considered an element to be of the 
# left side type that can only be to the left of the "Concat" operator
def isLeftSideObjects(regexObject: Regex) -> bool:
    leftSideObjects = [Star, Plus, QuestionMark, RightParenthesis]
    for obj_class in leftSideObjects:
        if isinstance(regexObject, obj_class):
            return True
    return False


#   Function that checks if an element in the list is of left side type. I considered an element to be of the 
# right side type that can only be to the right of the "Concat" operator
def isRightSideObjects(regexObject: Regex) -> bool:
    rightSideObjects = [LeftParenthesis]
    for obj_class in rightSideObjects:
        if isinstance(regexObject, obj_class):
            return True
    return False

# The function inserts "Concat" type elements in the correct places in the regex list sent as an argument
# For instance: ["a", "b"] --> ["a", ".", "b"]
#               ["a", "*", "b", "(", "d", "c", "+", ")"] --> ["a", "*", ".", "b", ".", "(", "d", ".", "c", "+", ")"] 
def insert_Concat_In_List(list: [Regex]) -> [Regex]:

    index = 0
    while index < len(list) - 1:

        # The case where I have two neutral elements one after the other
        if isNeutralObjects(list[index]) and isNeutralObjects(list[index+1]):
            list.insert(index+1,Concat())
            index += 1

        # The case where I have an element that can sit on the left and the next one is neutral
        if isLeftSideObjects(list[index]) and isNeutralObjects(list[index+1]):
            list.insert(index+1,Concat())
            index += 1

        # The case where I have an element that can stand on the right and the previous one is neutral
        if isNeutralObjects(list[index]) and isRightSideObjects(list[index+1]):
            list.insert(index+1,Concat())
            index += 1

        # The case where I have an element that can sit on the left and one that can sit on the right
        if isLeftSideObjects(list[index]) and isRightSideObjects(list[index+1]):
            list.insert(index+1,Concat())
            index += 1

        index += 1  

    return list


# The function applies the Shunting-Yard algorithm to obtain an ordering similar to traversing a priority tree of operations.
def shunting_yard(list: [Regex]) -> [Regex]:

    priorities = {Star:3, Plus:3, QuestionMark:3, Concat:2, Union:1}
    letterList = [Character, AllBigCharacters, AllSmallCharacters, AllNumbers]
    output = []
    operatorStack = []

    index = 0
    while index < len(list):
        symbol = list[index]

        # If the input symbol is a letter… append it directly to the output queue
        if type(symbol) in letterList:
            output.append(symbol)

        # If the input symbol is an operator… if there exists an operator already on the top of the operator stack with higher 
        # or equal precedence than our current input symbol, remove the operator from the top of the operator stack and append 
        # it to the output queue. Do this until the current input symbol has a higher precedence than the symbol on the top of the 
        # operator stack, or the operator stack is empty.
        elif type(symbol) in priorities:
            while operatorStack and type(operatorStack[-1]) != LeftParenthesis and priorities[type(operatorStack[-1])] >= priorities[type(symbol)]:
                output.append(operatorStack.pop())
            operatorStack.append(symbol)

        # If the input symbol is an ( … append it to the operator stack
        elif type(symbol) == LeftParenthesis:
            operatorStack.append(symbol)

        # If the input symbol is an ) … pop all operators from the operator stack and append them to the output queue until 
        # you find an ( . Then, you can remove both of those parentheses and continue with the algorithm.
        elif type(symbol) == RightParenthesis:
            while operatorStack and type(operatorStack[-1]) != LeftParenthesis:
                output.append(operatorStack.pop())
            operatorStack.pop()

        index += 1

    # If I'm left with operators in the stack, I'll add them to the end of the output list
    while operatorStack:
        output.append(operatorStack.pop())

    return output


# Function used for construction after the Shunting-Yard algorithm to gradually build the final regex
def build_final_regex(list: [Regex]) -> Regex:
    operators = [Concat, Union, Star, Plus, QuestionMark]
    stack = []
    
    index = 0
    while index < len(list):
        symbol = list[index]

        if type(symbol) == Concat:
            symbol.nfa1 = stack[-2].thompson()
            symbol.nfa2 = stack[-1].thompson()
            stack.pop()
            stack.pop()
            stack.append(symbol)

        elif type(symbol) == Union:
            symbol.nfa1 = stack[-2].thompson()
            symbol.nfa2 = stack[-1].thompson()
            stack.pop()
            stack.pop()
            stack.append(symbol)

        elif type(symbol) == Star:
            symbol.nfa1 = stack.pop().thompson()
            stack.append(symbol)

        elif type(symbol) == Plus:
            symbol.nfa1 = stack.pop().thompson()
            stack.append(symbol)

        elif type(symbol) == QuestionMark:
            symbol.nfa1 = stack.pop().thompson()
            stack.append(symbol)

        else:
            stack.append(symbol)

        index += 1
    return stack.pop()


# Function that was helpful for debugging
def debug(regexList):
    for regex_obj in regexList:
        print(regex_obj)

# Function that parses the regex in the form of a string and brings it to a final form of the Regex type
def parse_regex(regex: str) -> Regex:
    
    regexList = init_list_of_regex(regex)
    
    regexList = insert_Concat_In_List(regexList)

    regexList = shunting_yard(regexList)

    final_regex = build_final_regex(regexList)
    
    return final_regex
