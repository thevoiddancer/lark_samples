from lark import Lark
from rich import print as rprint

text = """1. Blade Runner [738 points] (87 groups, 116 songs, 221 samples)
  "Move on, move on." (Note: Police robot addressing crowd gathering after
   a shootout)
    - Age of Chance; This is Crush Collision; One Thousand Years of Trouble

  "All diese Momente werden verloren sein in der Zeit" (Note: "All those
   moments will be lost in time")
  "Zeit zu sterben." (Note: "Time to die.")
    - Amgod; Silence besides the Sun; Half Rotten and Decayed
    
2. NASA (Space Programmes) [490 points] (49 groups, 57 songs, 226 samples)
  "T minus 15 seconds, guidance is internal...12, 11, 10, 9...ignition sequence
   start, 6, 5, 4, 3, 2, 1, zero..." (Note: The Space Shuttle)
    - 1000 Homo DJs; Supernaut; Supernaut"""

basic_grammar = r"""
start           : source_block*
source_block    : source_info _NL song_block*
source_info     : order "." title "[" points "points]" "(" groups "groups," songs "songs," samples "samples)"
song_block      : sample_info* song_info
sample_info     : sample "(Note:" note ")" 
sample          : DQUOTE WORD_EXP+ DQUOTE
song_info       : "-" artist ";" song ";" album

order   : INT
title   : WORD_EXP+
points  : INT
groups  : INT
songs   : INT
samples : INT
note    : WORD_EXP+
artist  : WORD_EXP+
song    : WORD+
album   : WORD+

%import common.INT
%import common.WORD
%import common.NEWLINE -> _NL
%import common.WS
%ignore WS
WORD_EXP        : WORD | "," | "." | DQUOTE | "(" | ")" | INT
DQUOTE          : "\""
"""

parser = Lark(grammar=basic_grammar)
parsed = parser.parse(text)
rprint(parsed)

