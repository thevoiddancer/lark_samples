# lark_samples
Lark code to parse the samples for the samples_revived repo.

In addition, the repo holds a short tutorial on lark use, applied on this
particular problem

## Samples syntax
Syntax is quite complex, with basic structure clear, but with multiple additions.

### Basic syntax
Basic syntax example follows:
```
1. Blade Runner [738 points] (87 groups, 116 songs, 221 samples)
  "Move on, move on." (Note: Police robot addressing crowd gathering after
   a shootout)
    - Age of Chance; This is Crush Collision; One Thousand Years of Trouble
```


### Additional syntax
Additionally, depending on the sample type, expanded syntax is possible:
```
  "..."            Basic sample

  "'...'           
   '...'"          Sample with conversation

  "... <???> ..."  Sample with unclear part

  "... [...] ..."  Sample with a sound effect

  [...]            Pure sound effect

  "[...]"          Pure sound effect (but rewared a point in the old site)

  "..." @ M:SS     Timestamp of the sample
```

Clearly, additional syntax complicates the parsing significantly, 
so will be ignored for the time being.

## Lark tutorial
In this example we will use just the Basic syntax mentioned in the section
above to analyze the problem and create the basic lark grammar. 

Example:
```
1. Blade Runner [738 points] (87 groups, 116 songs, 221 samples)
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
    - 1000 Homo DJs; Supernaut; Supernaut
```

As we can see in the example, we have multiple samples in one song, 
multiple samples for one film, and we have several films/sources listed.

### Step 1: basic structure
Basic source structure is as follows:
order. source_name [source_points] (source_uses)
    "sample_text" (sample_note)
        - band_name; song_name; album_name

Basic structure is implemented in tutorial/1-basic-structure.py explained below:
1. Set up the basic terminals, INT and STRING (%include lines and below)
2. Write out the basic structure by separating it into logical units (rules)
   The trickiest part, but it helps to separate it logically. 
   For instance, in this case:
     - first line talks about sample source: "source_info"
        - contains source order, title, points and uses
     - the rest talk about sample use: "sample_block"
        - contains sample info and song info
            - sample info contains sample text and note
            - song info contains artist, song and album
     - in addition, wrap the whole thing in a block (source_block) 
3. Set up the lark with grammar and parse it

### Step 2: repeating structure
To expand our example to the one listed above, if we have done the first step
correctly, all we need to do is add the repeating mark (* or +, as in regex).

To test this out, add individual sections one by one (add extra sample, extra
song and extra sauce).

In addition, extra data will require expansion of rules and terminals.

### Step 3: Transformer