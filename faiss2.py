import faiss
from llama_index.core import (
    SimpleDirectoryReader,
    load_index_from_storage,
    VectorStoreIndex,
    StorageContext,
)
from llama_index.vector_stores.faiss import FaissVectorStore

d = 1536
faiss_index = faiss.IndexFlatL2(d)

documents = SimpleDirectoryReader("docs").load_data()

vector_store = FaissVectorStore(faiss_index=faiss_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)
  
# save index to disk
index.storage_context.persist()

query_engine = index.as_query_engine()
