import sys
import requests
import json
sys.path.append(r'..')
from task_handler import url_second, url_third

##  DOWNLOAD TASK CONTENT
task_content = requests.get(url_second)
task_content_parsed = json.loads(task_content.text)
question = task_content_parsed["question"]

## PREPARING A RESPONSE
url = "https://unknow.news/archiwum_aidevs.json"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
response = requests.get(url, headers=headers)

content = json.loads(response.text)

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from uuid import uuid4
from qdrant_client import QdrantClient
import json

COLLECTION_NAME = "ai_devs_search_task"

qdrant = QdrantClient(url="http://localhost:6333")
embeddings = OpenAIEmbeddings()
result = qdrant.get_collections()
indexed = next((collection for collection in result.collections if collection.name == COLLECTION_NAME), None)
print(result)

if not indexed:
    qdrant.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config={"size": 1536, "distance": "Cosine", "on_disk": True},
    )

collection_info = qdrant.get_collection(collection_name=COLLECTION_NAME)

from langchain.docstore.document import Document
if not collection_info.points_count:
    
    documents = []
    for element in content:
        document = Document(page_content=element['info'])
        document.metadata["title"] = element['title']
        document.metadata["url"] = element['url']
        document.metadata["date"] = element['date']
        document.metadata["info"] = element['info']
        document.metadata["source"] = COLLECTION_NAME
        document.metadata["uuid"] = str(uuid4())
        documents.append(document)

    points = []
    for document in documents:
        embedding = embeddings.embed_documents([document.page_content])[0]
        points.append(
            {
                "id": document.metadata["uuid"],
                "payload": document.metadata,
                "vector": embedding,
            }
        )

    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        wait=True,
        points=points,
    )

query_embedding = embeddings.embed_query(question)

search_result = qdrant.search(
    collection_name=COLLECTION_NAME,
    query_vector=query_embedding,
    limit=1,
    query_filter={"must": [{"key": "source", "match": {"value": COLLECTION_NAME}}]},
)

for result in search_result:
    print("ID: ", result.id)
    print("Score: ", result.score)
    print(json.dumps(result.payload, indent=4, ensure_ascii=False))

## SENDING THE REPONSE
response_third = requests.post(url_third, json = {"answer": result.payload['url']})
print(response_third.text)