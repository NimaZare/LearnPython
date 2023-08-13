from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        super().__init__()

    def Login(self):
        self.driver.get('https://instagram.com')
        sleep(2)
        user_name = self.driver.find_element_by_xpath('//input[@name="username"]')
        user_name.clear()
        user_name.send_keys(self.username)
        passwordMe = self.driver.find_element_by_xpath('//input[@name="password"]')
        passwordMe.clear()
        passwordMe.send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.get(f'https://www.instagram.com/{self.username}/')

    def Like(self, hashtags, like_count):
        hashtags_list = hashtags.split(',')
        for i in hashtags_list:
            self.driver.get(f'https://www.instagram.com/explore/tags/{i}/')
            sleep(2)
            links = self.driver.find_elements_by_tag_name('a')
            posts_link = [l.get_attribute('href') for l in links if '.com/p/' in l.get_attribute('href')]
            for i in range(like_count):
                self.driver.get(posts_link[i])
                self.driver.find_element_by_xpath('//button[@class="wpO6b "]').click()
                sleep(randint(3, 6))
            
        
    
    def Quit(self):
        self.driver.quit()
    
 

# mybot = InstagramBot(input('Please enter username : '), input('Please enter password : '))
mybot = InstagramBot('jackycleverboy', 'Nima#$#1551295')
mybot.Login()
sleep(3)
mybot.Like('apple,love', 3)
