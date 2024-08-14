import requests
import json
with open("config.json", "r") as config_file:
    config = json.load(config_file)
with requests.Session() as session:
    session.cookies.set('.ROBLOSECURITY', config.get("roblox_token", ""))
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = session.get("https://usermoderation.roblox.com/v1/not-approved", headers=headers)
        response.raise_for_status()
        json_data = response.json()
        if json_data:
            print(json.dumps(json_data, indent=4))
        else:
            print("No ban data!")
    except requests.exceptions.HTTPError as http_err:
        print(f"Error: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error: {req_err}")
    except json.JSONDecodeError:
        print("Json decode error")

input("\nPress Enter to exit...")
