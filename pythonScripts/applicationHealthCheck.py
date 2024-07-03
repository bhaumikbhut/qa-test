import requests
import time

url = ''  # Replace with your application's URL

def check_application_health():
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            return 'up'
        else:
            return 'down'
    
    except requests.exceptions.RequestException as e:
        return 'down'

if __name__ == "__main__":
    print(f"Checking application health for: {url}")
    
    status = check_application_health()
    
    if status == 'up':
        print("Application is UP and functioning correctly.")
    elif status == 'down':
        print("Application is DOWN or not responding.")

