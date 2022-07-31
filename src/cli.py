from src.evaluator import WTFEval
from src.lexer import WTFLexer
from src.parser import WTFParser 

env = {}

def run(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            parser = WTFParser()
            lexer = WTFLexer()
            tree = parser.parse(lexer.tokenize(line))
            WTFEval(tree, env)
