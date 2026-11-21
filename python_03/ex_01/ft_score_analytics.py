#!/usr/bin/env python3


import sys

def check_invalid(args: str):
    if int(args):
        return
    else:
        raise ValueError(f"Invalid parameter: {args[i]}")

def parse_valid(lst: list)-> int:
    args_count: int = len(lst) - 1
    valid_count = 0
    i: int = 0

    while i < args_count:
        try:
            check_invalid(lst[i + 1])
            valid_count += 1
        except ValueError as e:
            print(f"{e}")
        i += 1
    return valid_count


if __name__ == "__main__":
    scores: list = sys.argv

    args_count = len(scores) - 1
    if args_count == 0:
        print("No scores provided." \
        " Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        valid_count = parse_valid(scores)
        if valid_count == 0:
            print("No scores provided." \
            " Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        else:
            valid_list: list = [None] * valid_count
            i: int = 0
            j: int = 0
            while i < args_count:
                try:
                    num = int(scores[i + 1])
                    if num :
                        valid_list[j] = num
                        j += 1
                except:
                    pass
                i += 1
            print(f"Score processed: {valid_list}")
            print(f"Total players: {valid_count}")
            print(f"Total score: {sum(valid_list)}")
            print(f"Average score: {sum(valid_list) / valid_count}")
            print(f"High score: {max(valid_list)}")
            print(f"Low score {min(valid_list)}")
