
# game zone cli

small terminal game collection i built while learning python.

## games

- **escape the mansion** - text adventure, 10 rooms, find the key, pick a lock
- **guess the number** - 1 to 100, get hints
- **scrambled words** - unscramble 3 shuffled words
- **rock paper scissors** - first to 3 wins

all in the terminal with colors. no gui, no internet.

## run it

clone the repo and then navigte to the folder then -

```bash
python3 game.py
```

## tech

| thing | what |
|---|---|
| language | python 3.8+ |
| colors | ansi escape codes |
| libraries | `random`, `time` (built-in) |
| dependencies | none |

## mansion game

you wake up in a mansion. find the key and escape.

commands: `north` `south` `east` `west` `up` `down` `take <item>` `search <thing>` `inventory` `help` `quit`

key is under the bed in the bedroom. then go back to the living room and `south` to the door.

there's a lockpicking minigame at the end - 5 tumblers, pick 1-10 for each. last one is 1-15. pick difficulty: careful (6 tries), normal (4), rushed (2). pick can bend randomly.

no save files yet. every launch starts fresh.

## what works and what doesn't

working: all 4 games, the mansion with all 10 rooms, the lockpick minigame


## tech

just python. `random` and `time` from stdlib. ansi codes for colors.

## license

mit , check the licence file for more info

## stuff i used to learn

- [ansi codes - wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code)
(this link was found by ai before i made this project)



