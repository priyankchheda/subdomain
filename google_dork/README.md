# Subdomain
Finds subdomains of the website with the help of Google Dorks.

## Introduction
In the Domain Name System (DNS) hierarchy, a subdomain is a domain that is a part of a main domain.

In Penetration Testing, finding subdomains is useful because they point to different applications and indicate different external network ranges used by the target company. For instance, x.company.com points to IP 1.1.1.1 and y.company.com points to IP 2.2.2.2. Now you know two different IP ranges possibly owned by your target and you can extend the attack surface.

Furthermore, subdomains sometimes host 'non-public' applications (e.g. test, development, restricted) which are usually less secure than the public applications so they can be the primary attack targets.

## Usage
```
$ 
$ python google_subdomain.py -h
usage: google_subdomain.py [-h] -d domain [-o OUTPUTFILE] [-p PAGES]

Subdomain using Google Dork.

optional arguments:
  -h, --help     show this help message and exit
  -d domain      Target Domain
  -o OUTPUTFILE  Output file name [Default: subdomain.out]
  -p PAGES       Crawl n Google pages [Default: 3]
$ 
$ 
$ python google_subdomain.py -d stackoverflow -p2

[URL] site:stackoverflow.com -site:www.stackoverflow.com
[+] es.meta.stackoverflow.com
[+] blog.stackoverflow.com
[+] chat.stackoverflow.com
[+] es.stackoverflow.com
[+] meta.stackoverflow.com
[+] business.stackoverflow.com
[+] blog.careers.stackoverflow.com
[+] talent.stackoverflow.com

[URL] site:stackoverflow.com -site:es.meta.stackoverflow.com -site:blog.stackoverflow.com -site:chat.stackoverflow.com -site:es.stackoverflow.com -site:meta.stackoverflow.com -site:business.stackoverflow.com -site:blog.careers.stackoverflow.com -site:www.stackoverflow.com -site:talent.stackoverflow.com
[+] insights.stackoverflow.com

[URL] site:stackoverflow.com -site:insights.stackoverflow.com -site:es.meta.stackoverflow.com -site:blog.stackoverflow.com -site:chat.stackoverflow.com -site:business.stackoverflow.com -site:meta.stackoverflow.com -site:es.stackoverflow.com -site:blog.careers.stackoverflow.com -site:www.stackoverflow.com -site:talent.stackoverflow.com
[-] Got Nothing
$
$
```

## Note
Please have ChromeDriver [https://sites.google.com/a/chromium.org/chromedriver/getting-started] installed in your system.
