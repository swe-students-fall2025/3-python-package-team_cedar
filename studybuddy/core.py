import random

# Core data
_TIPS = {
    "math": [
        "If it’s too complex, assume x = 0. Problem solved.",
        "Numbers never lie, but you might when asked if you understand them.",
    ],
    "history": [
        "If you forget the date, just say 'around that time.'",
        "History repeats itself. So if you fail this exam, you’ll get another chance.",
    ],
    "physics": [
        "If it moves, it’s probably physics. If not, hit it again.",
        "Remember: every action has an equal and opposite procrastination.",
    ],
}



# Functions
def _choose(lst, rnd):
    return lst[rnd.randrange(len(lst))]

def study_tip(topic: str = "math", mood: str = "chaotic", seed: int | None = None) -> str:
    """Return a humorous study tip."""
    rnd = random.Random(seed)
    tips = _TIPS.get(topic, _TIPS["math"])
    return _choose(tips, rnd)
