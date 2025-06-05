import requests

class CreateUrlEndpoint: 

    
    def create_short_url_for_url(self, long_url, code = None):
        if code:
            response = requests.post('https://gotiny.cc/api',
                               headers={'Content-Type': 'applocation/json'},
                               json={'long': long_url, 'custom': code}) 
        else:
            response = requests.post('https://gotiny.cc/api',
                               headers={'Content-Type': 'applocation/json'},
                               json={'input': long_url}) 
        status = None
        long = None
        tiny = None
        sent_code = None

        site_url = 'https://www.discovery.com//shark-week/se-schedule-2023-pictures'
        response = requests.post('https://gotiny.cc/api',
                            headers={'Content-Type': 'applocation/json'},
                            json={'input': site_url})
        self.sent_code = code if code else None
        self.sent_url = long_url
        self.status = response.status_code
        self.long = response.json()[0]['long']
        self.tiny = response.json()[0]['code']

        return response
     
    def check_response_status_is_ok(self, status):
        assert self.status == 200

    def check_long_url_same_as_sent(self):
        assert self.sent_url == self.long

    def check_tiny_url_is_not_empty(self):
        assert self.tiny > 0

    def check_short_code_same_as_sent(self):
        assert self.sent_code == self.code
