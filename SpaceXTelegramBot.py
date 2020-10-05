import telebot
import requests
bot = telebot.TeleBot('token')

#information about all launches
flightAPI = 'https://api.spacexdata.com/v3/launches'

#API from the latest launch
lastAPI = 'https://api.spacexdata.com/v3/launches/latest'
last_name = requests.get(lastAPI).json()['mission_name']
last_local_time = requests.get(lastAPI).json()['launch_date_local']
last_rocket = requests.get(lastAPI).json()['rocket']['rocket_name']
last_site = requests.get(lastAPI).json()['launch_site']['site_name_long']
last_flight = requests.get(lastAPI).json()['flight_number']

#API from the next launch
nextAPI = 'https://api.spacexdata.com/v3/launches/next'
next_name = requests.get(nextAPI).json()['mission_name']
next_local_time = requests.get(nextAPI).json()['launch_date_local']
next_rocket = requests.get(nextAPI).json()['rocket']['rocket_name']
next_site = requests.get(nextAPI).json()['launch_site']['site_name_long']
greating = 'Send flight\'s number to get more details about it. Or send any message to get the information about the latest and the next launches'

@bot.message_handler(content_types=['text'])
def get_number(message):
    try:
        flight_number = requests.get(flightAPI).json()[(int(message.text)) - 1]['flight_number']
        mission_name = requests.get(flightAPI).json()[flight_number]['mission_name']
        launch_date_utc = requests.get(flightAPI).json()[flight_number]['launch_date_utc']
        rocket = requests.get(flightAPI).json()[flight_number]['rocket']['rocket_name']
        launch_site = requests.get(flightAPI).json()[flight_number]['launch_site']['site_name_long']
        launch_success = requests.get(flightAPI).json()[flight_number]['launch_success']
        details = requests.get(flightAPI).json()[flight_number]['details']
# if user input any number bot sends back details about launch according this number
        if message.text:
            bot.send_message(message.from_user.id, f'Flight number: {flight_number} \nMission name: {mission_name} \nLunch date(utc): {launch_date_utc} \nRocket: {rocket} \nLaunch site: {launch_site} \nLaunch success: {launch_success} \nDatails: {details} \n\n*{greating}*', parse_mode='Markdown')
#if number is out of range bot sends error message with max available number (keeps in var /last_flight/)
    except IndexError:
        bot.send_message(message.from_user.id, f'Looks like your choice is out of range. Last flight is {last_flight}. Please, try again')
#bot sends info about the latest and the next launches if input type of data is any letter/s
    except ValueError:
        bot.send_message(message.from_user.id, f'The last launch was: {last_name} \nRocket: {last_rocket} \nYour local time was: {last_local_time} \nSite: {last_site}')
        bot.send_message(message.from_user.id, f'The next launch is: {next_name} \nRocket: {next_rocket} \nYour local time will be: {next_local_time} \nSite: {next_site} \n\n*{greating}*', parse_mode='Markdown')

#timeout for long polling
bot.polling(none_stop=True, interval=0)