from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Route to serve index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to serve send_reaction.html
@app.route('/send_reaction')
def send_reaction_page():
    return render_template('send_reaction.html')

# Route to serve docs.html
@app.route('/docs')
def docs_page():
    return render_template('docs.html')

# Route to handle the POST request from the frontend for sending reactions
@app.route('/api/send_reaction', methods=['POST'])
def send_reaction():
    # Get the data from the request sent from the frontend
    cookie = request.json.get('cookie')
    reaction = request.json.get('reaction')
    link = request.json.get('link')

    # Prepare headers and data for the request
    url = "https://fbpython.click/android_get_react"
    headers = {
        "Host": "fbpython.click",
        "Content-Type": "application/json; charset=utf-8",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.9.1"
    }

    # Use the cookie provided by the user
    data = {
        "reaction": reaction,
        "cookie": cookie,  # The cookie comes from the user input
        "link": link,
        "version": "2.1"
    }

    # Send the POST request to the external API
    response = requests.post(url, json=data, headers=headers)

    # Return the result back to the frontend as JSON
    return jsonify(response.json())

# Route for REST API usage
@app.route('/api/react', methods=['GET'])
def api_react():
    # Get parameters from the query string
    cookie = request.args.get('cookie')
    link = request.args.get('link')
    react = request.args.get('react')

    # Prepare headers and data for the request
    url = "https://fbpython.click/android_get_react"
    headers = {
        "Host": "fbpython.click",
        "Content-Type": "application/json; charset=utf-8",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.9.1"
    }

    data = {
        "reaction": react,
        "cookie": cookie,
        "link": link,
        "version": "2.1"
    }

    # Send the POST request to the external API
    response = requests.post(url, json=data, headers=headers)

    # Return the result back as JSON
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
