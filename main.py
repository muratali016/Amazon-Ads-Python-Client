import requests
class AmazonAPI:
    def __init__(self, client_id, scope, access_token):
        self.base_url = 'https://advertising-api-eu.amazon.com'
        self.headers = {
            'Content-Type': 'application/vnd.createasyncreportrequest.v3+json',
            'Amazon-Advertising-API-ClientId': client_id,
            'Amazon-Advertising-API-Scope': scope,
            'Authorization': f'Bearer {access_token}'
        }
    def create_report(self, name, start_date, end_date, configuration):
        url = f'{self.base_url}/reporting/reports'
        data = {
            "name": name,
            "startDate": start_date,
            "endDate": end_date,
            "configuration": configuration
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()

    def get_report_status(self, report_id):
        url = f'{self.base_url}/reporting/reports/{report_id}'
        response = requests.get(url, headers=self.headers)
        return response.json()
