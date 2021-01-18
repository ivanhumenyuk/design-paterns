import time


# Target class
class UserInterface():
    def json_request(self):
        pass

    def json_response(self):
        pass


# Adaptee class,
class XmlApiService():
    def xml_api_request(self):
        return 'XML request'

    def xml_api_response(self):
        return 'XML response'


# Adapter class
class JsonConverter(UserInterface):
    def __init__(self, xml: XmlApiService):
        self.xml = xml

    def json_request(self):
        return f'--This is {self.xml.xml_api_request()} to {self.xml.__class__.__name__} reformatted form JSON--'

    def json_response(self):
        return f'--This is {self.xml.xml_api_response()} from {self.xml.__class__.__name__} reformatted to JSON--'


def user(service: UserInterface):
    print('Your data is reformatting...')
    print('\n')
    time.sleep(3)
    print(service.json_request())
    print('\n')
    print('Processing...')
    time.sleep(3)
    print('\n')
    print(service.json_response())


if __name__ == '__main__':
    xml_serv = XmlApiService()
    converter = JsonConverter(xml_serv)

    user(converter)
