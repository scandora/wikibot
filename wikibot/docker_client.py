import docker

class DockerClient:
    def __init__(self):
        self.client = docker.from_env()

    def list_containers(self):
        containers_info = []

        for container in self.client.containers.list():
            info = {
                "name": container.name,
                "image": container.image.tags[0] if container.image.tags else container.image.short_id,
                "traefik_url": self.extract_traefik_url(container),
            }
            containers_info.append(info)

        return containers_info

    def extract_traefik_url(self, container):
        labels = container.labels or {}

        # Look for typical Traefik router Host rule
        for key, value in labels.items():
            if key.startswith("traefik.http.routers.") and key.endswith(".rule"):
                if "Host(`" in value:
                    start = value.find("Host(`") + len("Host(`")
                    end = value.find("`)", start)
                    if start > 0 and end > start:
                        return f"https://{value[start:end]}"
        return None
