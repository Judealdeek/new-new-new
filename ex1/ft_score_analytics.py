import sys


def ft_score_analytics():
    args = sys.argv
    scores = []
    print("=== Player Score Anaylytics ===")
    for i in range(1, len(args)):
        try:
            score = int(args[i])
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter:  '{args[i]}'")
    if len(scores) == 0:
        print(
                "No Scores provided.  Usage:  "
                f"python3 {args[0]} <score1> <score2> ..."
                )
        return
    print("Scores processed:  ", scores)
    print("Total players:  ", len(scores))
    print("Total score:  ", sum(scores))
    print("Average score:  ", sum(scores) / len(scores))
    print("High score:  ", max(scores))
    print("Low score:  ", min(scores))
    print("Score range:  ", max(scores) - min(scores))


ft_score_analytics()
