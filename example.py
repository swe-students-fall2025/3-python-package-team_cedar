from studybuddy import study_tip, motivate, excuse, study_plan, allocate_time


def main():
    print("=== StudyBuddy Demo ===")
    print("\nStudy Tip:", study_tip("physics", "chaotic"))
    print("\nMotivation:", motivate("sarcastic"))
    print("\nExcuse:", excuse("homework"))
    print("\nStudy Plan:")
    for step in study_plan(3, "high", seed=4):
        print(" -", step)
    print("\n")
    print(allocate_time({"Math-UA 101": 3, "CSCI-UA 480": 2, "CSCI-UA 467": 1}, total_minutes=125, min_chunk=5))

        
if __name__ == "__main__":
    main()
