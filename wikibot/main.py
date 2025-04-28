import os
from dotenv import load_dotenv

from wikibot.docker_client import DockerClient
from wikibot.generator import generate_wiki_table
from wikibot.wiki_client import WikiClient

# --- Load environment variables ---
load_dotenv()

API_URL = os.getenv("WIKI_API_URL")
USERNAME = os.getenv("WIKI_USERNAME")
PASSWORD = os.getenv("WIKI_PASSWORD")
PAGE_TITLE = os.getenv("WIKI_PAGE_TITLE")

def main():
    docker_client = DockerClient()
    containers = docker_client.list_containers()
    wiki_table = generate_wiki_table(containers)

    wiki = WikiClient(API_URL, USERNAME, PASSWORD)
    wiki.update_page(PAGE_TITLE, wiki_table)

if __name__ == "__main__":
    main()

