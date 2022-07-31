from sly import Lexer 

class WTFLexer(Lexer):
    tokens = { IDENTIFIER, INTEGER, STRING, VARIABLE, VARIABLE_ASSIGN_OP, EQUALS_OP, NOT_EQUALS_OP }
    ignore = "\t "
    literals = { ":", "=", "+", "-", "*", "/", "!", ">", "<", "%" }

    IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    VARIABLE = r'\$'

    VARIABLE_ASSIGN_OP = ':='
    EQUALS_OP = "=="
    NOT_EQUALS_OP = "!="

    @_(r'\d+')
    def INTEGER(self, t):
        t.value = int(t.value)
        return t

    @_(r'//.*')
    def COMMENT(self, t):
        pass 

    @_(r'\n+')
    def NEWLINE(self, t):
        self.line = t.value.count('\n')