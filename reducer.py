#!/usr/bin/env python3
import sys
from collections import defaultdict

def reducer():
    print("Reducer started", file=sys.stderr)
    current_county = None
    county_make_count = defaultdict(int)

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            county, make = line.split('\t')
        except ValueError:
            print(f"Skipping line with incorrect format: {line}", file=sys.stderr)
            continue
        
        if county != current_county:
            if current_county:
                most_frequent_make = max(county_make_count, key=county_make_count.get)
                print(f"{current_county}\t{most_frequent_make}\t{county_make_count[most_frequent_make]}")
            current_county = county
            county_make_count = defaultdict(int)
        
        county_make_count[make] += 1
    
    if current_county:
        most_frequent_make = max(county_make_count, key=county_make_count.get)
        print(f"{current_county}\t{most_frequent_make}\t{county_make_count[most_frequent_make]}")

    print("Reducer finished", file=sys.stderr)

if __name__ == "__main__":
    reducer()
