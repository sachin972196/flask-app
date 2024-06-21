# script.py

import instaloader
from instaloader.exceptions import InstaloaderException

def get_instagram_video_url(url):
    try:
        loader = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(loader.context, url.rsplit('/', 2)[1])
        if post.typename == "GraphVideo":
            video_url = post.video_url
            return True, video_url
        else:
            return False, "No video found at the provided URL."
    except InstaloaderException as e:
        return False, f"Error fetching video URL: {e}"
