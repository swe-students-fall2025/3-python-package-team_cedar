import argparse, json
from . import (
    study_tip,
    motivate,
    excuse,
    study_plan,
    roast,
    compliment,
    break_tip,
    pomodoro_plan,
    playlist,
    secret,
    list_topics,
    list_styles,
    list_reasons,
    list_vibes,
)
def main():
    parser = argparse.ArgumentParser(prog="studybuddy", description="StudyBuddy CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # tip
    s = sub.add_parser("tip", help="Get a humorous study tip")
    s.add_argument("--topic", default="math")
    s.add_argument("--seed", type=int)

    # motivate
    s = sub.add_parser("motivate", help="Get motivation: sarcastic | genuine | mixed")
    s.add_argument("--style", default="mixed")
    s.add_argument("--seed", type=int)

    # excuse
    s = sub.add_parser("excuse", help="Get a funny excuse")
    s.add_argument("--reason", default="homework")
    s.add_argument("--seed", type=int)

    # plan
    s = sub.add_parser("plan", help="Generate a study plan")
    s.add_argument("--hours", type=int, default=3)
    s.add_argument("--caffeine", default="high", choices=["low", "high"])
    s.add_argument("--seed", type=int)

    # roast / compliment / break
    s = sub.add_parser("roast", help="Receive a playful roast")
    s.add_argument("--seed", type=int)

    s = sub.add_parser("compliment", help="Receive a kind compliment")
    s.add_argument("--seed", type=int)

    s = sub.add_parser("break", help="Get a mini break idea")
    s.add_argument("--seed", type=int)

    # pomodoro
    s = sub.add_parser("pomodoro", help="Build a Pomodoro plan")
    s.add_argument("--sessions", type=int, default=3)
    s.add_argument("--seed", type=int)

    # playlist
    s = sub.add_parser("playlist", help="Suggest study playlists for a vibe")
    s.add_argument("--vibe", default="focus")
    s.add_argument("-n", "--n", type=int, default=3)
    s.add_argument("--seed", type=int)

    # secret
    s = sub.add_parser("secret", help="Reveal a tiny easter egg")
    s.add_argument("--seed", type=int)

    # lists (discoverability)
    sub.add_parser("list-topics", help="Show valid topics for 'tip'")
    sub.add_parser("list-styles", help="Show valid styles for 'motivate'")
    sub.add_parser("list-reasons", help="Show valid reasons for 'excuse'")
    sub.add_parser("list-vibes", help="Show valid playlist vibes")

    args = parser.parse_args()
 

    if args.cmd == "tip": print(study_tip(args.topic, "chaotic", args.seed))
    elif args.cmd == "motivate": print(motivate(args.style, args.seed))
    elif args.cmd == "excuse": print(excuse(args.reason, args.seed))
    elif args.cmd == "plan": print("\n".join(study_plan(args.hours, args.caffeine, args.seed)))
    elif args.cmd == "roast": print(roast(args.topic, args.intensity, args.seed))
    elif args.cmd == "break": print(break_idea(args.minutes, args.activity, args.seed))
    elif args.cmd == "pomodoro": print("\n".join(pomodoro_schedule(args.sessions, args.work, args.brk, args.long)))
    elif args.cmd == "playlist": print(json.dumps(study_playlist(args.mood, args.n, args.seed)))
    elif args.cmd == "deadline": print(deadline_reminder(args.hours_left, args.tone))
    elif args.cmd == "pep": print(pep_talk(args.name, args.goal, args.theme, args.seed))


