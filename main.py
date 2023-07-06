import requests
from bs4 import BeautifulSoup


def scrape_wbna_schedule():
    full_schedule = []

    url = f'https://www.statspros.com/seattle-storm-tv-broadcast-schedule/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    schedule_table = soup.find("div", class_="entry-content").find('table').find('tbody')
    schedule_table = schedule_table.find('tr')

    for i in schedule_table:

        game = i.findAll('td')

        full_schedule.append({
            'teams': game[0],
            'date_time': game[1],
            'venue': game[2],
            'broadcast': game[3]
        })

    return full_schedule


if __name__ == '__main__':
    for i in scrape_wbna_schedule():
        teams = i['teams']
        date_time = i['date_time']
        venue = i['venue']
        broadcast = i['broadcast']

        print(f'Teams: {teams}, Date / Time: {date_time}, Venue: {venue}, Broadcast: {broadcast}')
