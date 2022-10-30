from urllib import request
from time import sleep
#from sensehat  import sensehat
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()

while  True:
  sleep(3)

  form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeFkSEXq4lH0KeH5NmUQmnBNMfvUt1NnW4mwgBKd22ThthncA/formResponse?usp=pp_url&entry.590822413={}&submit=Submit".format(temp)
  request.urlopen(form_url)
  
