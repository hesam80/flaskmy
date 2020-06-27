import requests
def get_proxy_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks://127.0.0.1:9050',
                       'https': 'socks://127.0.0.1:9050'},
    return session
session = get_proxy_session()
print(session.get("http://httpbin.org/ip").text)
# Above should print an IP different than your public IP

# Following prints your normal public IP
print(requests.get("http://httpbin.org/ip").text)