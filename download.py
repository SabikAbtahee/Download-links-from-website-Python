from bs4 import BeautifulSoup
import bs4
import requests
import os


###Directory in which downloaded files will be found
directoryPath= 'C:\\Users\\Public\\Downloads\\'
if not os.path.exists('C:\\Users\\Public\\Downloads'):
	os.mkdir('C:\\Users\\Public\\Downloads')

###Configure your websites in the variable website link
websiteLink = requests.get('https://tauheed-sunnat.com/quran/shaykh-abu-baker-shatree')

###Configure File extension
extension=".mp3" # ".mp3" ".pdf" ".txt" ".zip"

###Config File Name Manually otherwise dont change it
i=1




soup = BeautifulSoup(websiteLink.text,'html.parser')
for link in soup.find_all('a',href=True):
	url = link['href']
	if(url.find(extension)>=0):
		r = requests.get(url)
		path=directoryPath+str(i)+extension
		i+=1
		with open(path, 'wb') as f:  
				f.write(r.content)

		print(r.status_code) 
		print(str(i) + "  DONE")
























	# IGNORE REST


	# websiteLink2 = requests.get('https://tauheed-sunnat.com/quran/shaykh-abu-baker-shatree?page=1')
	# link=[websiteLink,websiteLink2]

	#Configured for specific website
	# if(url.find('.mp3')>=0):
	# 	# print(url)
	# 	y=url[127:150]
	# 	z=""
	# 	for i in y:
	# 		if(i.isalpha()==True):
	# 			z+=i
	# 		if(i=="%"):
	# 			print("ASD")
	# 			break
	# 	r = requests.get(url)
	# 	path="C:\\Downloads"+str(z)+".mp3"
		
	# 	with open(path, 'wb') as f:  
	# 		f.write(r.content)

	# 	print(r.status_code) 
	# 	print(str(z) + "  DONE")


# url = 'https://tauheed-sunnat.com/sites/default/files/quran/Tilawat/Shatree/Quran%20-%20Abu%20Baker%20Shatree%20-%20Surah%20009%20-%20Al-Tauba%20-%20The%20Repentance%20%28www.Tauheed-Sunnat.com%29.mp3'
# # urllib.request.urlretrieve(url, '/Users/scott/Downloads/cat.mp3') 
# r = requests.get(url)
# with open('/Users/sabik/Downloads/cat3.mp3', 'wb') as f:  
#     f.write(r.content)
# print(r.status_code)  
# print(r.headers['content-type'])  
# print(r.encoding) 


# x="https://tauheed-sunnat.com/sites/default/files/quran/Tilawat/Shatree/Quran%20-%20Abu%20Baker%20Shatree%20-%20Surah%20001%20-%20";

# for i in y:
# 	if(i.isalpha()==True and (i!='%' or i!='-' )):
# 		z+=i

# print(z)