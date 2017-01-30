# -*- coding: utf-8 -*-

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys #引入keys类操作
import time
import json

display = Display(visible=0, size=(800, 600))
display.start()
browser = webdriver.Chrome('/home/zegaoliu/Downloads/chromedriver')
browser.get('http://scdownloader.net/')
elem = browser.find_element_by_id("songURL")
elem.send_keys("https://soundcloud.com/trapgod1017bricksquad/gucci-mane-both-ft-drake-1")
elem.send_keys(Keys.RETURN)
html = []
axe = browser.find_element_by_xpath('//*[@id="results-wrapper"]/a').get_attribute("href")
html.append(axe)
print html #Check if the url address is valid
html.append(axe)
time.sleep(1)
browser.close()
fl=open('/home/zegaoliu/Dropbox/PythonScripts/PythonLearning/RemixMusic/MusicUrl.json', 'w')
#fl=open('../out/map_polyline.js', 'a')
#fl.write("var polyline_data=")
fl.write(json.dumps(html))
fl.close()
display.stop()


