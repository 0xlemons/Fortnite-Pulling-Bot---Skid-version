import requests
from datetime import datetime

def get_achievement_data(key, xuid, achievement_name="Gunsmith"):

    base_url = f"https://xbl.io/api/v2/achievements/player/{xuid}/267695549"

    headers = {
        "X-Authorization": key
    }

    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        for achievement in data.get("achievements", []):
            if achievement.get("name") == achievement_name and achievement.get("progressState") == "Achieved":
               
                time_unlocked = achievement['progression']['timeUnlocked']
                
                time_unlocked = time_unlocked.rstrip('Z').split('.')[0]
                
                date_time = datetime.fromisoformat(time_unlocked)
                
                month = date_time.month
                day = date_time.day
                year = date_time.year
                unlocked = True
                return unlocked, month, year, day
        
        print(f"The achievement '{achievement_name}' is not found or not unlocked.")
        return None
    else:
        print(f"Request failed with status code {response.status_code}")
        return None
    



