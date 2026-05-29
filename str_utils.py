def slugify(text):
    return "-".join(text.lower().split())


def truncate(text, n):
    return text if len(text) <= n else text[: n - 1] + "…"
