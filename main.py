################################
# .import                      #
################################


import requests
from bs4 import BeautifulSoup
from pytube import YouTube
import random
from time import sleep


################################
# .variables                   #
################################


downloadDir = '/mnt/f/ippsec' # Change this to your download dir anc create it
listNew = open("urls.txt").readlines()

################################
# .banner                      #
################################


def obligatory_banner():
  banner = """\033[91m
   ___ ____  ____  ____  _____ ____                                
  |_ _|  _ \|  _ \/ ___|| ____/ ___|                               
   | || |_) | |_) \___ \|  _|| |                                   
   | ||  __/|  __/ ___) | |__| |___                                
  |___|_| __|_|   |____/|_____\____| ___    _    ____  _____ ____  
  |  _ \ / _ \ \      / / \ | | |   / _ \  / \  |  _ \| ____|  _ \ 
  | | | | | | \ \ /\ / /|  \| | |  | | | |/ _ \ | | | |  _| | |_) |
  | |_| | |_| |\ V  V / | |\  | |__| |_| / ___ \| |_| | |___|  _ < 
  |____/ \___/  \_/\_/  |_| \_|_____\___/_/   \_\____/|_____|_| \_\
\033[0m

  \033[90m-----------------:[\033[0m SevenLayerJedi ]
  \033[90m-----------------:[\033[0m v1.05          ]\n"""
  print(banner)


################################
# .main                        #
################################


obligatory_banner()

for link in listNew:
  print(' [+] DOWNLOADING: {0}'.format(link))
  try:
    YouTube(link).streams.first().download(downloadDir)
    sleep(random.randrange(3,10))
  except:
    print(' [+] SLEEPING FOR 2 MINUTES')
    sleep(120)
    YouTube(link).streams.first().download(downloadDir)
