I'll help you create a comprehensive README.md file that meets all the requirements. Based on the document, here's a complete, beautifully-formatted README:

```markdown
# StudyBuddy — Your (Unhelpfully) Helpful Study Companion

![CI](https://github.com/swe-students-fall2025/3-python-package-team_cedar/actions/workflows/ci.yml/badge.svg)

**StudyBuddy** is a lighthearted Python package that adds sarcasm, pep talks, and playful structure to your study routine. It gives you randomized study tips, motivation, excuses, Pomodoro schedules, break ideas, playlists, deadline reminders, and more.

- **PyPI:** https://pypi.org/project/studybuddy/
- **CLI included:** run `studybuddy ...` from your terminal
- **Example app:** [`examples/demo.py`](./examples/demo.py)

---

## Installation

From PyPI (recommended):

```bash
pip install studybuddy
```

From source:

```bash
git clone https://github.com/swe-students-fall2025/3-python-package-team_cedar.git
cd 3-python-package-team_cedar
pip install -e .
```

---

## Quick Start (Import & Use)

```python
from studybuddy import (
    study_tip, motivate, excuse, study_plan,
    roast, break_idea, pomodoro_schedule,
    study_playlist, deadline_reminder, pep_talk
)

print(study_tip("physics", "chaotic", seed=42))
print(motivate("genuine"))
print(excuse("exam", seed=7))
print(study_plan(3, "high", seed=5))

print(roast("cs", intensity=8, seed=3))
print(break_idea(4, "hydrate", seed=2))
print("\n".join(pomodoro_schedule(4, 25, 5, 15)))
print(study_playlist("focus", n=3, seed=9))
print(deadline_reminder(12, tone="firm"))
print(pep_talk("Nicole", "finish project", theme="overachiever", seed=11))
```

---

## CLI Usage

StudyBuddy installs a command-line tool named `studybuddy` that mirrors the Python functions.

### Show help
```bash
studybuddy -h
```

### Run functions from your terminal
```bash
# Tips, motivation, excuses, and plans
studybuddy tip --topic physics --seed 1
studybuddy motivate --style sarcastic
studybuddy excuse --reason exam --seed 4
studybuddy plan --hours 3 --caffeine high --seed 5

# Roasts, breaks, pomodoro
studybuddy roast --topic cs --intensity 8 --seed 3
studybuddy break --minutes 5 --activity walk --seed 2
studybuddy pomodoro --sessions 4 --work 25 --break 5 --long 15

# Playlists, deadlines, and pep talks
studybuddy playlist --mood focus --n 3 --seed 9
studybuddy deadline --hours_left 12 --tone firm
studybuddy pep --name Nicole --goal "finish project" --theme overachiever --seed 11
```

If the CLI doesn't run, try:
```bash
python -m studybuddy.cli pep --name You --goal "study 2h"
```

---

## API Reference (All Functions)

All functions accept an optional `seed` parameter for reproducible randomness.

### `study_tip(topic="math", mood="chaotic", seed=None) -> str`
Returns a humorous study tip for the given topic.
- **Args:** 
  - `topic`: `"math"` | `"physics"` | `"history"` (unknown topics fall back to `"math"`)
  - `mood`: currently unused (for future expansion)
  - `seed`: optional integer for reproducibility

**Example:**
```python
study_tip("physics", "chaotic", seed=1)
```

### `motivate(style="sarcastic", seed=None) -> str`
Returns a motivational or sarcastic message.
- **Args:**
  - `style`: `"sarcastic"` or `"genuine"` (unknown → `"sarcastic"`)
  - `seed`: optional integer for reproducibility

**Example:**
```python
motivate("genuine")
```

### `excuse(reason="homework", seed=None) -> str`
Returns a funny excuse for the situation.
- **Args:**
  - `reason`: `"homework"` | `"late"` | `"exam"` (unknown → `"homework"`)
  - `seed`: optional integer for reproducibility

**Example:**
```python
excuse("exam", seed=7)
```

### `study_plan(hours=3, caffeine_level="high", seed=None) -> list[str]`
Creates a silly study plan, one step per list item.
- **Args:**
  - `hours`: 1–5 (longer values are clamped to 5)
  - `caffeine_level`: `"low"` | `"high"`
  - `seed`: optional integer for reproducibility

**Example:**
```python
study_plan(3, "high", seed=5)
```

### `roast(topic="cs", intensity=5, seed=None) -> str`
Delivers a playful roast for a topic.
- **Args:**
  - `topic`: `"cs"` | `"math"` | `"writing"` (unknown → `"cs"`)
  - `intensity`: 1–10 (controls "spice" level)
  - `seed`: optional integer for reproducibility

**Example:**
```python
roast("cs", intensity=8, seed=3)
```

### `break_idea(minutes=5, activity="stretch", seed=None) -> str`
Suggests a micro-break idea customized by minutes and activity.
- **Args:**
  - `minutes`: number of minutes for the break
  - `activity`: `"stretch"` | `"walk"` | `"hydrate"` (unknown → `"stretch"`)
  - `seed`: optional integer for reproducibility

**Example:**
```python
break_idea(4, "hydrate", seed=2)
```

### `pomodoro_schedule(sessions=4, work_min=25, break_min=5, long_break_min=15) -> list[str]`
Builds a Pomodoro-style schedule; every 4th break is long.
- **Args:**
  - `sessions`: number of work sessions
  - `work_min`: minutes per work session
  - `break_min`: minutes for short breaks
  - `long_break_min`: minutes for long break (every 4th)

**Example:**
```python
pomodoro_schedule(4, 25, 5, 15)
```

### `study_playlist(mood="focus", n=3, seed=None) -> list[str]`
Returns playlist/channel names for a given mood.
- **Args:**
  - `mood`: `"focus"` | `"energy"` | `"calm"` (unknown → `"focus"`)
  - `n`: number of playlists to return
  - `seed`: optional integer for reproducibility

**Example:**
```python
study_playlist("focus", n=3, seed=9)
```

### `deadline_reminder(hours_left, tone="funny") -> str`
Provides a countdown-style reminder before a deadline.
- **Args:**
  - `hours_left`: integer, hours until deadline
  - `tone`: `"funny"` | `"firm"` | `"poetic"`

**Example:**
```python
deadline_reminder(12, tone="firm")
```

### `pep_talk(name="friend", goal="study 2 hours", theme="wholesome", seed=None) -> str`
Gives a short personalized pep talk.
- **Args:**
  - `name`: person's name to address
  - `goal`: the goal to encourage
  - `theme`: `"wholesome"` | `"chaotic"` | `"deadpan"` | `"overachiever"`
  - `seed`: optional integer for reproducibility

**Example:**
```python
pep_talk("Ben", "finish project", "overachiever", seed=11)
```

---

## Example Program

See the complete working example at [`examples/demo.py`](./examples/demo.py):

```python
from studybuddy import (
    study_tip, motivate, excuse, study_plan,
    roast, break_idea, pomodoro_schedule,
    study_playlist, deadline_reminder, pep_talk
)

