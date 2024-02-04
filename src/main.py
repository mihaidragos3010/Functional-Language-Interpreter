from sys import argv
from .Lexer import Lexer

# Function read the input file and return a string of it
def read(file_name: str) -> str:
    try:
        with open(f"{file_name}", 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."
    
# Function that use a lexer to return a list of tokens
def init_list_of_tokens(string: str) -> list[tuple[str, str]] | None:
    spec = [
			("SPACE", "\\ "),
			("NEWLINE", "\n"),
            ("TAB", "\t"),
            ('COLON', ':'),
            ("LEFT_PARENTHESIS", r"\("),
            ("RIGHT_PARENTHESIS", r"\)"),
            ("LAMBDA", "lambda"),
            ("SUM", r"\+"),
            ("CONCAT", r"\+\+"),
			("NUMBER", "[0-9]+"),
            ("SYMBOL", "([a-z]|[A-Z])+")
		]
    
    return Lexer(spec).lex(string)

# This is a abstract node for tree
class Atom:

    # Variable used to check if this node can by iterate. This variable 
    # have a powerful meaning for list and lambda
    isOpen: bool

    def __init__(self) -> None:
        isOpen = False
        self.parent = None

        pass

    def action(self) :
        pass

# Node means a list 
class List(Atom):

    children: [Atom]

    def __init__(self, children: [Atom]) -> None:
        super().__init__()
        self.isOpen = True
        self.children = children

    # Function used to swich my position in tree with an given atom as a parameter
    def action(self, new_instance: Atom):

        if isinstance(self.parent, List):
            index = self.parent.children.index(self)
            self.parent.children.pop(index)
            self.parent.children.insert(index, new_instance)
            new_instance.parent = self.parent
            return self

        if isinstance(self.parent, Lambda):
            self.parent.expression = new_instance
            return self

        return new_instance
    
    def __str__(self):

        string_to_return = ""

        if self.children == []:
            string_to_return += "()"
        else:
            string_to_return += "( "
            for atom in self.children:
                string_to_return += atom.__str__()
                string_to_return += " "
            string_to_return += ")"

        return string_to_return

# Node means a number
class Number(Atom):

    value: int

    def __init__(self, value: int) -> None:
        super().__init__()
        self.isOpen = False
        self.value = value

    def __str__(self):
        return f"{self.value}"
    

# Node means a sum function that iterates recursivly each list and return a sum of elemens
class Sum(Atom):

    def __init__(self) -> None:
        super().__init__()
        self.isOpen = False

    def __str__(self):
        return f"+"

    # Function iterate through a tree and return sum of numbers node
    def action(self, root: Atom) -> Number:

        new_number = 0
        if isinstance(root, List):
            for child in root.children:

                if isinstance(child, List):
                    new_number += self.action(child).value

                if isinstance(child, Number):
                    new_number += child.value

        if isinstance(root, Number):
            new_number += root.value

        return Number(new_number)

# This node means a concat function that append each elements if a given list
class Concat(Atom):

    def __init__(self) -> None:
        super().__init__()
        self.isOpen = False

    def __str__(self):
        return f"++"

    # Function iterate through a given list and return a new list based on concat of each elements
    def action(self, root: Atom) -> List:

        new_List = List([])
        if isinstance(root, List):
            for child in root.children:

                if isinstance(child, List):
                    for nephew in child.children:
                        new_List.children.append(nephew)
                if isinstance(child, Number):
                    new_List.children.append(child)

        return new_List

# This node means a symbol of a lambda function
class Symbol(Atom):

    value: str

    def __init__(self, value: str) -> None:
        super().__init__()
        self.isOpen = False
        self.value = value

    def __str__(self):
        return f"{self.value}"
    

# This node means a lambda function that change his symbol as one argument
class Lambda(Atom):

    symbol: str
    expression: Atom

    def __init__(self, symbol: str) -> None:
        super().__init__()
        self.isOpen = True
        self.symbol = symbol
        self.expression = None

    def __str__(self):
        return f"lambda {self.symbol}: {self.expression}"
    
    def isMySymbol(self, symbol: Symbol) -> bool:
        return self.symbol == symbol.value
    
    # Function used to change each symbol owned by this node with a given argument
    def action(self, root: Atom, arg: Atom) -> Atom:
        
        if isinstance(root, List):
            for index in range(len(root.children)):
                root.children[index] = self.action(root.children[index], arg)

        if isinstance(root, Lambda):
            root.expression = self.action(root.expression, arg)

        if isinstance(root, Symbol) and self.isMySymbol(root):
            root = arg

        return root
    
# Class is used to parse tokens list made by a lexer to return a parse tree
class Parse():

    # List of tokens 
    tokens_list: [tuple[str, str]]

    # A dictionary of each lambda symbols and his index
    # This variable is used whether 2 different lambda have the same name to 
    # append it a index to differentiate them
    lambda_index: dict[str, int]

    # The root of tree that afterward will be return
    root: Atom

    def __init__(self, tokens: [tuple[str, str]]) -> None:
        self.tokens_list = tokens
        self.root = None

        self.lambda_index = {}
        for token, symbol in tokens:
            if token == "SYMBOL":
                self.lambda_index[symbol] = 0

    # The the last node that have "isOpen" variable true (List or Lambda)
    def takeLastOpen(self, root: Atom) -> Atom:
        
        if isinstance(root, List):
            for child in root.children:
                if child.isOpen:
                    return self.takeLastOpen(child)

        if isinstance(root, Lambda) and root.expression != None:
            if root.expression.isOpen:
                return self.takeLastOpen(root.expression)

        return root
    
    # Function that close the last list of tree, make this "isOpen" variable false
    def closeLastListOpen(self, root: Atom) -> None:
        
        if isinstance(root, List):
            for child in root.children:
                if child.isOpen:
                    return self.closeLastListOpen(child)

        if isinstance(root, Lambda) and root.expression != None:
            if root.expression.isOpen:
                return self.closeLastListOpen(root.expression)

        root.isOpen = False

    # Function that close the last lambda function and each lambda parent of it
    def closeLastLambdaOpen(self, root: Atom) -> None:
        
        if isinstance(root, List):
            for child in root.children:
                if child.isOpen:
                    return self.closeLastLambdaOpen(child)
        
        if isinstance(root, Lambda) and root.expression != None:
            if root.expression.isOpen:
                self.closeLastLambdaOpen(root.expression)

            if not root.expression.isOpen:
                root.isOpen = False
    
    # Funtion used ti insert each new node in tree
    def insert(self, node: Atom) -> None:

        if self.root == None:
            self.root = node
            return 

        last_open = self.takeLastOpen(self.root)

        if isinstance(last_open, List):
            last_open.children.append(node)
            node.parent = last_open

        if isinstance(last_open, Lambda):
            last_open.expression = node

    # Function that parse tokens list and return a tree based on it
    def parse(self) -> Atom:

        i = 0
        while i < len(self.tokens_list):
            token, value = self.tokens_list[i]

            node = None
            if token == "LEFT_PARENTHESIS":
                node = List([])

            if token == "NUMBER":
                node = Number(int(value))
            
            if token == "RIGHT_PARENTHESIS":
                self.closeLastListOpen(self.root)
                self.closeLastLambdaOpen(self.root)

            if token == "SUM":
                node = Sum()

            if token == "CONCAT":
                node = Concat()

            if token == "LAMBDA":
                _, symbol = self.tokens_list[i+2]
                self.lambda_index[symbol] += 1
                index = self.lambda_index[symbol]
                node = Lambda(f"{symbol}{index}")
                i += 3

            if token == "SYMBOL":
                symbol = value
                symbol += str(self.lambda_index[symbol])
                node = Symbol(symbol)

            if node != None:
                self.insert(node)
                self.closeLastLambdaOpen(self.root)
               
            i += 1

        return self.root

# Class interpret a parse tree
class Interpreter:

    root: Atom
    
    def __init__(self, root: Atom) -> None:
        self.root = root

    # Function check if there is a lambda node in tree
    def checkLambda(self, root: Atom) -> bool:

        rez = False
        if isinstance(root, List):
            for child in root.children:
                    rez |= self.checkLambda(child)

        if isinstance(root, Lambda):
            rez = True

        return rez

    # Function check if there is a function (Sum or Concat) node in tree
    def checkFunction(self, root: Atom) -> bool:

        rez = False
        if isinstance(root, List):
            for child in root.children:
                    rez |= self.checkFunction(child)

        if isinstance(root, Sum):
            rez = True

        if isinstance(root, Concat):
            rez = True

        return rez

    # Function that action first lambda node and switch his result with this parent
    def processFirstLambda(self, root: Atom) -> Atom:

        if isinstance(root, List):

            child = root.children[0]
            if isinstance(child, Lambda):
                rez = child.action(child.expression, root.children[1])
                root = root.action(rez)
                return root

            for child in root.children:
                if isinstance(child, List):
                    self.processFirstLambda(child)
                    return root

        pass

    # Function that execute each function (Sum and Concat) bottom to top
    def processFunctions(self, root: Atom) -> Atom:

        if isinstance(root, List):
            for child in root.children:
                if isinstance(child, List):
                    self.processFunctions(child)

            if root.children:
                child = root.children[0]
                if isinstance(child, Sum):
                    rez = child.action(root.children[1])
                    root = root.action(rez)


                if isinstance(child, Concat):
                    rez = child.action(root.children[1])
                    root = root.action(rez)

        return root

    # Function that process the tree and return a tree that means the output
    def process(self) -> Atom:

        while self.checkLambda(self.root):
            self.root = self.processFirstLambda(self.root)

        self.root = self.processFunctions(self.root)

        return self.root

def main():

    if len(argv) != 2:
        return

    # Input file name
    filename = argv[1]

    # Read input file
    application_string = read(filename)

    # Use lexer to create a list of tokens
    tokens_list = init_list_of_tokens(application_string)
    
    # Create a tree that is based by tokens list
    tree = Parse(tokens_list).parse()

    # Interpret a parse tree and return final output
    tree = Interpreter(tree).process()

    print(tree)

if __name__ == '__main__':
    main()
