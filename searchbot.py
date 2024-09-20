from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your API Key and Custom Search Engine (CSE) ID
api_key = 'AIzaSyCHypa5gHM29KNDoa7Y6f17WhUV7MJ9t4I'
cse_id = '645b315c8a32c4605'

def google_search(query, api_key, cse_id):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}"
    response = requests.get(url)
    results = response.json()
    return results

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')  # Get the search query from the frontend
    search_results = google_search(query, api_key, cse_id)
    
    # Extract the first result snippet and link from the Google Search API response
    if 'items' in search_results:
        answer = search_results['items'][0]['snippet']  # First result snippet
        link = search_results['items'][0]['link']  # First result URL
    else:
        answer = "No results found."
        link = "#"

    # Return a JSON response with the answer and link
    return jsonify({'answer': answer, 'link': link})

if __name__ == "__main__":
    app.run(debug=True)
