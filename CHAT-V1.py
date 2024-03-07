import os
os.system ("clear")

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

while True:
	user = input ("- user : ")
	if user in data:
		print ("- bot  :",data[user])
	else:
		print ("- bot  : maaf saya tidak mengerti !")
		
	
	
		
		
	
				
	