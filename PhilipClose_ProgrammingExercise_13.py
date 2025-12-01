# Write a program (function) to create a database called population_(your initials).
# For ex: population_SM would be my database. Create a table named population with the
# following fields; 1. city, 2. year, 3. population. Choose 10 cities in Florida and
# insert data into the population table for the year 2023.

# Import libraries. matplotlib will need to be downloaded if not already.
import random
import sqlite3
import matplotlib.pyplot as plt

# Define function to create the database and insert initial 2023 population data.
def create_database():

    # Connect to (or create) a SQLite database.
    conn = sqlite3.connect('population_PC.db')
    cursor = conn.cursor()

    # Create the population table if it doesn't already exist.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')

    # Initial population data for 10 Florida cities in 2023.
    florida_cities = {
        'Miami': 450000,
        'Orlando': 310000,
        'Tampa': 400000,
        'Jacksonville': 950000,
        'Tallahassee': 200000,
        'St. Petersburg': 260000,
        'Bradenton': 56000,
        'Sarasota': 60000,
        'Fort Lauderdale': 180000,
        'Gainesville': 140000
    }

    # Insert each city's data into the table.
    for city, population in florida_cities.items():
        cursor.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, 2023, population))

    # Commit changes and close connection.
    conn.commit()
    conn.close()

# Define function to simulate -3 to 6% annual population growth for 20 years at random.
def simulate_population_growth():

    # Connect to the database.
    conn = sqlite3.connect('population_PC.db')
    cursor = conn.cursor()

    # Fetch the initial 2023 population data
    cursor.execute('SELECT city, population FROM population WHERE year = 2023')
    initial_data = cursor.fetchall()

    # Loop through each city and simulate growth for 2024-2043
    for city, population in initial_data:
        current_population = population
        for year in range(2024, 2024 + 20):

            # Calculate new population with -3% to 4% growth at random.
            current_population = float(current_population * random.uniform(0.97, 1.04))

            # Insert the new year's data.
            cursor.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, year, current_population))

    # Commit changes and close connection.
    conn.commit()
    conn.close()

# Define function to plot population growth for a selected city.
def plot_population_growth():

    # List of available cities.
    cities = [
        'Miami', 'Orlando', 'Tampa', 'Jacksonville', 'Tallahassee',
        'St. Petersburg', 'Bradenton', 'Sarasota', 'Fort Lauderdale', 'Gainesville'
    ]

    # Display city options to the user.
    print("Choose a city from the following list:")
    for idx, city in enumerate(cities, start=1):
        print(f"{idx}. {city}")

    # Prompt user to select a city by number.
    try:
        choice = int(input("Enter the number corresponding to the city: "))
        if 1 <= choice <= len(cities):
            selected_city = cities[choice - 1]
        else:
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input.")
        return

    # Connect to the database.
    conn = sqlite3.connect('population_PC.db')
    cursor = conn.cursor()

    # Fetch population data for the selected city.
    cursor.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (selected_city,))
    data = cursor.fetchall()

    # Close the database connection.
    conn.close()

    # Check if data is found and plot.
    if data:
        years = [row[0] for row in data]
        populations = [row[1] for row in data]

        # Plot population growth.
        plt.figure(figsize=(10, 6))
        plt.plot(years, populations, marker='o')
        plt.title(f"Population Growth of {selected_city}")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.grid(True)
        plt.show()
    else:
        print("No data found for the selected city.")

# Define the main function to control the program flow.
def main():

    # Create the database and insert initial data.
    create_database()

    # Simulate population growth for 20 years.
    simulate_population_growth()

    # Plot population growth for the user's selected city.
    plot_population_growth()

# Call main function.
main()