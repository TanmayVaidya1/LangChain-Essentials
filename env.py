from dotenv import load_dotenv, find_dotenv

# Load the first .env file found in the project tree (common env for all modules)
load_dotenv(find_dotenv())
