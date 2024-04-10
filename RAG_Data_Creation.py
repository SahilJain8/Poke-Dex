from pinecone import  Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv

load_dotenv()
pc = Pinecone(api_key=os.environ['pinecone_key'])

index = pc.list_indexes().names()
print(index)