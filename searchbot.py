from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

api_key = 'AIzaSyCHypa5gHM29KNDoa7Y6f17WhUV7MJ9t4I'
cse_id = '645b315c8a32c4605'

def google_search(query, api_key, cse_id):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}"
    response = requests.get(url)
    results = response.json()
    return results

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    search_results = google_search(query, api_key, cse_id)
    
    # Extract useful information from the Google Search results
    if 'items' in search_results:
        answer = search_results['items'][0]['snippet']  # The first result's snippet
        link = search_results['items'][0]['link']  # The first result's URL
    else:
        answer = "No results found."
        link = "#"

    return jsonify({'answer': answer, 'link': link})

if __name__ == "__main__":
    app.run(debug=True)
