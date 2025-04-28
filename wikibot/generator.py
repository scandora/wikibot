from datetime import datetime

def generate_wiki_table(containers):
    """
    Generates MediaWiki table markup for a list of container dictionaries,
    and includes an 'Updated' timestamp at the top.
    """

    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    table = []
    table.append(f"''Updated: {now}''")  # Italicized timestamp
    table.append("")
    table.append('{| class="wikitable"')
    table.append('|+ Docker Containers')
    table.append('! Container !! Image !! Traefik URL')

    for container in containers:
        name = container.get("name", "")
        image = container.get("image", "")
        traefik_url = container.get("traefik_url")

        if traefik_url:
            url_markup = f"[{traefik_url} {traefik_url.replace('https://', '')}]"
        else:
            url_markup = "—"  # dash if no URL

        table.append('|-')
        table.append(f'| {name} || {image} || {url_markup}')

    table.append('|}')

    return "\n".join(table)

