import random
from typing import List, Optional

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


_ROASTS = [
    "Your study habits are like Wi-Fi at a coffee shop — weak and unreliable.",
    "If procrastination was a sport, you'd be an Olympian.",
    "You're doing amazing… at finding new ways to avoid studying.",
    "Please dont tell me your actually trying??",
]


_COMPLIMENTS = [
    "You're sharper than your pencil!",
    "Brains and beauty — unfair combo.",
    "You make studying look… almost cool.",
    "Wow, is this what a natural genius looks like?",
    "we need to talk about how amazing you are",
]

_BREAKS = [
    "Stretch like you’re reaching for better grades.",
    "Take a water break — hydration is brain fuel.",
    "Do nothing for 5 minutes. You’ve earned it.",
]


# --- Playlists ---
_PLAYLISTS = {
    "focus": [
        "Chillhop Essentials – Instrumental beats",
        "Deep Focus – steady no-lyrics electronica",
        "Coding Mode – subtle pulses, low distraction",
        "Brain Food – downtempo, minimal vocals",
        "Lo-Fi Beats – mellow study loops",
    ],
    "lofi": [
        "lofi hip hop radio – beats to relax/study to",
        "Late Night Lo-Fi – rainy window vibes",
        "Cafe Lofi – warm, cozy instrumentals",
        "Lo-Fi Piano – soft keys + vinyl crackle",
        "Study & Sleep – ultra-gentle loops",
    ],
}

_VALID_CAFFEINE = {"low", "high"}

# internal helpers
def _rng(seed: Optional[int]) -> random.Random:
    """Private RNG factory to keep seeding consistent everywhere."""
    return random.Random(seed)

def _choose(lst: List[str], rnd: random.Random) -> str:
    """Safe random chooser (assumes non-empty list)."""
    return lst[rnd.randrange(len(lst))]

def _weighted_choice(options: List[str], weights: List[float], rnd: random.Random) -> str:
    """Safe weighted choice with basic validation."""
    if not options:
        raise ValueError("No options provided for weighted choice.")
    if len(options) != len(weights):
        raise ValueError("Options and weights must be the same length.")
    if all(w == 0 for w in weights):
        # Fallback to uniform if all weights are zero
        return _choose(options, rnd)
    return rnd.choices(options, weights=weights, k=1)[0]

# public interpretation
def list_topics() -> List[str]:
    """Return available topics for study_tip()."""
    return sorted(_TIPS.keys())

def list_styles() -> List[str]:
    """Return available styles for motivate()."""
    return sorted(_MOTIVATIONS.keys()) + ["mixed"]

def list_reasons() -> List[str]:
    """Return available reasons for excuse()."""
    return sorted(_EXCUSES.keys())

def list_vibes() -> list[str]:
    """Return available vibes for playlist()."""
    return sorted(_PLAYLISTS.keys())



# public functions API


def study_tip(topic: str = "math", mood: str = "chaotic", seed: Optional[int] = None) -> str:
    """
    Return a humorous study tip.
    Unknown topics default to 'math'.
    """
    rnd = _rng(seed)
    tips = _TIPS.get(topic, _TIPS["math"])
    return _choose(tips, rnd)

def motivate(style: str = "mixed", seed: Optional[int] = None) -> str:
    """
    Return a motivational message.
    style: 'sarcastic' | 'genuine' | 'mixed'
    """
    rnd = _rng(seed)
    if style == "mixed":
        options = _MOTIVATIONS["sarcastic"] + _MOTIVATIONS["genuine"]
        weights = [0.7] * len(_MOTIVATIONS["sarcastic"]) + [0.3] * len(_MOTIVATIONS["genuine"])
        return _weighted_choice(options, weights, rnd)
    msgs = _MOTIVATIONS.get(style, _MOTIVATIONS["sarcastic"])
    return _choose(msgs, rnd)

def excuse(reason: str = "homework", seed: Optional[int] = None) -> str:
    """
    Return a funny excuse for academic mishaps.
    Unknown reasons default to 'homework'.
    """
    rnd = _rng(seed)
    excuses = _EXCUSES.get(reason, _EXCUSES["homework"])
    return _choose(excuses, rnd)

def study_plan(hours: int = 3, caffeine_level: str = "high", seed: Optional[int] = None) -> List[str]:
    """
    Return a list of study plan steps.
    - hours clamped to [1, 5]
    - caffeine_level in {'low','high'} (defaults to 'high' if unknown)
    """
    rnd = _rng(seed)
    if hours < 1:
        hours = 1
    if hours > 5:
        hours = 5
    if caffeine_level not in _VALID_CAFFEINE:
        caffeine_level = "high"

    plan = []
    for i in range(hours):
        step = _choose(_STEPS, rnd)
        if caffeine_level == "high" and "coffee" not in step.lower():
            step = "Drink more coffee. " + step
        plan.append(f"Step {i + 1}: {step}")
    return plan

def roast(seed: Optional[int] = None) -> str:
    """Serve a light, lovingly savage roast."""
    rnd = _rng(seed)
    return _choose(_ROASTS, rnd)

def compliment(seed: Optional[int] = None) -> str:
    """Give the user a kind compliment."""
    rnd = _rng(seed)
    return _choose(_COMPLIMENTS, rnd)

def break_tip(seed: Optional[int] = None) -> str:
    """Suggest a healthy mini-break."""
    rnd = _rng(seed)
    return _choose(_BREAKS, rnd)

def pomodoro_plan(sessions: int = 3, seed: Optional[int] = None) -> List[str]:
    """
    Build a simple Pomodoro schedule.
    sessions clamped to [1, 8]
    """
    rnd = _rng(seed)
    if sessions < 1:
        sessions = 1
    if sessions > 8:
        sessions = 8

    plan: List[str] = []
    verbs = ["Study hard", "Focus intensely", "Pretend to focus"]
    for i in range(1, sessions + 1):
        work = _choose(verbs, rnd)
        plan.append(f"Pomodoro {i}: {work} for 25 min, then break 5 min.")
    plan.append("Final note: You've earned a long break (and a snack).")
    return plan

def secret(seed: Optional[int] = None) -> str:
    """Easter egg."""
    rnd = _rng(seed)
    return _choose([
        "Secret unlocked: You deserve a nap.",
        "Achievement: Survived another study session!",
        "StudyBuddy secretly believes in you.",
    ], rnd)


def playlist(vibe: str = "focus", n: int = 3, seed: int | None = None) -> list[str]:
    """
    Suggest a study playlist (list of n items) for a given vibe.

    Args:
        vibe: one of list_vibes(); unknown -> 'focus'
        n: number of suggestions (clamped to [1, 10])
        seed: optional seed for reproducibility

    Returns:
        list[str]: n playlist suggestions (may repeat if n > pool size)
    """
    rnd = random.Random(seed)
    if vibe not in _PLAYLISTS:
        vibe = "focus"
    n = max(1, min(10, n))
    pool = _PLAYLISTS[vibe]

    # If the pool is smaller than n, allow repeats; otherwise sample without replacement
    if n <= len(pool):
        return rnd.sample(pool, k=n)
    else:
        return [pool[rnd.randrange(len(pool))] for _ in range(n)]
