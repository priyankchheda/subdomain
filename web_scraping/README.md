# Subdomain-via-Third-Party-Resource
Finds subdomains of the website with the help of Third Party Internet Resource like crt.sh, virustotal.com and dnsdumpster.com

## Introduction
In the Domain Name System (DNS) hierarchy, a subdomain is a domain that is a part of a main domain.

In Penetration Testing, finding subdomains is useful because they point to different applications and indicate different external network ranges used by the target company. For instance, x.company.com points to IP 1.1.1.1 and y.company.com points to IP 2.2.2.2. Now you know two different IP ranges possibly owned by your target and you can extend the attack surface.

Furthermore, subdomains sometimes host 'non-public' applications (e.g. test, development, restricted) which are usually less secure than the public applications so they can be the primary attack targets.

## Usage
```
$ 
$ python websites.py -h
usage: websites.py [-h] -d domain [-o OUTPUTFILE]

Subdomain using various Internet Resource.

optional arguments:
  -h, --help     show this help message and exit
  -d domain      Target Domain
  -o OUTPUTFILE  Output file name [Default: subdomain.out]
$ 
$ 
$ 

```

## Note
Please have ChromeDriver [https://sites.google.com/a/chromium.org/chromedriver/getting-started] installed in your system.
