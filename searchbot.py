from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your new Google Gemini API Key
gemini_api_key = 'AIzaSyChx4l1SUYQnzjCwOJlH-LzxOafYbM4998'

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    print(f"Received search query: {query}")

    try:
        # Example API call to Google Gemini (replace with actual endpoint if needed)
        url = f"https://gemini.googleapis.com/v1/search?q={query}&key={gemini_api_key}"
        response = requests.get(url)
        search_results = response.json()
        
        # Process the results
        if 'results' in search_results and len(search_results['results']) > 0:
            answer = search_results['results'][0]['snippet']  # Adjust based on Gemini response
            link = search_results['results'][0]['link']  # Adjust based on Gemini response
        else:
            answer = "No results found."
            link = "#"

        return jsonify({'answer': answer, 'link': link})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Something went wrong'}), 500
