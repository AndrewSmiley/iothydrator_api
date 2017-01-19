import requests r = requests.get("http://localhost:8000/v1/get_cars", params={"make":"Ford"}) if r.status_code == 200:
    print r.text
