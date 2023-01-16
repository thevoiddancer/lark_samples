from lark import Lark, Transformer, Tree
from rich import print as rprint


text = """
1. Blade Runner [738 points] (87 groups, 116 songs, 221 samples)
  "Move on, move on."
    - Age of Chance; This is Crush Collision; One Thousand Years of Trouble
"""

# 1. Blade Runner [738 points] (87 groups, 116 songs, 221 samples)
#   "Move on, move on."
#     - Age of Chance; This is Crush Collision; One Thousand Years of Trouble

grammar = r"""
start           : sample_block 
sample_block    : start1 start2 start3

start1           : _INT "." source "[" _STRING* "]" "(" _STRING* ")" [_NL]
source          : STRING*
start2           : _DQUOTE STRING* _DQUOTE [_NL]
start3           : "-" band ";" song ";" album
band            : STRING*
song            : STRING*
album           : STRING*

_DQUOTE          : "\""
_STRING         : STRING
_INT            : INT
STRING          : ESCAPED_STRING | VALUE
VALUE           : ("_" | LETTER | DIGIT | "-" | "[]" | "/" | "." | ":" | ",")+

%import common.LETTER
%import common.ESCAPED_STRING
%import common.INT
%import common.DIGIT
%import common.WS
%ignore WS
_NL: /(\r?\n[\t ]*)+/
"""

class Trans(Transformer):
    def __default__(self, data, children, meta):
        if data.value in ('band', 'song', 'album', 'source'):
            return " ".join([node.value for node in children])
        else:
            return Tree(data, children, meta)

parser = Lark(grammar=grammar)
transformer = Trans()

parsed = parser.parse(text)
transformed = transformer.transform(parsed)
rprint(transformed)
