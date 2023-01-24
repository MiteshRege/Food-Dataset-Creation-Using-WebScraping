import bs4 
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

#creating a directory to save images
folder_name = 'Dataset-MajorProj-Sem8\kanda_poha'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

def download_image(url, folder_name, num):

    # write image to file
    reponse = requests.get(url)
    if reponse.status_code==200:
        with open(os.path.join(folder_name, str(num)+".jpg"), 'wb') as file:
            file.write(reponse.content)

chromePath=r'C:\Users\hp\Documents\Selenium_Proj\Drivers\chromedriver.exe'
driver=webdriver.Chrome(chromePath)
search_URL = "https://www.google.com/search?q=kanda poha&source=lnms&tbm=isch"
driver.get(search_URL)


#//*[@id="islrg"]/div[1]/div[1]
#//*[@id="islrg"]/div[1]/div[50]
#//*[@id="islrg"]/div[1]/div[25]
#//*[@id="islrg"]/div[1]/div[75]
#//*[@id="islrg"]/div[1]/div[350]


a = input("Waiting...")

#Scrolling all the way up
driver.execute_script("window.scrollTo(0, 0);")

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('img', {'class':"rg_i Q4LuWd"} )

print(len(containers))

len_containers = len(containers)

for i in range(1, len_containers+1):
    if i % 25 == 0:
        continue
# preview :

# //*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img
# //*[@id="islrg"]/div[1]/div[4]/a[1]/div[1]/img
# //*[@id="islrg"]/div[1]/div[7]/a[1]/div[1]/img
# //*[@id="islrg"]/div[1]/div[3]/a[1]/div[1]/img
# //*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img
# //*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img
# zommer one :

# //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img
# //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img
# //*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img
    xPath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)

    previewImageXPath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img"""%(i)
    previewImageElement = driver.find_element(By.XPATH, previewImageXPath)
    # previewImageElement = driver.find_element_by_xpath(previewImageXPath)
    previewImageURL = previewImageElement.get_attribute("src")
    print("preview URL", previewImageURL)


    #print(xPath)


    driver.find_element_by_xpath(xPath).click()
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

    timeStarted = time.time()
    while True:

        imageElement = driver.find_element_by_xpath("""//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img""")
        imageURL= imageElement.get_attribute('src')

        if imageURL != previewImageURL:
            #print("actual URL", imageURL)
            break

        else:
            #making a timeout if the full res image can't be loaded
            currentTime = time.time()

            if currentTime - timeStarted > 40:
                print("Timeout! Will download a lower resolution image and move onto the next one")
                break


    #Downloading image
    try:
        download_image(imageURL, folder_name, i)
        print("Downloaded element %s out of %s total. URL: %s" % (i, len_containers + 1, imageURL))
    except:
        print("Couldn't download an image %s, continuing downloading the next one"%(i))

    #//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img
    #//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img


#     ##########
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# # What you enter here will be searched for in
# # Google Images
# query = "Amras"

# # Creating a webdriver instance
# chromePath=r'C:\Users\hp\Documents\Selenium_Proj\Drivers\chromedriver.exe'
# driver=webdriver.Chrome(chromePath)
# # driver = webdriver.Chrome('C:\Users\hp\Documents\Selenium_Proj\Drivers\chromedriver.exe')


# # Maximize the screen
# driver.maximize_window()

# # Open Google Images in the browser
# driver.get('https://images.google.com/')

# # Finding the search box
# # //*[@id="REsRA"]
# box = driver.find_element_by_xpath('//*[@id="REsRA"]')

# # Type the search query in the search box
# box.send_keys(query)

# # Pressing enter
# box.send_keys(Keys.ENTER)

# # Function for scrolling to the bottom of Google
# # Images results
# def scroll_to_bottom():

# 	last_height = driver.execute_script('\
# 	return document.body.scrollHeight')

# 	while True:
# 		driver.execute_script('\
# 		window.scrollTo(0,document.body.scrollHeight)')

# 		# waiting for the results to load
# 		# Increase the sleep time if your internet is slow
# 		time.sleep(3)

# 		new_height = driver.execute_script('\
# 		return document.body.scrollHeight')

# 		# click on "Show more results" (if exists)
# 		try:
# 			driver.find_element_by_css_selector("#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img").click()

# 			# waiting for the results to load
# 			# Increase the sleep time if your internet is slow
# 			time.sleep(3)

# 		except:
# 			pass

# 		# checking if we have reached the bottom of the page
# 		if new_height == last_height:
# 			break

# 		last_height = new_height


# # Calling the function

# # NOTE: If you only want to capture a few images,
# # there is no need to use the scroll_to_bottom() function.
# scroll_to_bottom()


# # Loop to capture and save each image
# for i in range(1, 50):

# 	# range(1, 50) will capture images 1 to 49 of the search results
# 	# You can change the range as per your need.
# 	try:

# 	# XPath of each image
#     # //*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img
# 		img = driver.find_element_by_xpath(
# 			'//*[@id="islrg"]/div[1]/div[' +
# 		str(i) + ']/a[1]/div[1]/img')

# 		# Enter the location of folder in which
# 		# the images will be saved
# 		img.screenshot('Dataset-MajorProj-Sem8\Aamras' +
# 					query + ' (' + str(i) + ').png')
# 		# Each new screenshot will automatically
# 		# have its name updated

# 		# Just to avoid unwanted errors
# 		time.sleep(0.2)

# 	except:
		
# 		# if we can't find the XPath of an image,
# 		# we skip to the next image
# 		continue

# # Finally, we close the driver
# driver.close()

