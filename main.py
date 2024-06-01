
def generate_spotify_app_url(spotifyId):
    return f"spotify:album:{spotifyId}"

def get_project_url(username):
    username = username.lower().strip().replace(" ", "-")
    return f"https://1001albumsgenerator.com/api/v1/projects/{username}"

def main():

