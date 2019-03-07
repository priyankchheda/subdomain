import requests
from bs4 import BeautifulSoup


def google(domain):
    search_query = "site:{0} -site:www.{0}".format(domain)
    response = requests.get("https://www.google.com/search?q=" + search_query)
    soup = BeautifulSoup(response.text, "lxml")
    #for site in soup.select("._Rm"):
    #    print site


def main():
    domain = "github.com"
    subdomain = google(domain)
    print subdomain


if __name__ == '__main__':
    main()
