#!/usr/bin/env python3
import sys

def mapper():
    print("Mapper started", file=sys.stderr)
    for line in sys.stdin:
        line = line.strip()
        if not line or line.startswith("Summons Number"):
            print(f"Skipping line: {line}", file=sys.stderr)
            continue
        columns = line.split(',')
        if len(columns) > 20:  # Ensuring there are enough columns
            violation_county = columns[21].strip()  # Index for violation county
            vehicle_make = columns[7].strip()       # Index for vehicle make
            if violation_county and vehicle_make:
                print(f"{violation_county}\t{vehicle_make}")
            else:
                print(f"Missing data - County: {violation_county}, Make: {vehicle_make}", file=sys.stderr)
        else:
            print(f"Skipping line with insufficient columns: {line}", file=sys.stderr)
    print("Mapper finished", file=sys.stderr)

if __name__ == "__main__":
    mapper()
