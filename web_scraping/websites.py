from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import time, argparse
import socket
import pymongo

def activecheck(domain):
    # check if the domain is active or not
    try:
        ip = socket.gethostbyname(domain.strip())
        return str(ip) + ' - ' + domain
    except socket.gaierror:
        try:
            i_tmp = "www." + domain
            ip = socket.gethostbyname(i_tmp.strip())
            return str(ip) + ' - ' + domain
        except socket.gaierror:
            return
            
def certificate(driver, domain, fout, subdomain):
    print "\n\n[*] Using Crt.sh"
    fout.write("\n\n[*] Using Crt.sh\n")
    driver.get("https://crt.sh/?q=%25"+domain)
    time.sleep(5)
    result = driver.page_source
    soup = BeautifulSoup(result,"lxml")
    results = soup.findAll("td", attrs={'style':None, 'class':None})
    for r in results:
        if domain in r.text.lower():
            print "  [+] " + r.text
            fout.write("  [+] " + r.text + "\n")
            subdomain.append(activecheck(r.text))
    return subdomain

def virustotal(driver, domain, fout, subdomain):
    print "\n\n[*] Using VirusTotal"
    fout.write("\n\n[*] Using VirusTotal\n")
    driver.get("https://virustotal.com/en/domain/"+domain+"/information/")
    time.sleep(5)
    result = driver.page_source
    soup = BeautifulSoup(result,"lxml")
    subd = soup.select('#observed-subdomains')[0].findAll('div', attrs={'class':'enum'})
    for sub in subd:
        for i in sub.findAll('a'):
            print "  [+] " + i.text.strip()
            fout.write("  [+] " + i.text.strip() + "\n")
            subdomain.append(activecheck(i.text.strip()))
    return subdomain

def getText(parent):
    return ''.join(parent.find_all(text=True, recursive=False)).strip()

def dnsdumpster(driver, domain, fout, subdomain):
    print "\n\n[*] Using DNSDumpster"
    fout.write("\n\n[*] Using DNSDumpster\n")
    driver.get("https://dnsdumpster.com")
    time.sleep(5)
    elem = driver.find_element_by_id("regularInput")
    elem.send_keys(domain)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    result = driver.page_source
    soup = BeautifulSoup(result,"lxml")
    for i in soup.findAll('td', attrs={'class':'col-md-4'}):
        print "  [+] " + getText(i)
        fout.write("  [+] " + getText(i) + "\n")
        subdomain.append(activecheck(getText(i)))
    return subdomain

def main():
    parser = argparse.ArgumentParser(description='Subdomain using various Internet Resource.')
    parser.add_argument('-d', dest='domain', metavar='domain', help='Target Domain', required=True)
    parser.add_argument('-o', dest='outputfile', help='Output file name [Default: subdomain.out]', default='subdomain.out')
    args = parser.parse_args()

    subdomain=[]
    fout = open(args.outputfile, 'w')
    driver = webdriver.Chrome()
    subdomain = certificate(driver, args.domain, fout, subdomain)
    subdomain = virustotal(driver, args.domain, fout, subdomain)
    subdomain = dnsdumpster(driver, args.domain, fout, subdomain)
    driver.close()

    subdomain = list(set(subdomain))
    if None in subdomain:
        subdomain.remove(None)

    print "\n\n\n" + "="* 60
    print "  \t\tCurrently Active Subdomains"
    print '='* 60 + "\n\n"
    fout.write("\n\n\n" + "="* 60 + "\n")
    fout.write("  \t\tCurrently Active Subdomains\n")
    fout.write('='* 60 + "\n\n\n")
    for i in subdomain:
        print "[+] " + i
        fout.write("[+] " + i + "\n")
    fout.close()

if __name__ == '__main__':
    main()
