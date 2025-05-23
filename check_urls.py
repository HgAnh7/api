from flask import Flask, request, jsonify
import re
import requests
import os

app = Flask(__name__)

@app.route('/check-urls', methods=['POST'])
def check_urls():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text field in request'}), 400

    content = data['text']
    urls = re.findall(r'https?://[^\s]+', content)

    working_urls = []
    broken_urls = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for url in urls:
        try:
            response = requests.head(url, headers=headers, timeout=5, allow_redirects=True)
            if response.status_code == 200:
                working_urls.append(url)
            else:
                broken_urls.append({'url': url, 'status': response.status_code})
        except Exception as e:
            broken_urls.append({'url': url, 'error': str(e)})

    return jsonify({
        'total': len(urls),
        'working': working_urls,
        'broken': broken_urls
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
