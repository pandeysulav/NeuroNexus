import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}

print("Fetching webpage...")
webpage = requests.get('https://www.ambitionbox.com/list-of-companies?page=1', headers=headers, timeout=15).text
print("Done!")

# Save to file
with open('ambitionbox.html', 'w', encoding='utf-8') as f:
    f.write(webpage)

print("HTML saved to ambitionbox.html")