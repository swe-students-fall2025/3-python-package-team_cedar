from studybuddy import study_tip, motivate, excuse, study_plan

def main():
    print("=== StudyBuddy Demo ===")
    print("\nStudy Tip:", study_tip("physics", "chaotic"))
    print("\nMotivation:", motivate("sarcastic"))
    print("\nExcuse:", excuse("homework"))
    print("\nStudy Plan:")
    for step in study_plan(3, "high", seed=4):
        print(" -", step)

        
if __name__ == "__main__":
    main()
