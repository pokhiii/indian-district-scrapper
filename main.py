import json
import requests
from bs4 import BeautifulSoup


def scrape_districts(state_url):
    """Scrapes the list of districts for a given state URL."""
    response = requests.get(state_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    district_rows = soup.find_all('div', class_='search-result-row')
    district_names = []

    for row in district_rows:
        district_name = row.find('a').text.strip()
        district_names.append(district_name)

    return district_names


def main():
    # Visit start URL with list of states
    start_url = "https://igod.gov.in/sg/district/states"

    response = requests.get(start_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        state_container = soup.find('div', class_=['cat-box', 'state'])

        state_list = state_container.find('ul')

        state_data = []
        district_data = {}

        for state in state_list.find_all('li'):
            state_name = state.find('a').text.strip()
            state_url = state.find('a')['href']
            state_code = state_url.split('/')[-3]

            state_data.append({
                'name': state_name,
                'code': state_code,
            })

            district_data[state_code] = scrape_districts(state_url)

        state_json = json.dumps(state_data, indent=4)
        district_json = json.dumps(district_data, indent=4)

        print(state_json)
        print(district_json)

    else:
        print(f"Error downloading {start_url}")


if __name__ == "__main__":
    main()
