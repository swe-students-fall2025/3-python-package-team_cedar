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

_MOTIVATIONS = {
    "sarcastic": [
        "Remember: diamonds are made under pressure. So start panicking.",
        "Dream big, nap often.",
        "You can do anything! Except maybe that.",
    ],
    "genuine": [
        "You’ve got this! Probably. Maybe. Let’s hope.",
        "One page at a time — just keep going.",
        "Even small progress counts. Keep at it.",
    ],
}

_EXCUSES = {
    "homework": [
        "My cat deleted my assignment. She’s learning cybersecurity.",
        "Google Docs went into witness protection.",
    ],
    "late": [
        "My Wi-Fi connected to another dimension.",
        "I was stuck in traffic... on the information highway.",
    ],
    "exam": [
        "I didn’t fail. I just found 99 ways that didn’t work.",
        "The test was multiple guess, and I guessed wrong multiple times.",
    ],
}

_STEPS = [
    "Make coffee.",
    "Open your notes.",
    "Panic productively for 90 minutes.",
    "Reward yourself with a snack break.",
    "Google half the material.",
]

# Functions
def _choose(lst, rnd):
    return lst[rnd.randrange(len(lst))]

def study_tip(topic: str = "math", mood: str = "chaotic", seed: int | None = None) -> str:
    """Return a humorous study tip."""
    rnd = random.Random(seed)
    tips = _TIPS.get(topic, _TIPS["math"])
    return _choose(tips, rnd)

def motivate(style: str = "sarcastic", seed: int | None = None) -> str:
    """Return a motivational or sarcastic message."""
    rnd = random.Random(seed)
    msgs = _MOTIVATIONS.get(style, _MOTIVATIONS["sarcastic"])
    return _choose(msgs, rnd)

def excuse(reason: str = "homework", seed: int | None = None) -> str:
    """Return a funny excuse for school mishaps."""
    rnd = random.Random(seed)
    excuses = _EXCUSES.get(reason, _EXCUSES["homework"])
    return _choose(excuses, rnd)

def study_plan(hours: int = 3, caffeine_level: str = "high", seed: int | None = None) -> list[str]:
    """Return a list of 'study plan' steps."""
    rnd = random.Random(seed)
    plan = []
    for i in range(min(hours, 5)):
        step = _choose(_STEPS, rnd)
        if caffeine_level == "high" and "coffee" not in step.lower():
            step = "Drink more coffee. " + step
        plan.append(f"Step {i+1}: {step}")
    return plan