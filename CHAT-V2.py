from rich.console import Console
from rich.panel import Panel
from time import sleep as s
import requests, sys, os, time, random


def proccess():
    for i in list("\|/-"):
        print(f"\r\033[0;97m[\033[0;92m{i}\033[0;97m] sedang mengetik...",end="")
        time.sleep(0.5)

data = {
"hai":"hai juga",
"assalamualaikum":"waalaikumsalam",
"apa kabar":"baik baik saja, apa kabar juga..?",
"sama":"baiklah...",
"aku suka kamu":"iyah, aku juga suka sama kamu",
"kamu lagi apa":"lagi duduk aja nih",
"kamu lagi ngapain":"lagi mikirin kamu",
"lagi apa":"apanya",
"iyah kamu lagi apa":"diem"
}


def bot():
	os.system('clear')
	while True:
		print(f"\n")
		user = input(f'     \033[1;90mKetik pesan\r \033[1;91m>\033[1;92m ')
		print('\033[4A');Console().print(Panel('[white]'+user, style='green'), justify='right')
		if user in data:
			proccess()
			print('\033[3A');Console().print(Panel('[white]'+data[user], style='purple'), justify='left')
		else:
			proccess()
			x = "maaf saya tidak mengerti !"
			print('\033[3A');Console().print(Panel('[white]'+x, style='purple'), justify='left')
			
			
bot()
                
        
		
		
	
	
				
	