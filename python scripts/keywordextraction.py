# Install required packages
import sys
!{sys.executable} -m pip install --upgrade git+https://github.com/UKPLab/sentence-transformers
!{sys.executable} -m pip install keybert ctransformers[cuda]
!{sys.executable} -m pip install --upgrade git+https://github.com/huggingface/transformers

from ctransformers import AutoModelForCausalLM
from transformers import AutoTokenizer, pipeline
from keybert.llm import TextGeneration
from keybert import KeyLLM, KeyBERT

# Load model
model = AutoModelForCausalLM.from_pretrained(
    "TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
    model_file="mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    model_type="mistral",
    gpu_layers=50,
    hf=True
)

# Tokenizer
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")

# Pipeline
generator = pipeline(
    model=model, tokenizer=tokenizer,
    task='text-generation',
    max_new_tokens=50,
    repetition_penalty=1.1
)

# Load it in KeyLLM
llm = TextGeneration(generator, prompt=prompt)
kw_model = KeyLLM(llm)

documents = [
    "Massive flocks of greater and lesser flamingos are often associated with the saline and alkaline lakes of Kenya and Tanzania. While greater flamingos can inhabit both saltwater and freshwater habitats, lesser flamingos are found in saline waters, and the species is considered “near threatened” by the International Union for Conservation of Nature. India has the largest population of lesser flamingos outside the African continent, mostly in the salt deserts of the western state of Gujarat. There are few historical records of flamingos in Mumbai; one from 1891 suggests they were an occasional bird of passage in the region.",
]

keywords = kw_model.extract_keywords(documents)

# Load it in KeyLLM
kw_model = KeyBERT(llm=llm, model='BAAI/bge-small-en-v1.5')

# Extract keywords
keywords = kw_model.extract_keywords(documents, threshold=.5)

print(keywords)
