import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os

# What you enter here will be searched for in Google Imag
querys = [
    "rasmalai",
    "gulab jamun",
    "samosa",
    "idli",
    "dosa",
    "ghevar",
    "vada pav",
    "palak paneer",
    "dal tadka",
    "chicken butter masala"
]
#make a loop if there are more than one query 
folder_name = 'E:/dataset/'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

def download_image(url, folder_name, num):

    # write image to file
    reponse = requests.get(url)
    if reponse.status_code==200:
        with open(os.path.join(folder_name, str(num)+".png"), 'wb') as file:
            file.write(reponse.content)
for query in querys:
	# Creating a webdriver instance
	options = webdriver.ChromeOptions()
	service = ChromeService(executable_path='C:/Users/ayush/Downloads/chromedriver_win32')
	driver = webdriver.Chrome(service=service, options=options)
	driver.maximize_window()


	# link of the website 
	driver.get('https://images.google.com/')

	# Finding the search box
	box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@jscontroller="vZr2rb"]//textarea')))


	# Type the search query in the search box
	box.send_keys(query)

	# Pressing enter
	box.send_keys(Keys.ENTER)
	print("starting scroll")
	# Function for scrolling to the bottom of Google
	# Images results
	def scroll_to_bottom():

		last_height = driver.execute_script('\
		return document.body.scrollHeight')

		while True:
			driver.execute_script('\
			window.scrollTo(0,document.body.scrollHeight)')

			# waiting for the results to load
			# Increase the sleep time if your internet is slow
			time.sleep(3)

			new_height = driver.execute_script('\
			return document.body.scrollHeight')

			# click on "Show more results" (if exists)
			try:
				driver.find_element_by_css_selector(".YstHxe input").click()

				# waiting for the results to load
				time.sleep(3)

			except:
				pass

			# checking if we have reached the bottom of the page
			if new_height == last_height:
				break

			last_height = new_height
		
#//*[@id="islrg"]/div[1]/div[51]/div[1]
    
	# Calling the function
	# there is no need to use the scroll_to_bottom() function if no of images is small.
	scroll_to_bottom()
	print("done scroll")
	driver.execute_script("window.scrollTo(0, 0);")
	page_html = driver.page_source
	pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
	containers = pageSoup.findAll('div', {'class':"isv-r PNCib MSM1fd BUooTd"} )
	print(len(containers))
	len_containers = len(containers)
	for i in range(45, len_containers+1):
             if i % 25 == 0:
                  continue#//*[@id="islrg"]/div[1]/div[51]/div[1]/a[1]/div[1]/img
             #//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]
             xPath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)
             previewImageXPath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img"""%(i)
             wait = WebDriverWait(driver, 10)
             previewImageElement = wait.until(EC.visibility_of_element_located((By.XPATH, previewImageXPath)))
             #previewImageElement = driver.find_element(By.XPATH, previewImageXPath)
             previewImageURL = previewImageElement.get_attribute("src")
             previewImageElementx = driver.find_element(By.XPATH, xPath)
             previewImageElementx.click()
             #driver.find_element_by_xpath(xPath).click()
             timeStarted = time.time()
             while True:
                   imageElement = driver.find_element(By.XPATH,"""//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]""")
                   #//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]
                   imageURL= imageElement.get_attribute('src')
                   if imageURL != previewImageURL:
                         print("actual URL", imageURL)
                         break
                   else:
                         #making a timeout if the full res image can't be loaded
                         currentTime = time.time()
                   if currentTime - timeStarted > 10:
                         print("Timeout! Will download a lower resolution image and move onto the next one")
                         break
             try:
                 download_image(imageURL, folder_name, i)
                 print("Downloaded element %s out of %s total. URL: %s" % (i, len_containers + 1, imageURL))
             except:
                     print("Couldn't download an image %s, continuing downloading the next one"%(i))
                #print("preview URL", previewImageURL)
                # #print(xPath)
                
    #time.sleep(3)

    #//*[@id="islrg"]/div[1]/div[16]/a[1]/div[1]/img

    #input('waawgawg another wait')

    # page = driver.page_source
    # soup = bs4.BeautifulSoup(page, 'html.parser')
    # ImgTags = soup.findAll('img', {'class': 'n3VNCb', 'jsname': 'HiaYvf', 'data-noaft': '1'})
    # print("number of the ROI tags", len(ImgTags))
    # link = ImgTags[1].get('src')
    # #print(len(ImgTags))
    # #print(link)
    #
    # n=0
    # for tag in ImgTags:
    #     print(n, tag)
    #     n+=1
    # print(len(ImgTags))

    #/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img

    #It's all about the wait

   
