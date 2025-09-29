import json
import requests

def check_hash_virustotal(file_hash, api_key):
    url = f'https://www.virustotal.com/api/v3/files/{file_hash}'
    headers = {'x-apikey': api_key}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        return data['data']['attributes']['last_analysis_stats']
    return None
