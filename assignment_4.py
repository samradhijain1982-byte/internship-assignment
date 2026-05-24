# 1) Study the open weather API show more data in your API calling program
import requests

def weather_data(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a0eaf94be701082c1133c0f588416920&units=metric"

    try:
        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        print("\n------ WEATHER REPORT ------\n")

        print("City :", data['name'])

        print("Temperature :", data['main']['temp'], "°C")

        print("Feels Like :", data['main']['feels_like'], "°C")

        print("Humidity :", data['main']['humidity'], "%")

        print("Pressure :", data['main']['pressure'], "hPa")

        print("Weather :", data['weather'][0]['description'])

        print("Wind Speed :", data['wind']['speed'], "m/s")

        print("Minimum Temperature :", data['main']['temp_min'], "°C")

        print("Maximum Temperature :", data['main']['temp_max'], "°C")

    except requests.exceptions.RequestException as e:

        print(f"An error occurred: {e}")

city = input("Enter a city name: ")

weather_data(city)

#Try building today's game yourself
import random

def guessing_game():

    number = random.randint(1, 100)

    print("Welcome to Number Guessing Game")
    print("Guess a number between 1 and 100")

    while True:

        guess = int(input("Enter your guess: "))

        if guess > number:

            print("Too High")

        elif guess < number:

            print("Too Low")

        else:

            print("Correct Number")
            print("You Won the Game")
            break

guessing_game()


#3) Search for more free API's generate your and call them to fetch data. Display some data in your program.
# joke api
import requests

def random_joke():

    url = "https://official-joke-api.appspot.com/random_joke"

    try:

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        print("\n------ RANDOM JOKE ------\n")

        print("Setup :", data['setup'])

        print("Punchline :", data['punchline'])

    except requests.exceptions.RequestException as e:

        print(f"An error occurred: {e}")

random_joke()

#cat fact api
# day 6 cat fact api
import requests

def cat_fact():

    url = "https://catfact.ninja/fact"

    try:

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        print("\n------ CAT FACT ------\n")

        print("Fact :", data['fact'])

    except requests.exceptions.RequestException as e:

        print(f"An error occurred: {e}")

cat_fact()


# activity api
import requests

def activity():

    url = "https://www.boredapi.com/api/activity"

    try:

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        print("\n------ RANDOM ACTIVITY ------\n")

        print("Activity :", data['activity'])

        print("Type :", data['type'])

    except requests.exceptions.RequestException as e:

        print(f"An error occurred: {e}")

activity()
