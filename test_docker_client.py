from wikibot.docker_client import DockerClient
import pprint

def main():
    client = DockerClient()
    containers = client.list_containers()

    pprint.pprint(containers)

if __name__ == "__main__":
    main()
