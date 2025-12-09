import requests
from datetime import date

class get_holiday:
    def __init__(self):
        self.today = date.today()
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day
        self.API_KEY = ''
        self.url = 'https://calendarific.com/api/v2/holidays'
        self.country_code = 'RU'
        self.params = {
            'api_key': self.API_KEY,
            'country': 'RU',
            'year': self.year,
            'month': self.month,
            'day': self.day
        }
        self.params2 = {
            'api_key': self.API_KEY,
            'country': self.country_code,
            'year': self.year
        }

    def holiday_today(self):
        response = requests.get(self.url, params=self.params)
        data = response.json()

        if 'response' in data and 'holidays' in data['response']:
            holidays = data['response']['holidays']
            if holidays:
                print(f"Сегодня ({self.today}) отмечаются следующие праздники:")
                for holiday in holidays:
                    print(f"- {holiday['name']}")
            else:
                print(f"Сегодня ({self.today}) праздников не найдено.")

    def holiday_list(self):
        response = requests.get(self.url, params=self.params2)
        data = response.json()

        if 'response' in data and 'holidays' in data['response']:
            holidays = data['response']['holidays']
            print(f"Всего праздников в {self.country_code} в {self.year}: {len(holidays)}")
            for holiday in holidays:
                date_str = holiday['date']['iso']
                name = holiday['name']
                print(f"{date_str}: {name}")



test = get_holiday()
test.holiday_today()
test.holiday_list()
