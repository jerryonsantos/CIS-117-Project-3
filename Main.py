
# CIS-117 Lab4
# This python model reads the csv file country_full.csv containing
# a list of countries and regions and splits the countries into different csv files
# per region
# Jeremiah David


import csv

europe_countries = []
asia_countries = []
africa_countries = []
americas_countries = []
oceania_countries = []

with open('country_full.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)

    try:
        with open('country_full.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                try:
                    region = row['region']
                    country_info = {'name': row['name'], 'region': region}
                    if region == 'Europe':
                        europe_countries.append(country_info)
                    elif region == 'Asia':
                        asia_countries.append(country_info)
                    elif region == 'Africa':
                        africa_countries.append(country_info)
                    elif region == 'Americas':
                        americas_countries.append(country_info)
                    elif region == 'Oceania':
                        oceania_countries.append(country_info)
                except KeyError as e:
                    print(f"Missing expected key in row: {e}")
    except FileNotFoundError:
        print("Error: 'country_full.csv' file not found.")
    except Exception as e:
        print(f"Unexpected error while reading CSV: {e}")




try:
    with open('Europe.csv', 'w', newline='') as europe_file:
        if europe_countries:
            try:
                fieldnames = ['name', 'region']
                writer = csv.DictWriter(europe_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(europe_countries)
            except Exception as e:
                print(f"Error writing to Europe.csv: {e}")
except Exception as e:
    print(f"Failed to open Europe.csv for writing: {e}")


try:
    with open('Asia.csv', 'w', newline='') as asia_file:
        if asia_countries:
            try:
                fieldnames = ['name', 'region']
                writer = csv.DictWriter(asia_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(asia_countries)
            except Exception as e:
                print(f"Error writing to Asia.csv: {e}")
except Exception as e:
    print(f"Failed to open Asia.csv for writing: {e}")


try:
    with open('Africa.csv', 'w', newline='') as africa_file:
        if africa_countries:
            try:
                fieldnames = ['name', 'region']
                writer = csv.DictWriter(africa_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(africa_countries)
            except Exception as e:
                print(f"Error writing to Africa.csv: {e}")
except Exception as e:
    print(f"Failed to open Africa.csv for writing: {e}")


try:
    with open('Americas.csv', 'w', newline='') as americas_file:
        if americas_countries:
            try:
                fieldnames = ['name', 'region']
                writer = csv.DictWriter(americas_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(americas_countries)
            except Exception as e:
                print(f"Error writing to Americas.csv: {e}")
except Exception as e:
    print(f"Failed to open Americas.csv for writing: {e}")


try:
    with open('Oceania.csv', 'w', newline='') as oceania_file:
        if oceania_countries:
            try:
                fieldnames = ['name', 'region']
                writer = csv.DictWriter(oceania_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(oceania_countries)
            except Exception as e:
                print(f"Error writing to Oceania.csv: {e}")
except Exception as e:
    print(f"Failed to open Oceania.csv for writing: {e}")





