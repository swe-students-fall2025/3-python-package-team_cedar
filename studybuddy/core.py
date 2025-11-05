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

_ROASTS = {
    "cs": [
        "Your code is like your dating life - full of bugs and nobody wants to debug it.",
        "You code like you're trying to solve world hunger... one syntax error at a time.",
        "Your algorithm is so inefficient, it makes bubble sort look like a speed demon.",
        "I've seen more organized code in a toddler's finger painting.",
        "Your variable names are more confusing than IKEA instructions.",
    ],
    "math": [
        "Your math skills are so bad, calculators file restraining orders.",
        "You approach equations like they're written in ancient hieroglyphs.",
        "Your algebra is weaker than decaf coffee on a Monday morning.",
        "You solve problems like you're playing mathematical roulette.",
        "Your geometry is so off, even abstract art looks realistic in comparison.",
    ],
    "physics": [
        "Your understanding of physics violates more laws than a parking ticket collector.",
        "You handle momentum like you handle your life - poorly.",
        "Your grasp of gravity is the only thing keeping your grades down.",
        "You treat thermodynamics like it's thermo-optional-amics.",
        "Your physics solutions defy more laws than they follow.",
    ],
}

_BREAK_ACTIVITIES = {
    "stretch": [
        "Do the 'I've been sitting too long' neck roll dance.",
        "Attempt yoga poses that would make a pretzel jealous.",
        "Stretch like a cat who just discovered the concept of flexibility.",
        "Channel your inner flamingo with some one-legged stretches.",
    ],
    "walk": [
        "Take a relaxing walk around your room (or building if you're feeling fancy).",
        "Practice your 'deep in thought' walk around the block.",
        "Walk to the kitchen and contemplate the meaning of snacks.",
        "Do the 'I need fresh air but also Wi-Fi' walk of balance.",
    ],
    "snack": [
        "Fuel up with brain food (chips count as brain food, right?).",
        "Have a philosophical discussion with your refrigerator contents.",
        "Practice portion control by eating one cookie... at a time... repeatedly.",
        "Conduct a scientific taste test of available snacks.",
    ],
}

_PLAYLIST_MOODS = {
    "focus": [
        "Lofi Hip Hop Radio - beats to procrastinate/study to",
        "Classical Music for People Who Think They're Sophisticated",
        "Ambient Sounds That Definitely Won't Put You to Sleep",
    ],
    "energetic": [
        "Upbeat Songs to Make You Feel Productive (Even If You're Not)",
        "High-Energy Tracks for Last-Minute Panic Sessions",
        "Songs That Make Cramming Feel Like a Dance Party",
    ],
    "chill": [
        "Chill vibes only – lo-fi beats to relax to",
        "Relaxing acoustic flow for study focus",
        "Calm music to help you relax and chill out",
    ],
}

_DEADLINE_MESSAGES = {
    "panic": [
        "Time to panic (just a little)! Activate MAXIMUM OVERDRIVE mode!",
        "This is fine. Everything is fine. *nervous laughter*",
        "Remember: pressure makes diamonds... or nervous breakdowns.",
        "It's crunch time! Time to crunch those... study materials.",
    ],
    "funny": [
        "Deadline approaching faster than your motivation to start working!",
        "Time left: {hours} hours. Panic level: Moderate to severe.",
        "Your deadline called - it's running fashionably early.",
        "Breaking news: Local student discovers deadlines don't extend themselves.",
    ],
    "motivational": [
        "You've got this! {hours} hours is plenty of time to work miracles!",
        "Every hour counts - make them work for you!",
        "You're closer to the finish line than you think!",
        "Time to show this deadline who's boss!",
    ],
}

_PEP_TALKS = {
    "wholesome": [
        "Hey {name}, you're doing great! {goal} is totally achievable.",
        "{name}, remember that progress isn't always linear, but you're moving forward!",
        "You've got the determination to reach your goal of {goal}, {name}!",
        "Every small step towards {goal} counts, {name}. Keep it up!",
    ],
    "tough_love": [
        "Listen up {name}, {goal} isn't going to happen by itself!",
        "{name}, stop making excuses and start making progress on {goal}!",
        "You want to achieve {goal}? Then quit talking and start doing, {name}!",
        "Reality check, {name}: {goal} requires actual work, not just wishful thinking!",
    ],
    "funny": [
        "{name}, your goal of {goal} is calling... it wants to know if you're still friends.",
        "Hey {name}, {goal} just texted - it's wondering when you'll take it seriously!",
        "{name}, your future self is judging your current commitment to {goal}.",
        "Breaking news {name}: {goal} is still waiting for you to show up!",
    ],
}

_AFFIRMATIONS = [
    "You are 100% capable of finishing this assignment (eventually).",
    "Progress > perfection.",
    "You’re not behind — you’re just on your own timeline.",
    "Even one line of code counts as productivity!",
    "You’re basically the main character of this study session."
]

_CHALLENGES = [
    "Study 10 pages without checking your phone.",
    "Summarize the last topic in one sentence.",
    "Do a 5-minute rapid-fire recall session.",
    "Write a haiku about your subject.",
    "Quiz yourself out loud — bonus points if you sound confident."
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
    "hype": [
        "Beast Mode – high-energy gym bangers",
        "EDM Bangers – tempo > productivity (maybe)",
        "Trap Motivation – bass + bravado",
        "Pop Power – hooks that keep you awake",
        "Drill & Focus(?) – questionable, but effective",
    ],
    "classical": [
        "Bach: The Well-Tempered Clavier",
        "Mozart for Studying – piano concertos",
        "Debussy & Satie – airy impressionism",
        "Baroque for Focus – steady rhythms",
        "Ludovico Einaudi – modern minimal piano",
    ],
    "ambient": [
        "Brian Eno – Music for Airports",
        "Max Richter – Sleep (selected)",
        "Carbon Based Lifeforms – soft space ambient",
        "Nils Frahm – solo ambient piano",
        "Rain & Brown Noise – pure background",
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