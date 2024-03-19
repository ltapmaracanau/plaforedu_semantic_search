from flask import Flask, request, jsonify
from search import SemanticSearchEngine
import torch

app = Flask(__name__)

search_engine = SemanticSearchEngine(use_gpu=torch.cuda.is_available())
search_engine.load_index('cursos')

@app.route('/')
def hello_world():
    return 'PlaforEDU Semantic Search'

@app.route('/search', methods=['GET'])
def search():
    query_text = request.args.get('query_text', '')
    top_k = request.args.get('top_k', 5, type=int)
    results = search_engine.search(query_text, top_k=top_k)
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