def main():
    print("Tip:", study_tip("physics", "chaotic", seed=42))
    print("Motivation:", motivate("genuine"))
    print("Excuse:", excuse("exam", seed=7))

    print("\nStudy Plan:")
    for step in study_plan(3, "high", seed=5):
        print(" -", step)

    print("\nRoast:", roast("cs", intensity=8, seed=3))
    print("Break:", break_idea(4, "hydrate", seed=2))

    print("\nPomodoro:")
    print("\n".join(pomodoro_schedule(4, 25, 5, 15)))

    print("\nPlaylist:", study_playlist("focus", n=3, seed=9))
    print("Deadline:", deadline_reminder(12, tone="firm"))
    print("Pep:", pep_talk("Nicole", "finish project", "overachiever", seed=11))

if __name__ == "__main__":
    main()
```

**Run it:**
```bash
python examples/demo.py
```

---

## Contributing

We welcome contributions! Follow this workflow to contribute to the project.

### Set up your development environment

Clone the repository:
```bash
git clone https://github.com/swe-students-fall2025/3-python-package-team_cedar.git
cd 3-python-package-team_cedar
```

Create a virtual environment:
```bash
# Option 1: venv (recommended)
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Option 2: Pipenv
pip install pipenv
pipenv install --dev
pipenv shell
```

Install dependencies:
```bash
pip install -U pip
pip install -e . pytest build twine
```

### Run tests
```bash
pytest -q
```

### Build the package
```bash
python -m build
```

This creates distribution files in the `./dist` directory.

### Publish to PyPI (maintainer only)
```bash
twine upload dist/*
```

### Git workflow for new features

1. Create a feature branch:
```bash
git switch -c feat/your-feature-name
```

2. Make changes and add tests

3. Commit your changes:
```bash
git add -A
git commit -m "feat(core): add your feature description"
```

4. Push to GitHub:
```bash
git push -u origin feat/your-feature-name
```

5. Open a Pull Request on GitHub
6. Request a teammate review
7. After approval, merge into `main`
8. Delete your feature branch

### Git attribution tip
Ensure commits show under your GitHub account:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Use your GitHub-verified email or your `@users.noreply.github.com` email.

---

## Continuous Integration

Every pull request triggers automated testing via GitHub Actions on **Python 3.10** and **3.11**.

The CI badge at the top of this README shows the current build status.

**Workflow file:** [`.github/workflows/ci.yml`](./.github/workflows/ci.yml)

---

## Team Cedar

| Name | GitHub |
|------|--------|
| Nicole Zhang | [@chzzznn](https://github.com/chzzznn) |
| Kylie | [@kylin1209](https://github.com/kylin1209) |


---

## PyPI Package

**https://pypi.org/project/studybuddy/**

---

## License

MIT — do cool things responsibly (and sarcastically). 
```

---
