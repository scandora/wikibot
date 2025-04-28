import requests

class WikiClient:
    def __init__(self, api_url, username, password):
        self.api_url = api_url
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.verify = "/home/docker/src/wikibot/scandora_root_ca.crt"
        self.logged_in = False

    def login(self):
        # Step 1: Get login token
        r1 = self.session.get(self.api_url, params={
            "action": "query",
            "meta": "tokens",
            "type": "login",
            "format": "json"
        })
        r1.raise_for_status()
        login_token = r1.json()["query"]["tokens"]["logintoken"]

        # Step 2: Send login request
        r2 = self.session.post(self.api_url, data={
            "action": "login",
            "lgname": self.username,
            "lgpassword": self.password,
            "lgtoken": login_token,
            "format": "json"
        })
        r2.raise_for_status()
        result = r2.json()

        if result.get("login", {}).get("result") == "Success":
            self.logged_in = True
            print(f"Logged in as {self.username}")
        else:
            raise Exception(f"Login failed: {result}")

    def get_csrf_token(self):
        r = self.session.get(self.api_url, params={
            "action": "query",
            "meta": "tokens",
            "format": "json"
        })
        r.raise_for_status()
        return r.json()["query"]["tokens"]["csrftoken"]

    def update_page(self, page_title, new_content, summary="Automated update by wikibot"):
        if not self.logged_in:
            self.login()

        csrf_token = self.get_csrf_token()

        r = self.session.post(self.api_url, data={
            "action": "edit",
            "title": page_title,
            "text": new_content,
            "token": csrf_token,
            "format": "json",
            "summary": summary
        })
        r.raise_for_status()
        result = r.json()

        if "edit" in result and result["edit"]["result"] == "Success":
            print(f"Page '{page_title}' updated successfully.")
        else:
            raise Exception(f"Failed to edit page: {result}")
