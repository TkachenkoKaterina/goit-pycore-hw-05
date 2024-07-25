import sys
import os
import re
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    parts = line.split(maxsplit=3)
    if len(parts) < 4:
        return {}
    date, time, level, message = parts
    return {
        'date': date,
        'time': time,
        'level': level,
        'message': message
    }

def load_logs(file_path: str) -> list:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    with open(file_path, 'r') as file:
        return [log_entry for line in file if (log_entry := parse_log_line(line.strip()))]

def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return list(filter(lambda log: log['level'].upper() == level, logs))

def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level'].upper()] += 1
    return dict(counts)

def display_log_counts(counts: dict) -> None:
    levels = ['INFO', 'ERROR', 'DEBUG', 'WARNING']
    print(f"{'Level':<10} {'Count':<5}")
    print("-" * 15)
    for level in levels:
        count = counts.get(level, 0)
        print(f"{level:<10} {count:<5}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <logfile> [<level>]")
        sys.exit(1)

    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        logs = load_logs(file_path)
        if filter_level:
            logs = filter_logs_by_level(logs, filter_level)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
