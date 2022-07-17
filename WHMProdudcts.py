
import requests

url='https://alphavps.com/clients/store/ssd-openvz-virtual-servers'

def _build_headers():
    headers = {}
    headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

def parse_product( url ):
    
    resp = requests.get(url, headers=_build_headers() )
    
    if resp.status_code == 200:
        print ( resp.text )
    else:
        print ( "Bad request ", resp.text )


if __name__ == '__main__':

    parse_product( url )
