from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import time, argparse
from random import randint
import socket

def googlesearch(domain, subdomain, outputfile, pages):
    pages = pages*10

    driver = webdriver.Chrome()
    
    
    driver.get("https://www.google.com")
    time.sleep(3)
    elem = driver.find_element_by_name("q")

    base_dork = "site:"+domain
    search_dork = base_dork
    for sd in subdomain:
        search_dork += " -site:"+sd
    
    print "\n[URL] " + search_dork
    elem.send_keys(search_dork)
    elem.send_keys(Keys.RETURN)
    time.sleep(3)

    f = open('random.txt','r')
    random_str = []
    for line in f.readlines():
        random_str.append(line.strip())
    f.close()

    main_url =  driver.current_url 
    result = driver.page_source
    soup = BeautifulSoup(result,"lxml")
    url = []
    google_links = [
        'https://www.google.com',
        'https://www.google.co.in',
        'http://www.google.com',
        'http://www.google.co.in'
    ]
   
    # Store Google Results in url list
    for site in soup.select("._Rm"):
        url.append(site.text.split(domain,1)[0] + domain)

    for i in xrange(10,pages,10):
        # Distraction Search so that Google don't block your IP.
        count = randint(1,3)
        while count:
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
            driver.get(google_links[randint(0,3)])
            time.sleep(3)
            elem = driver.find_element_by_name("q")
            search_string = random_str[randint(0,len(random_str)-1)]
            elem.send_keys(search_string)
            elem.send_keys(Keys.RETURN)
            time.sleep(randint(3,10))
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w') 
            count = count - 1

        # Next Page
        driver.get(main_url + "&start="+str(i))
        time.sleep(3)
        result = driver.page_source
        soup = BeautifulSoup(result,"lxml")
        
        for site in soup.select("._Rm"):
            url.append(site.text.split(domain,1)[0] + domain)

    driver.close()

    tmp_url = []
    for u in url:
        # Remove https:// and http:// from url result
        tmp_url.append(u.replace("https://","").replace("http://",""))
    url = list(set(tmp_url))
    if domain in url:
        url.remove(domain)

    # Store output in file
    fo = open(outputfile, 'a')
    for i in url:
        print "[+] " + i
        fo.write("\n[+] " + i)
    fo.close()

    return url

def main():
    parser = argparse.ArgumentParser(description='Subdomain using Google Dork.')
    parser.add_argument('-d', dest='domain', metavar='domain', help='Target Domain', required=True)
    parser.add_argument('-o', dest='outputfile', help='Output file name [Default: subdomain.out]', default='subdomain.out')
    parser.add_argument('-p', dest='pages', type=int, help='Crawl n Google pages [Default: 3]', default=3)
    args = parser.parse_args()
    subdomain=["www."+args.domain]
    sd_list = []
    while True:
        try:
            sd_list = googlesearch(args.domain, subdomain, args.outputfile, args.pages)
        except Exception as e:
            print "Exception: " + str(e)
        subdomain.extend(sd_list)
        subdomain = list(set(subdomain))
        if not sd_list:
            print "[-] Got Nothing"
            break

if __name__=="__main__":
	main()
