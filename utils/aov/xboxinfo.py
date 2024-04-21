import requests
url = "https://xbl.io/api/v2/search/"
api_key = "dc46de61-dbba-4471-91f6-577ed1a0bc3"
headers = {
    "X-Authorization": api_key
}
def xuid(username):
    response = requests.get(f'{url}{username}', headers=headers)
    data = response.json()
    if 'people' in data and data['people']:
        first_person = data['people'][0]
        xuid = first_person.get('xuid')
        return xuid      
def followers(username):
    response = requests.get(f'{url}/{username}', headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
        return None
    try:
        data = response.json()
        if 'people' in data and data['people']:
            first_person = data['people'][0] 
            followers = first_person.get('detail', {}).get('followerCount')
            return followers
    except:
        print ('error getting followers')

