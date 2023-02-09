from io import StringIO
from lark import Lark, Transformer, Tree, Discard
from rich import print as rprint
from rich.console import Console

text = """
1. Blade Runner [738 points] (87 groups, 116 songs, 221 samples)
  "Move on, move on." (Note: Police robot addressing crowd gathering after
   a shootout)
    - Age of Chance; This is Crush Collision; One Thousand Years of Trouble

  "All diese Momente werden verloren sein in der Zeit" @ 0:12 (Note: "All those
   moments will be lost in time")
  "Zeit zu sterben." @ 0:24 (Note: "Time to die.")
  [Roy howling like a wolf]  @ 0:48 (Note: Just before the final fight with
  Deckard)
  "Gigantische Schiffe, die brannten, draußen vor der Schulter des
   Orion." @ 1:36 (Note: "Attack ships on fire off the shoulder of Orion.")
  "Gib mir Leben, Vater!" @ 3:05 (Note: "I want more life, father!")
  (Note: All samples taken from the dubbed German version)
    - Amgod; Silence besides the Sun; Half Rotten and Decayed

  "That's what it is to be a slave." @ 1:39 (Note: Roy Batty)
  "Quite an experience to live in fear isn't it... That's what it is
   to be a slave." @ 0:33 (Note: Roy Batty. Partly used at 3:49 and 5:02 as
   well)
    - Aslan Faction; Forced Bleeding; Blunt Force Trauma

  "I've seen things you people wouldn't believe..."
  "...attack ships on fire off the shores of Orion."
  "I've done questionable things - also extraordinary things, revel in your
   time!"
    - ATD Convention; Cyber Vision; (Demo)
"""

"""

"""

grammar = r"""
start
"""



grammar_not_working_correctly = r"""
start           : source_block 

source_block    : source_info song_use_entry*
source_info     : _INT "." source "[" _STRING* "]" "(" _STRING* ")" [_NL]
source          : STRING*

song_use_entry  : sample_entry*  song_info

sample_entry    : [sample_text] [timestamp] [sample_note] _NL

sample_text     : (_DQUOTE STRING* _DQUOTE) | ("[" STRING* "]")
timestamp       : "@" (INT (":" INT)* [","])*
sample_note     : "(Note:" (STRING_EXP | _NL)* ")"

song_info       : "-" band ";" song ";" album
band            : STRING*
song            : STRING*
album           : ["("] STRING* [")"]

_DQUOTE          : "\""
_STRING         : STRING
_INT            : INT
STRING_EXP      : STRING | _DQUOTE
STRING          : ESCAPED_STRING | VALUE
VALUE           : ("_" | LETTER | DIGIT | "-" | "[]" | "/" | "." | ":" | "," | "ß" | "!" | "?" | "'")+

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
        if data.value in ('band', 'song', 'album', 'source', 'sample_text', 'sample_note'):
            return {data.value: ' '.join([node.value for node in children])}
        else:
            return Tree(data, children, meta)


parser = Lark(grammar=grammar)
transformer = Trans()

parsed = parser.parse(text)
transformed = transformer.transform(parsed)
rprint(transformed)
