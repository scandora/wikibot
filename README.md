```markdown
# Wikibot

Wikibot is a lightweight automation tool that connects to a running Docker host,  
generates a dynamic list of containers, and automatically updates a page on a MediaWiki instance with a live status table.  
It is ideal for self-hosters and infrastructure teams who want live container status documentation without manual updates.

---

## Major Libraries Used

- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/) — Access local Docker containers
- [Requests](https://docs.python-requests.org/en/latest/) — Communicate with MediaWiki API
- [Python-dotenv](https://pypi.org/project/python-dotenv/) — Load environment variables securely

---

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/wikibot.git
    cd wikibot
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory:

    ```dotenv
    WIKI_API_URL=https://your-wiki.example.com/api.php
    WIKI_USERNAME=Wikibot
    WIKI_PASSWORD=your-password
    WIKI_PAGE_TITLE=DockerContainers
    ```

5. (Optional) If using a custom SSL CA, ensure your `.env` path matches your cert setup, or configure trust properly.

---

## Usage

Run the bot manually:

```bash
python3 -m wikibot.main

This will:

    Connect to your local Docker daemon

    Pull live container list

    Format a MediaWiki table

    Update the target page via the MediaWiki API

You can schedule it to run periodically via cron or systemd timers for fully automated updates.

License

MIT License
