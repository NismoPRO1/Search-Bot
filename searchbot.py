from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Your Google Gemini API Key
gemini_api_key = 'AIzaSyChx4l1SUYQnzjCwOJlH-LzxOafYbM4998'

# Set the Gemini API URL in an environment variable
gemini_api_url = os.getenv('GEMINI_API_URL', 'https://gemini.googleapis.com/v1/search')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    print(f"Received search query: {query}")

    try:
        # Construct the request URL
        url = f"{gemini_api_url}?q={query}&key={gemini_api_key}"
        response = requests.get(url)
        
        # Log status code and response content for debugging
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content}")
        
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
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
