from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load text file
loader = TextLoader("data.txt", encoding="utf-8")
documents = loader.load()

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

docs = text_splitter.split_documents(documents)

print(f"Total chunks created: {len(docs)}")
print(docs[0].page_content)  # Print first chunk