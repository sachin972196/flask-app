import instaloader
from instaloader.exceptions import InstaloaderException, QueryReturnedNotFoundException

def get_instagram_video_url(url):
    try:
        loader = instaloader.Instaloader()
        # Authenticate with your Instagram credentials
        # Replace 'your_username' and 'your_password' with your actual credentials
        loader.login('python_code121', 'sachin@sach123')
        
        # Fetch post details
        post = instaloader.Post.from_shortcode(loader.context, url.rsplit('/', 2)[1])
        
        if post.typename == "GraphVideo":
            video_url = post.video_url
            return True, video_url
        else:
            return False, "No video found at the provided URL."
    
    except QueryReturnedNotFoundException:
        return False, "Instagram post not found."
    
    except InstaloaderException as e:
        return False, f"Error fetching video URL: {e}"
