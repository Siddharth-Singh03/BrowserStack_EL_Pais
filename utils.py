
import requests
import os

def download_image(url, filename, folder="images"):
    os.makedirs(folder, exist_ok=True)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(folder, filename), "wb") as f:
                f.write(response.content)
            print(f"✅ Image saved: {filename}")
        else:
            print(f"❌ Failed to download image: {url}")
    except Exception as e:
        print(f"❌ Error downloading image: {e}")

def get_repeated_words(text_list):
    from collections import Counter
    words = " ".join(text_list).lower().split()
    counter = Counter(words)
    return {word: count for word, count in counter.items() if count > 2}
