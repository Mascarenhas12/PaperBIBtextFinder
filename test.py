#MADE BY MANUEL DUARTE MASCARENHAS - IST LEIC-T 2019

import requests, sys, bs4, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def q_search(search, opt):
    site = ("https://scholar.google.com","https://www.nber.org/papers.html")[opt]
    driver = webdriver.Chrome()
    driver.get(site)
    element = driver.find_element_by_name("q")
    element.clear()
    element.send_keys(search)
    element.submit()
    time.sleep(0.5)

    return driver

def get_soup(site):
    res = requests.get(site)
    #print(res)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    return soup

def get_bib(Bibhref):
    soup = get_soup(Bibhref)
    print(soup.prettify())

def article(search):
    driver = q_search(search,False)
    #print(driver.current_url)

    try:
        Citar = driver.find_element_by_css_selector("a[title='Citar']")
    except:
        print("Couldn't find anything in search\n")
        driver.quit()
        sys.exit(1)

    Citar.click()
    #print(button)

    time.sleep(0.5)
    Bibbut = driver.find_element_by_id("gs_citi")

    Bibhref = (Bibbut.find_elements_by_css_selector("*")[0]).get_attribute("href")
    #print(Bibhref)

    get_bib(Bibhref)
    driver.quit()
    sys.exit(0)

def wp_article(search):
    driver = q_search(search,True)

    url= driver.current_url

    soup = get_soup(url)
    list = soup.select(".url")

    tag = list[0].string
    Bibhref = "https://www.nber.org" + tag + ".bib"
    get_bib(Bibhref)
    driver.quit()
    sys.exit(0)

#--------------------------------MAIN------------------------------------------#
search = sys.argv[1]
print(search +"\n")

if("wp" in search):
    wp_article(search.replace("wp",""))
else:
    article(search)
