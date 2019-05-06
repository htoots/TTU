# Homework 4 for ICS0019

Task:
```
Create a Python spider for page:
https://ordi.eu/lauaarvutid?___store=en&___from_store=et (English)
or
https://ordi.eu/lauaarvutid (Estonian)
Grab all computers from all pages and create JSON file with attributes:
{Product name: '', Price: '', Picture href: ''}
You may use Scrapy library or Beautiful Soup library.
```

## Running script
```
python(3) script.py
```

Script goes to site,

`https://ordi.eu/lauaarvutid?___store=en&___from_store=et&limit=all`

gets all computers with their product name, price, href and saves it

uses requests, json, and lxml
