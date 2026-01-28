import sys

try:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    elif len(sys.argv) > 1:
        new_list = []
        for item in sys.argv[1:]:
            new_list += [int(item)]
        arg_count = len(new_list)
        score_sum = sum(new_list)
        Average = score_sum / arg_count
        max_score = max(new_list)
        min_score = min(new_list)
        score_range = max_score - min_score
        print(f"Total players: {arg_count}")
        print(f"Total score: {score_sum}")
        print(f"Average score: {Average}")
        print(f"High score: {max_score}")
        print(f"Low score: {min_score}")
        print(f"Score range: {score_range}")
except ValueError as e:
    print(f"ValueError = {e}")
