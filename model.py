from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.llms.llama_cpp.llama_utils import (
    messages_to_prompt,
    completion_to_prompt
)

model_url = 'https://huggingface.co/TheBloke/saiga_mistral_7b-GGUF/resolve/main/saiga_mistral_7b.Q4_K_M.gguf'

llm = LlamaCPP(
    # You can pass in the URL to a GGML model to download it automatically
    model_url=None,
    # optionally, you can set the path to a pre-downloaded model instead of model_url
    model_path='/content/saiga_mistral_7b.Q5_K_S.gguf',
    max_new_tokens=4000,
    context_window=20000,
    generate_kwargs={},
    model_kwargs={"n_gpu_layers": -1,
                  "cache":True,
                  "use_mmap":True},
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=True
)

def gen_stream(text):
  response_iter = llm.stream_complete(text)
  for response in response_iter:
      print(response, end="", flush=True)

