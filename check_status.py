import requests


class StatusCheck:
    check_response_jobwatch = requests.get('https://www.itjobswatch.co.uk')
    def check_status(self, test):
        if self.check_response_jobwatch.status_code == test:
            return 'Successful'
        else:
            return 'Unsuccessful'
