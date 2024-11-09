# Katie Hilliard
# Module 4.2 Assignment

"""Changes made:
1. Added a menu that include high, low, and exit options.
2. Allowed user to select which temperatures to view.
3. Added the plot low temperature option in blue.
4. Enabled program to loop back to the menu after displaying a graph.
5. Added an exit message for the user when 'Exit' is selected. """

import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys

def display_instructions():
    """Display the menu instructions."""
    print("Welcome to the Sitka Weather Data Viewer!")
    print("Please select an option:")
    print("1 - High Temperatures")
    print("2 - Low Temperatures")
    print("3 - Exit")

def plot_temperatures(dates, temperatures, title, color):
    """Plot temperatures based on the provided data."""
    fig, ax = plt.subplot()
    ax.plot(dates, temperatures, c=color)

    # Format plot
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# Load data from CSV
filename = 'stika_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.striptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)

# Main loop
while True:
    display_instructions()
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        # Show high temperatures in red
        plot_temperatures(dates, highs, "Daily High Temperatures - 2018", "red")
    elif choice == '2':
        # Show low temperatures in blue
        plot_temperatures(dates, lows, "Daily Low Temperatures - 2018", "blue")
    elif choice == '3':
        # Exit the program
        print("Thank you for using the Sitka Weather Data Viewer. Goodbye!")
        sys.exit() # Exit the program
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
