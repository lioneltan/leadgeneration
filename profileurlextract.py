from selenium.webdriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup
import xlsxwriter
from itertools import chain

urls = [
"https://www.linkedin.com/in/louistancsmarketing/?originalSubdomain=sg", "https://www.linkedin.com/in/louistancsmarketing/?originalSubdomain=sg"
]

for url in urls:
    driver_path='C:\\Users\\sirli\\OneDrive\\Desktop\\chromedriver\\chromedriver.exe'
    options = ChromeOptions()
    options.headless = True
    driver = Chrome(executable_path=driver_path, options=options)
    driver.get(url)
    xpathtitle='//*[starts-with(@class, "text-body-medium")]'

    link_elementstitle = driver.find_elements_by_xpath(xpathtitle)

    for links_el in link_elementstitle:
        titleoutput= links_el.get_attribute("innerHTML")
        list.append([titleoutput])
        print(list)