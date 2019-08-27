import json
import requests
from django.utils import six
if six.PY2:
    from urllib import quote
else:
    from urllib.parse import quote


# Class Show_Info():

def get_new_token():
    apikey = '47UG60SA6LRXE233'
    username = 'satishkrgu95hbv'
    userkey = 'OC6KE0IRGFGSGY4J'
    payload = json.dumps({'apikey': apikey, 'username': username, 'userkey': userkey})
    url = 'https://api.thetvdb.com/login'
    headers = {"Content-Type": "application/json", "Accept": "application/json", "User-agent": "Mozilla/5.0"}
    r = requests.post(url, data=payload, headers=headers)
    return r.json()['token']


def get_token():
    try :
        new_token = get_new_token()
    except:
        print('API MUST BE DOWN')
        return None
    return new_token


def search_series_list(series_name):
    token = get_token()
    headers = {"Content-Type": "application/json", "Accept": "application/json", 'Authorization': 'Bearer '+token, "User-agent": "Mozilla/5.0"}
    url = 'https://api.thetvdb.com/search/series?name=' + quote(series_name)
    try:
        json_r = requests.get(url, headers=headers).json()
        return json_r['data'][:5]
    except Exception:
        return None


def get_series_with_id(tvdbID):
    token = get_token()
    headers = {"Content-Type": "application/json", "Accept": "application/json", 'Authorization': 'Bearer '+token, "User-agent": "Mozilla/5.0"}
    url = 'https://api.thetvdb.com/series/' + str(tvdbID)
    try:
        json_r = requests.get(url, headers=headers).json()
        json_r = json_r['data']
        show_info = {}
        show_info['tvdbID'] = tvdbID
        show_info['seriesName'] = json_r['seriesName']
        show_info['banner'] = json_r['banner']
        show_info['status'] = json_r['status']
        show_info['firstAired'] = json_r['firstAired']
        show_info['overview'] = json_r['overview']
        show_info['imdbID'] = json_r['imdbId']
        show_info['genre'] = json_r['genre']
        show_info['siteRating'] = json_r['siteRating']
        show_info['network'] = json_r['network']
        return show_info
    except Exception:
        return None

# print(search_series_list("Game of Thrones"))
