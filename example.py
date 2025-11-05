from studybuddy import (
    study_tip, motivate, excuse, study_plan, allocate_time,
    roast, break_idea, pomodoro_schedule, study_playlist,
    deadline_reminder, pep_talk, affirmation, challenge
)


def main():
    print("=== StudyBuddy Demo ===")

    print("\n📘 Study Tip:", study_tip("physics", "chaotic"))

    print("\n💬 Motivation:", motivate("sarcastic"))

    print("\n🙈 Excuse:", excuse("homework"))

    print("\n🧠 Study Plan:")
    for step in study_plan(3, "high", seed=4):
        print(" -", step)
    print("\n")


    print("\n Roast:", roast("cs", intensity=7))

    print("\n☕ Break Idea:", break_idea(10, "walk"))

    print("\n⏱️ Pomodoro Schedule:")
    for s in pomodoro_schedule(4):
        print(" -", s)

    print("\n🎧 Study Playlist:")
    for p in study_playlist("focus", 3):
        print(" -", p)

    print("\n⏳ Deadline Reminder:", deadline_reminder(5, "motivational"))

    print("\n💪 Pep Talk:", pep_talk(name="Sean", goal="finish your project", theme="tough_love"))

    print("\n🌈 Affirmation:", affirmation())

    print("\n🎯 Challenge:", challenge())

    print("\n🕒 Time Allocation:")
    print(allocate_time({"Math-UA 101": 3, "CSCI-UA 480": 2, "CSCI-UA 467": 1}, total_minutes=125, min_chunk=5))

        
if __name__ == "__main__":
    main()
