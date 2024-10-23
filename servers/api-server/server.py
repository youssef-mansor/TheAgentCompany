from flask import Flask, jsonify
import subprocess
import os
import json
import threading
import requests


app = Flask(__name__)

def get_git_root():
    try:
        git_root = subprocess.check_output(
            ['git', 'rev-parse', '--show-toplevel'],
            cwd=os.getcwd(),
            stderr=subprocess.STDOUT,
            universal_newlines=True
        ).strip()
        return git_root
    except subprocess.CalledProcessError:
        return None

EXECUTION_DIR = get_git_root() + '/servers'

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Web service is up!")
            return 200, "Web service is up!"
        else:
            return response.status_code
    except requests.ConnectionError:
        print("Web service is not available yet. Retrying...")
        return 500, "Web service is not available yet"

def execute_command(command):
    try:
        print(EXECUTION_DIR, command)
        os.chdir(EXECUTION_DIR)
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Command execute failed: {e}"
    except Exception as e:
        return f"Error : {e}"

def async_execute_command(command):
    threading.Thread(target=execute_command, args=(command,)).start()

@app.route('/api/nextcloud-config', methods=['GET'])
def get_nextcloud_config():
    output = execute_command('docker exec nextcloud-aio-mastercontainer cat /mnt/docker-aio-config/data/configuration.json')
    try:
        config = json.loads(output)
        password = config.get('secrets', {}).get('NEXTCLOUD_PASSWORD')
        if password:
            return jsonify({"NEXTCLOUD_PASSWORD": password})
        else:
            return jsonify({"error": "NEXTCLOUD_PASSWORD not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse JSON output"}), 500

@app.route('/api/reset-rocketchat', methods=['POST'])
def reset_rocketchat():
    async_execute_command('make reset-rocketchat')
    return jsonify({"message": "Reset RocketChat command initiated"}), 202

@app.route('/api/reset-plane', methods=['POST'])
def reset_plane():
    async_execute_command('make reset-plane')
    return jsonify({"message": "Reset Plane command initiated"}), 202

@app.route('/api/reset-gitlab', methods=['POST'])
def reset_gitlab():
    async_execute_command('make reset-gitlab')
    return jsonify({"message": "Reset GitLab command initiated"}), 202

@app.route('/api/reset-nextcloud', methods=['POST'])
def reset_nextcloud():
    async_execute_command('make reset-nextcloud')
    return jsonify({"message": "Reset Nextcloud command initiated"}), 202

@app.route('/api/healthcheck/gitlab', methods=['GET'])
def healthcheck_gitlab():
    code, msg = check_url("http://localhost:8929")
    return jsonify({"message":msg}), code

@app.route('/api/healthcheck/nextcloud', methods=['GET'])
def healthcheck_nextcloud():
    code, msg = check_url("http://localhost:8090")
    return jsonify({"message":msg}), code

@app.route('/api/healthcheck/rocketchat', methods=['GET'])
def healthcheck_rocketchat():
    code, msg = check_url("http://localhost:3000")
    return jsonify({"message":msg}), code

@app.route('/api/healthcheck/plane', methods=['GET'])
def healthcheck_plane():
    code, msg = check_url("http://localhost:8091")
    return jsonify({"message":msg}), code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2999)