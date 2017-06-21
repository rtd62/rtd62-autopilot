import os
import time

from markovbot import MarkovBot

# Initialize a MarkovBot instance
tweetbot = MarkovBot()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the text file
book = os.path.join(dirname, '54913-0.txt')
# Make your bot read the text file
tweetbot.read(book)

my_first_text = tweetbot.generate_text(25, seedword=['starland', 'night'])
print("tweetbot says:")
print(my_first_text)

# Consumer Key
cons_key = '7OlHJHJwV5uz9S4Kx5HVpecCa'
# Consumer Secret
cons_secret = 'XTgcFAMTAOe3tMCoy0NPtaXq11myqskd2xiNobMLGQg2aTcKw0'
# Access Token
access_token = '875619076323786754-LdydJujj8Vn1vAofyWtzXDEQ0MIuga8'
# Access Token Secret
access_token_secret = '6pjE9SkSfYG5wyhMG13n8YtBT5uC8gjITmifg2TPiyjXD'

# Log In to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

# Start periodically tweeting
tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=1, keywords=None, prefix=None, suffix="#autopilot")

# Background Activity
secsinweek = 7 * 24 * 60 * 60
time.sleep(secsinweek)