# spacextelegrambot
:rocket: A bot sends details about any SpaceX launch according send number to your Telegram account

Active modules:
* telebot - official module for interaction with bot token
* requests - for getting API requests

Bot works with [Telegram](https://telegram.org/) messenger. If the user wants to receive information about a specific flight number, then in response he will receive detailed information about the launch

![number](https://github.com/teora13/spacextelegrambot/blob/master/screens/number.png?raw=true)


If incorrect data is sent (negative values or too large), the bot sends an error message containing information about the maximum allowable value. This value is dynamic and it receives it through the API request

![error](https://github.com/teora13/spacextelegrambot/blob/master/screens/error.png?raw=true)


Also the bot checks the type of data that the user is sending. If any other non-digital value was sent, then general information about the most recent and next scheduled launch 
is returned to user

![lastNnext](https://github.com/teora13/spacextelegrambot/blob/master/screens/lastNnext.png?raw=true)
