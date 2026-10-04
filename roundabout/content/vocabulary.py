"""
Vocabulary initialization for Roundabout: The God-Forsaken Ring.

Based on the Zork I vocabulary, extended per mechanics.md §"Verb Canonical Map".
New canonicals: sail, dock, buy, tip, fish, drive, swap, clear, load, pry, use, cast.
Synonym additions: aboard→board; cast takes incant/chant/spell from exorcise.
set removed from turn aliases (reassigned so SET SAIL hits sail).
"""

from __future__ import annotations

from engine.parser import Vocabulary


def make_vocabulary() -> Vocabulary:
    """Create and return a populated Vocabulary for Roundabout."""
    v = Vocabulary()

    # Buzzwords — silently consumed during parsing
    v.add_buzz("again", "g", "oops")
    v.add_buzz(
        "a", "an", "the", "is", "and", "of", "then", "all", "one",
        "but", "except", "yes", "no", "y", "here",
    )

    # Prepositions
    v.add_preposition("with", "using", "through", "thru")
    v.add_preposition("in", "inside", "into")
    v.add_preposition("on", "onto")
    v.add_preposition("under", "underneath", "beneath", "below")
    v.add_preposition("at")
    v.add_preposition("from")
    v.add_preposition("to")
    v.add_preposition("down")
    v.add_preposition("off")
    v.add_preposition("over")
    v.add_preposition("about")
    v.add_preposition("for")
    v.add_preposition("behind")
    v.add_preposition("away")
    v.add_preposition("across")
    v.add_preposition("out")
    v.add_preposition("up")
    v.add_preposition("near")

    # Directions
    v.add_direction("north", "n")
    v.add_direction("south", "s")
    v.add_direction("east", "e")
    v.add_direction("west", "w")
    v.add_direction("down", "d")
    v.add_direction("up", "u")
    v.add_direction("northwest", "nw")
    v.add_direction("northeast", "ne", "northe")
    v.add_direction("southwest", "sw")
    v.add_direction("southeast", "se", "southe")
    v.add_direction("in")
    v.add_direction("out")
    v.add_direction("land")

    # -----------------------------------------------------------------------
    # Verbs — canonical first, then synonyms
    # Ordering mirrors Zork I base; Roundabout additions noted inline.
    # -----------------------------------------------------------------------

    # Meta / system
    v.add_verb("verbose")
    v.add_verb("brief")
    v.add_verb("super", "superbrief")
    v.add_verb("diagnose")
    v.add_verb("inventory", "i")
    v.add_verb("quit", "q")
    v.add_verb("restart")
    v.add_verb("restore")
    v.add_verb("save")
    v.add_verb("score")
    v.add_verb("script")
    v.add_verb("unscript")
    v.add_verb("version")

    # Action verbs (alphabetical)
    v.add_verb("activate")
    v.add_verb("answer", "reply")
    v.add_verb("apply")
    v.add_verb("attack", "fight", "hurt", "injure", "hit")
    v.add_verb("back")
    v.add_verb("blast")
    v.add_verb("blow")
    # board: add "aboard" as synonym for BOARD SHIP/CLIMB ABOARD
    v.add_verb("board", "aboard")
    v.add_verb("brush", "clean")
    v.add_verb("burn", "incinerate", "ignite")
    # buy: new canonical for BUY DRINK / ORDER FOOD / RENT ROOM
    v.add_verb("buy", "order", "purchase", "rent")
    v.add_verb("cast", "incant", "chant", "spell")  # takes incant/chant/spell from exorcise
    v.add_verb("clear")                             # CLEAR BONES / CLEAR DRAIN
    v.add_verb("climb", "sit")
    v.add_verb("challenge", "wrestle")              # CHALLENGE LYNDS
    v.add_verb("pay")                               # PAY BOGGART
    v.add_verb("disarm", "defuse")                  # DISARM PLATE
    v.add_verb("close")
    v.add_verb("command")
    v.add_verb("count")
    v.add_verb("cross", "ford")
    v.add_verb("curse", "shit", "fuck", "damn")
    v.add_verb("cut", "slice", "pierce")
    v.add_verb("deflate")
    v.add_verb("destroy", "damage", "break", "block", "smash")
    v.add_verb("dig")
    v.add_verb("disembark")
    v.add_verb("disenchant")
    v.add_verb("drink", "imbibe", "swallow")
    v.add_verb("drive")                             # DRIVE STAKE INTO WEREWOLF
    v.add_verb("drop")
    v.add_verb("dock")                              # DOCK (return ship to harbor)
    v.add_verb("eat", "consume", "taste", "bite")
    v.add_verb("enchant")
    v.add_verb("enter")
    v.add_verb("exit")
    v.add_verb("examine", "describe", "what", "whats")
    v.add_verb("exorcise", "banish", "begone")      # "drive" is its own verb
    v.add_verb("extinguish", "douse")
    v.add_verb("fill")
    v.add_verb("find", "where", "seek", "see")
    v.add_verb("fish", "angle")                     # FISH at Roundabout Pond
    v.add_verb("follow", "pursue", "chase", "come")
    v.add_verb("give", "donate", "offer", "feed", "hand")
    v.add_verb("hello", "hi")
    v.add_verb("inflate", "inflat")
    v.add_verb("jump", "leap", "dive")
    v.add_verb("kick", "taunt")
    v.add_verb("kill", "murder", "slay", "dispatch")
    v.add_verb("kiss")
    v.add_verb("knock", "rap")
    v.add_verb("lean")
    v.add_verb("leave")
    v.add_verb("light")
    v.add_verb("listen")
    v.add_verb("load")                              # LOAD STONE ONTO CART
    v.add_verb("lock")
    v.add_verb("look", "l", "stare", "gaze")
    v.add_verb("lower")
    v.add_verb("lubricate", "oil", "grease")
    v.add_verb("make")
    v.add_verb("melt", "liquify")
    v.add_verb("move")
    v.add_verb("mumble", "sigh")
    v.add_verb("open")
    v.add_verb("pick")
    v.add_verb("play")
    v.add_verb("plug", "glue", "patch", "repair", "fix")
    v.add_verb("poke")
    v.add_verb("pour", "spill")
    v.add_verb("pray")
    v.add_verb("pry", "lever", "jimmy")             # PRY DOOR (crowbar)
    v.add_verb("pull", "tug", "yank")
    v.add_verb("pump")
    v.add_verb("push", "press")
    v.add_verb("put", "stuff", "insert", "place", "hide")
    v.add_verb("raise", "lift")
    v.add_verb("read", "skim")
    v.add_verb("repent")
    v.add_verb("rest")                              # REST spell (Level 6+)
    v.add_verb("ring", "peal")
    v.add_verb("roll")
    v.add_verb("rub", "touch", "feel", "pat", "pet")
    # sail: new canonical; set is NOT aliased here (prevents SET SAIL ambiguity)
    v.add_verb("sail")                              # SAIL / SAIL EAST / SET SAIL
    v.add_verb("say")
    v.add_verb("search")
    v.add_verb("shake")
    v.add_verb("skip", "hop")
    v.add_verb("slide")
    v.add_verb("smell", "sniff")
    v.add_verb("spin")
    v.add_verb("spray")
    v.add_verb("squeeze")
    v.add_verb("stab")
    v.add_verb("stand")
    v.add_verb("stay")
    v.add_verb("strike")
    v.add_verb("swap", "trade", "exchange")         # SWAP IDOL WITH SALT
    v.add_verb("swim", "bathe", "wade")
    v.add_verb("swing", "thrust")
    v.add_verb("take", "get", "hold", "carry", "grab", "catch")
    v.add_verb("remove", "doff")                    # REMOVE GLASSES (take off worn item)
    v.add_verb("talk")
    v.add_verb("tell", "ask")
    v.add_verb("throw", "hurl", "chuck", "toss")
    v.add_verb("tie", "fasten", "secure", "attach")
    v.add_verb("tip")                               # TIP MAY [#]
    # turn: "set" removed — SET SAIL must route through "sail" canonical
    v.add_verb("turn", "flip", "shut")
    v.add_verb("unlock")
    v.add_verb("unload", "return")                 # UNLOAD STONE (Quest 32)
    v.add_verb("untie", "free", "release", "unfasten", "unattach", "unhook")
    v.add_verb("use")                               # USE PORTCULLIS BAR
    v.add_verb("wait", "z")
    v.add_verb("wake", "awake", "surprise", "startle")
    v.add_verb("walk", "go", "run", "proceed", "step")
    v.add_verb("wave", "brandish")
    v.add_verb("wear")
    v.add_verb("wind")
    v.add_verb("wish")
    v.add_verb("yell", "scream", "shout")

    return v
