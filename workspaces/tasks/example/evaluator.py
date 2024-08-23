import requests
import os

def check_url(browser_logs):
    return "http://ogma.lti.cs.cmu.edu:8929/root/api-server" in browser_logs

def check_code_clone():
    # check path exists
    if os.path.exists('/workspace/api-server'):
        with open('/workspace/api-server/server.py') as f:
            code_content = f.read()
            if "# Route 1: Welcome message" in code_content:
                return True
    return False

def check_api():
    response = requests.get("http://localhost:5000/welcome")
    return response.status_code == 200 and response.json() == {"message": "Welcome to the Flask API!"}

if __name__ == "__main__":
    print(check_url("ACTION: goto('http://ogma.lti.cs.cmu.edu:8929/root/api-server')"))
    print(check_code_clone())
    print(check_api())