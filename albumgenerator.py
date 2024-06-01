def get_project_url(username):
    return f"https://1001albumsgenerator.com/api/v1/projects/{clean_username(username)}"


def clean_username(username):
    return username.lower().strip().replace(" ", "-")
