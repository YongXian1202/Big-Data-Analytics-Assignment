# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:16:20 2024

@author: yongx
"""
import csv
import time
from collections import defaultdict

def process_file(input_file):
    print("Processing file...")

    # Start counting time
    start_time = time.time()

    # Process input and collect intermediate key-value pairs
    intermediate_data = []

    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip the header row
        for line in reader:
            line = [col.strip() for col in line]
            if not line:
                print(f"Skipping empty line")
                continue
            
            if len(line) > 20:  # Ensuring there are enough columns
                violation_county = line[21]  # Index for violation county
                vehicle_make = line[7]       # Index for vehicle make
                if violation_county and vehicle_make:
                    intermediate_data.append((violation_county, vehicle_make))
                else:
                    print(f"Missing data - County: {violation_county}, Make: {vehicle_make}")
            else:
                print(f"Skipping line with insufficient columns: {line}")

    # Aggregate data
    print("Aggregating data...")
    county_make_count = defaultdict(lambda: defaultdict(int))

    for county, make in intermediate_data:
        county_make_count[county][make] += 1

    # Output the results
    print("Outputting results...")
    results = []
    for county in county_make_count:
        most_frequent_make = max(county_make_count[county], key=county_make_count[county].get)
        results.append((county, most_frequent_make, county_make_count[county][most_frequent_make]))

    # End counting time
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")
    
    return results

if __name__ == "__main__":
    # Read file
    input_file = r'C:\Users\yongx\.spyder-py3\Parking_Violations_Issued_-_Fiscal_Year_2017.csv'
    results = process_file(input_file)
    
    # Print results
    for county, make, count in sorted(results):
        print(f"{county}\t{make}\t{count}")

