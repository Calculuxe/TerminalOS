import os
import platform
import random
import math
import pygame
import requests
from bs4 import BeautifulSoup
import datetime
import time
import threading
import pytz
import sys

pygame.mixer.init()

device_name = "Default"

# Define ANSI escape codes for background colors
BACKGROUND_COLORS = {
    "black": "\033[40m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    "light_gray": "\033[47m",
    "reset": "\033[0m"  # Reset to default background color
}

# Play startup sound
def play_startup_sound():
    try:
        pygame.mixer.music.load('C:\\TerminalOS\\screen-20240831-105650.wav')
        pygame.mixer.music.play()
    except pygame.error:
        print("Startup sound file not found. Continuing without sound.")

# Play shutdown sound
def play_shutdown_sound():
    try:
        pygame.mixer.music.load('C:\\TerminalOS\\screen-20240831-112339.wav')
        pygame.mixer.music.play()
    except pygame.error:
        print("Shutdown sound file not found. Continuing without sound.")

def play_alarm_sound():
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(r'C:\TerminalOS\screen-20241026-085510.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except pygame.error:
        print("Alarm sound file not found. Continuing without sound.")
        

def restart():
    print("Restarting TerminalOS...")
    play_shutdown_sound()
    time.sleep(1)
    main()

def shutdown():
    print("Shutting down TerminalOS...")
    play_shutdown_sound()
    time.sleep(5)
    sys.exit()  # Explicitly call the exit function

def other_shutdown():
    print("Shutting down...")
    time.sleep(1)
    exit()

# Function to clear the screen
def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    


def show_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Time: {current_time}")

def alarm_thread(alarm_hour, alarm_minute):
    while True:
        now = datetime.datetime.now()
        if now.hour == alarm_hour and now.minute == alarm_minute:
            print("Alarm! Beep! Beep! Beep!")
            play_alarm_sound()
            break
        time.sleep(10)

def set_alarm():
    try:
        alarm_time = input("Enter alarm time (HH:MM format, 24-hour clock): ")
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        print(f"Alarm set for {alarm_hour:02}:{alarm_minute:02}")
        threading.Thread(target=alarm_thread, args=(alarm_hour, alarm_minute)).start()
    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM format.")

def timer_thread(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up! Beep! Beep! Beep!")
    play_alarm_sound()

def set_timer():
    while True:
        try:
            seconds = int(input("Enter timer duration in seconds: "))
            if seconds <= 0:
                print("Please enter a positive number.")
                continue
            print(f"Timer set for {seconds} seconds.")
            threading.Thread(target=timer_thread, args=(seconds,)).start()
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for seconds.")

def world_clock():
    time_zones = {
        "New York": "America/New_York",
        "Los Angeles": "America/Los_Angeles",
        "Chicago": "America/Chicago",
        "Houston": "America/Chicago",
        "Phoenix": "America/Phoenix",
        "Philadelphia": "America/New_York",
        "San Antonio": "America/Chicago",
        "San Diego": "America/Los_Angeles",
        "Dallas": "America/Chicago",
        "San Jose": "America/Los_Angeles",
        "Austin": "America/Chicago",
        "Jacksonville": "America/New_York",
        "Fort Worth": "America/Chicago",
        "Columbus": "America/New_York",
        "San Francisco": "America/Los_Angeles",
        "Charlotte": "America/New_York",
        "Indianapolis": "America/Indiana/Indianapolis",
        "Seattle": "America/Los_Angeles",
        "Denver": "America/Denver",
        "Washington D.C.": "America/New_York"
    }
    
    print("\nWorld Clock")
    print("Choose a city to see the current time:")
    
    for city in time_zones.keys():
        print(city)

    choice = input("Enter city name: ")

    if choice in time_zones:
        timezone = pytz.timezone(time_zones[choice])
        current_time = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current time in {choice}: {current_time}")
    else:
        print("Invalid city. Please choose from the list.")

def clock_app():
    while True:
        print("\nClock and Alarm App")
        print("1. Show Current Time")
        print("2. Set Alarm")
        print("3. Set Timer")
        print("4. World Clock")
        print("5. Exit")
        
        choice = input("> ")

        if choice == "1":
            show_time()
        elif choice == "2":
            set_alarm()
        elif choice == "3":
            set_timer()
        elif choice == "4":
            world_clock()
        elif choice == "5":
            print("Exiting Clock and Alarm App.")
            break
        else:
            print("Invalid option. Please try again.")

def change_background_color():
    print("Available background colors: black, red, green, yellow, blue, magenta, cyan, light_gray")
    color = input("Enter the background color you want: ").strip().lower()
    if color in BACKGROUND_COLORS:
        print(BACKGROUND_COLORS[color], end='')  # Set the background color
        clear_screen()
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Applying Changes...")
        print("Done!")
        clear_screen()
    else:
        print("Invalid color! Using default background.")
        
# Initialize device_name at the top if it's not already done elsewhere
device_name = "Default Device Name"  # Change this to your default device name

def check_for_updates():
    print("The TerminalOS Update Tool has been temporarily shut down.")

def utilities():
    while True:
        try:
            print("---Welcome to Utilities. Please Select an option.---")
            print("--Options--")
            print("About System: 'About' ")
            print("General: 'General' ")
            print("Advanced: 'Advanced' ")
            print("Exit: 'Exit' ")
            setting_option = input("Choose: ")

            if setting_option == "About":
                print("--About Your System--")
                print("Version: TerminalOS 1.0 Build 2411.07 MU04")
                print("Release Channel: Stable/Broad")
                print("This is the fourth minor update for TerminalOS made after release and includes rebranding..")

            elif setting_option == "General":
                print("--General--")
                print("-Options-")
                print("Device Name: 'Name' ")
                print("System update: 'Update' ")
                print("Type 'Back' to go back.")
                general_option = input("Choose: ")

                if general_option == "Name":
                    device_name = "Default"
                    print("Your current device name is", device_name, ". Change? Y/N.")
                    change_name = input("").strip().upper()  # Normalize input to uppercase for comparison
                    if change_name == "Y":
                        device_name = input("Enter your new device name: ")
                    elif change_name == "N":
                        print("Ok, Going back.")
                        return
                    else:
                        print("Not valid. Choosing no.")
                        return

                elif general_option == "Update":
                    check_for_updates()

                elif general_option == "Back":
                    return   

            elif setting_option == "Advanced":
                print("Warning. These settings are advanced and can break TerminalOS.")
                print("--Advanced--")
                print("-Options-")
                print("Reset TerminalOS: 'Reset' ")
                print("Go back: 'Back' ")
                adv_option = input("Choose an option: ")

                if adv_option == "Reset":
                    file_path = 'C:\\TerminalOS\\first_use.txt'
                    try:
                        os.remove(file_path)
                        print(f"TerminalOS has reset. Restarting...")
                        restart()  # Assuming restart is a defined function
                    except FileNotFoundError:
                        print(f"{file_path} does not exist.")
                    except PermissionError:
                        print(f"Permission denied: cannot reset TerminalOS. Delete the first_use.txt manually using a file explorer.")
                    except Exception as e:
                        print(f"An error occurred while resetting: {e}")

                elif adv_option == "Back":
                    return
                else:
                    print("Not a valid option")
                    
            elif setting_option == "Exit":
                break

            else:
                print("Not a valid option")
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            

# Search Engine functionality
def search_duckduckgo(query):
    url = f"https://duckduckgo.com/html/?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching search results: {e}")
        return []

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        search_results = soup.find_all('a', class_='result__a', href=True)

        if not search_results:
            print("No search results found.")
        else:
            for link in search_results:
                title = link.get_text()
                href = link['href']
                results.append((title, href))
        return results

    except Exception as e:
        print(f"Error parsing search results: {e}")
        return []

def display_results(results):
    if not results:
        print("No results found.")
        return

    print("\nSearch Results:\n")
    for idx, (title, href) in enumerate(results):
        print(f"{idx + 1}. {title}")
        print(href)
        print()

def search():
    while True:
        query = input("Enter search query (type 'exit' to quit, or 'Version' to see the version.): ")
        if query.lower() == 'exit':
            break
        elif query == "Version":
            print("Calculuxe Power Search v1.0")

        search_results = search_duckduckgo(query)
        display_results(search_results)

# Weather Functionality
def get_weather(city_name):
    API_KEY = "055293b6b887a090db927d0afb13421f"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    try:
        complete_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp_celsius = main["temp"]
            temp_fahrenheit = (temp_celsius * 9/5) + 32
            humidity = main["humidity"]
            weather_info = (f"\nWeather in {city_name.capitalize()}:\n"
                            f"Temperature: {temp_celsius}°C / {temp_fahrenheit}°F\n"
                            f"Description: {weather_desc}\n"
                            f"Humidity: {humidity}%\n")
        else:
            weather_info = "\nCity not found.\n"
    except Exception as e:
        weather_info = "\nError fetching weather data.\n"

    return weather_info

def mainw():
    print("Welcome to the Weather Terminal!")
    while True:
        city_name = input("Enter city name (or type 'exit' to quit): ").strip()
        if city_name.lower() == 'exit':
            break
        weather_info = get_weather(city_name)
        print(weather_info)

# Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Undefined" if b == 0 else a / b

def square(a):
    return a ** 2

def square_root(a):
    return "Undefined" if a < 0 else math.sqrt(a)

def modulus(a, b):
    return "Undefined (cannot divide by zero)" if b == 0 else a % b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculator():
    print("\n--- Welcome to the Calculator! ---")
    print("Type 'Back' to return to the main menu.")
    
    while True:
        operation = input("\nChoose an operation (Addition, Subtraction, Multiplication, Division, Squaring, Square Root, Modulus) or type 'Back' to go back\n> ")
        
        if operation.lower() == "back":
            return
        
        if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Modulus"]:
            a = get_number('Enter 1st number: ')
            b = get_number('Enter 2nd number: ')

        if operation == "Addition":
            print(f'Result: {add(a, b)}')
        elif operation == "Subtraction":
            print(f'Result: {subtract(a, b)}')
        elif operation == "Multiplication":
            print(f'Result: {multiply(a, b)}')
        elif operation == "Division":
            print(f'Result: {divide(a, b)}')
        elif operation == "Modulus":
            print(f'Result: {modulus(a, b)}')
        elif operation == "Squaring":
            a = get_number('Enter a number: ')
            print(f'Result: {square(a)}')
        elif operation == "Square Root":
            a = get_number('Enter a number: ')
            print(f'Result: {square_root(a)}')
        else:
            print("Invalid operation! Please try again.")
def filesearch():
    import os

def list_files(directory):
    try:
        files = os.listdir(directory)
        print(f"\nContents of '{directory}':")
        for file in files:
            print(file)
    except PermissionError:
        print("Permission denied: Unable to access this directory.")
    except FileNotFoundError:
        print("Directory not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def change_directory(current_dir):
    new_dir = input("Enter the directory you want to navigate to: ")
    # Handle relative and absolute paths
    if os.path.isdir(new_dir):
        return new_dir
    else:
        print("Invalid directory. Staying in the current directory.")
        return current_dir

def file_explorer():
    current_dir = os.getcwd()  # Start in the current working directory
    while True:
        list_files(current_dir)
        command = input("\nType 'cd' to change directory, 'exit' to quit: ").strip().lower()
        if command == 'cd':
            current_dir = change_directory(current_dir)
        elif command == 'exit':
            print("Exiting the file explorer.")
            break
        else:
            print("Invalid command. Please type 'cd' or 'exit'.")

if __name__ == "__maine__":
    file_explorer()


# Worm Game
def worm_game():
    print("\n--- Welcome to Whack a Worm! ---")
    print("Choose a position (1-5) to whack the worm before it disappears.")
    positions = ["1", "2", "3", "4", "5"]
    score = 0
    rounds = 5
    
    for _ in range(rounds):
        worm_position = random.choice(positions)
        print(f"\nRound {_ + 1}/{rounds}: Worm appears in position {worm_position}")

        start_time = time.time()
        player_guess = input("Choose a position (1, 2, 3, 4, 5): ")

        if player_guess == worm_position:
            reaction_time = time.time() - start_time
            if reaction_time <= 2:
                print(f"Whack! You got it in {reaction_time:.2f} seconds!")
                score += 1
            else:
                print("Too slow! Worm disappeared.")
        else:
            print(f"Missed! Worm was at position {worm_position}.")

    print(f"\nGame over! Final score: {score}/{rounds}")

# Text Editor
# Text Editor with error handling
def text_editor():
    print("\n--- Welcome to the Simple Text Editor! ---")
    print("You can create, view, and edit text files.")
    print("Type 'SAVE' on a new line to save your work.\n")

    while True:
        print("1. Create new file")
        print("2. View a file")
        print("3. Edit an existing file")
        print("4. Exit text editor")

        choice = input("> ")

        if choice == "1":
            filename = input("Enter new file name: ")
            if os.path.exists(filename):
                print("File already exists!")
            else:
                try:
                    with open(filename, 'w') as f:
                        print("Enter text (type 'SAVE' to save):")
                        while True:
                            line = input()
                            if line == "SAVE":
                                break
                            f.write(line + "\n")
                    print(f"File '{filename}' created.")
                except IOError as e:
                    print(f"Error creating file '{filename}': {e}")

        elif choice == "2":
            filename = input("Enter file name to view: ")
            if os.path.exists(filename):
                try:
                    with open(filename, 'r') as f:
                        print("\n--- File Contents ---")
                        print(f.read())
                except IOError as e:
                    print(f"Error reading file '{filename}': {e}")
            else:
                print(f"File '{filename}' not found.")

        elif choice == "3":
            filename = input("Enter file name to edit: ")
            if os.path.exists(filename):
                try:
                    with open(filename, 'a') as f:
                        print("Enter text to append (type 'SAVE' to save):")
                        while True:
                            line = input()
                            if line == "SAVE":
                                break
                            f.write(line + "\n")
                    print(f"File '{filename}' updated.")
                except IOError as e:
                    print(f"Error updating file '{filename}': {e}")
            else:
                print(f"File '{filename}' not found.")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def out_of_the_box_experience():
    # Define the path to the file that tracks first use
    first_use_file = 'C:\\TerminalOS\\first_use.txt'

    try:
        # Check if the first use file exists
        if not os.path.exists(first_use_file):
            # Display the out-of-the-box experience
            print("\n--- Welcome to TerminalOS! ---")
            print("Here are some tips to get started:")
            print("1. Type 'Calculator' to perform basic arithmetic operations.")
            print("2. Use 'Weather' to get the current weather in your city.")
            print("3. Enjoy the 'Worm' game for some fun!")
            print("4. Explore the 'Text Editor' for file operations.")
            print("5. Type 'time' to check the time")
            print("6. Type 'clear' to clear your screen.")
            print("7. Type 'Search' to search with power!")
            
            name = input("Type your name: ")

            def typewriter(text, delay=0.1):
                for letter in text:
                    print(letter, end='', flush=True)
                    time.sleep(delay)
                print()
            
            typewriter("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁", 0.09)
            
            # Create the file to indicate that the out-of-the-box experience has been shown
            with open(first_use_file, 'w') as f:
                f.write("This file indicates the out-of-the-box experience has been shown.")

    except PermissionError:
        # Skip the out-of-the-box experience if there's a permission error
        print("Skipping out-of-the-box experience due to permission error.")

# Modify the main function to include the out-of-the-box experience
def main():
    out_of_the_box_experience()  # Call the OOBE function before showing the main interface
    print("TerminalOS v1.00 MU04 Build 2411.07 Compiled on 11/7/24 by Calculuxe")
    print("Type 'Ter' to start, 'info' for build info, or '?' for help.")

    while True:
        a = input("> ")
        if a == "?":
            print("Commands: 'Ter' to start, 'info' for build info, or '?' for help.")
        elif a == "info":
            print("TerminalOS v1.00 MU04 Build 2411.07 Compiled on 11/7/24 by Calculuxe")
        elif a == "Ter":
            print("TerminalOS v1.00 MU04 Build 2411.07 Compiled on 11/7/24 by Calculuxe")
            play_startup_sound()
            print("Type '?' for commands.")
            while True:
                b = input("> ")
                if b == "clear":
                  clear_screen()
                elif b == "Customize":
                  change_background_color()
                elif b == "Clock":
                    clock_app()
                elif b == "File Search":
                    file_explorer()
                elif b == "Calculator":
                    calculator()
                elif b == "Worm":
                    worm_game()
                elif b == "Restart":
                    restart()
                elif b == "Shut down":
                    shutdown()
                elif b == "Search":
                    search()
                elif b == "Weather":
                    mainw()
                elif b == "Text Editor":
                    text_editor()
                elif b == "Utilities":
                    utilities()
                elif b == "?":
                    print("Available commands: clear, Clock, Calculator, Worm, Shut down, Search, Weather, Utilities, Customize, File Search, Text Editor, and Restart")
                else:
                    print("Invalid command! Type '?' for help.")

if __name__ == "__main__":
    main()
