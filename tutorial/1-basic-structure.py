from lark import Lark
from rich import print as rprint

text = """1. Blade Runner [738 points] (87 groups, 116 songs, 221 samples)
  "Move on, move on." (Note: Police robot addressing crowd gathering after
   a shootout)
    - Age of Chance; This is Crush Collision; One Thousand Years of Trouble"""

basic_grammar = r"""
start           : source_block
source_block    : source_info _NL song_block
source_info     : order "." title "[" points "points]" "(" groups "groups," songs "songs," samples "samples)"
song_block      : sample_info song_info
sample_info     : sample "(Note:" note ")" 
sample          : DQUOTE WORD_EXP+ DQUOTE
song_info       : "-" artist ";" song ";" album

order   : INT
title   : WORD+
points  : INT
groups  : INT
songs   : INT
samples : INT
note    : WORD_EXP+
artist  : WORD+
song    : WORD+
album   : WORD+

%import common.INT
%import common.WORD
%import common.NEWLINE -> _NL
%import common.WS
%ignore WS
WORD_EXP        : WORD | "," | "."
DQUOTE          : "\""
"""

parser = Lark(grammar=basic_grammar)
parsed = parser.parse(text)
rprint(parsed)

