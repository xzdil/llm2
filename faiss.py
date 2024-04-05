from llama_index.core import set_global_tokenizer
from transformers import AutoTokenizer
from model import llm

set_global_tokenizer(
    AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-chat-hf").encode
)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

from llama_index.core import SimpleDirectoryReader
documents = SimpleDirectoryReader('docs').load_data()

index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

query_engine = index.as_query_engine(llm=llm,streaming=True)
