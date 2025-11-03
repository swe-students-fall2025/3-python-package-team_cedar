# 🧠 StudyBuddy — Your (Unhelpfully) Helpful Study Companion

![CI](https://github.com/swe-students-fall2025/3-python-package-team_cedar/actions/workflows/ci.yml/badge.svg)

**StudyBuddy** is a lighthearted Python package that adds sarcasm, pep talks, and playful structure to your study routine.  
It gives you randomized study tips, motivation, excuses, Pomodoro schedules, break ideas, playlists, deadline reminders, and more.

- **PyPI:** https://pypi.org/project/studybuddy/
- **CLI included:** run `studybuddy ...` from your terminal
- **Example app:** [`examples/demo.py`](./examples/demo.py) (code below)

---

## 📦 Installation

From PyPI (recommended):
```bash

##  Quick Start (Import & Use)

```python
pip install studybuddy

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
