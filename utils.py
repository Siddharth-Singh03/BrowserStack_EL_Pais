import requests
import os

def download_image(url, filename, folder="images"):
    # Make sure the images folder exists (create if missing)
    os.makedirs(folder, exist_ok=True)
    try:
        # Fetch the image from the provided URL
        response = requests.get(url)
        if response.status_code == 200:
            # Save image content to a file
            with open(os.path.join(folder, filename), "wb") as f:
                f.write(response.content)
            print(f"Image saved: {filename}")
        else:
            print(f"Failed to download image: {url}")
    except Exception as e:
        # Catch and print any errors during download
        print(f"Error downloading image: {e}")

def get_repeated_words(text_list):
    from collections import Counter
    # Combine all titles into a single string, lowercase for uniformity
    words = " ".join(text_list).lower().split()
    counter = Counter(words)
    # Return words that occur more than twice
    return {word: count for word, count in counter.items() if count > 2}
