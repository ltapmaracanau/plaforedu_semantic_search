import torch
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import json


class SemanticSearchEngine:
    def __init__(self, model_name='ricardo-filho/bert-base-portuguese-cased-nli-assin-2', use_gpu=torch.cuda.is_available()):
        self.model = SentenceTransformer(model_name)
        if use_gpu:
            self.model = self.model.to('cuda') 
        self.dimension = self.model.get_sentence_embedding_dimension()
        self.index = faiss.IndexFlatIP(self.dimension)
        self.id_to_data = {}

    def add_entries(self, entries):
        ids, descriptions = zip(*entries)
        embeddings = self.model.encode(descriptions, convert_to_tensor=True, normalize_embeddings=True)
        if torch.cuda.is_available():
            embeddings = embeddings.cpu()
        embeddings = embeddings.numpy()
        self.index.add(embeddings)
        for entry_id, description in zip(ids, descriptions):
            self.id_to_data[entry_id] = description

    def search(self, query_text, top_k=5):
        query_embedding = self.model.encode([query_text], convert_to_tensor=True, normalize_embeddings=True)
        if torch.cuda.is_available():
            query_embedding = query_embedding.cpu()
        query_embedding = query_embedding.numpy()
        distances, indices = self.index.search(query_embedding, top_k)
        results = [(list(self.id_to_data.keys())[idx], self.id_to_data[list(self.id_to_data.keys())[idx]], float(distance)) for idx, distance in zip(indices[0], distances[0])]
        return sorted(results, key=lambda x: x[2], reverse=True)

    def save_index(self, file_path):
        faiss.write_index(self.index, file_path + '.index')
        with open(file_path + '.json', 'w') as f:
            json.dump(self.id_to_data, f)

    def load_index(self, file_path):
        self.index = faiss.read_index(file_path + '.index')
        with open(file_path + '.json', 'r') as f:
            self.id_to_data = json.load(f)
