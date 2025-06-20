from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup
from translate import translate_text
from utils import download_image, get_repeated_words
from browserstack_config import get_browserstack_driver

def scrape_articles(username, access_key, browser, os_name, os_version):
    # Set up BrowserStack driver with dynamic browser/OS config
    driver = get_browserstack_driver(
        browser=browser,
        os_name=os_name,
        os_version=os_version,
        username="siddharthsingh_uBV5vj",
        access_key="iyHTqwghxFYoufAsMiBx"
    )

    driver.get("https://elpais.com/")
    assert "España" in driver.page_source or "El País" in driver.title

    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "blockNavigation"))
        )
    except:
        print(" Warning: Overlay still visible, proceeding anyway.")

    try:
        accept_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Accept']"))
        )
        accept_button.click()
        print("Clicked Accept on consent popup.")
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "didomi-popup"))
        )
    except:
        print("No consent popup found or could not close it.")

    opinion_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Opinión')]"))
    )
    opinion_link.click()

    driver.implicitly_wait(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    articles = soup.select("article")[:5]
    original_titles = []

    for idx, article in enumerate(articles):
        title_tag = article.find(["h2", "h3"])
        title = title_tag.get_text(strip=True) if title_tag else f"Title {idx+1}"
        original_titles.append(title)

        print(f"\n📰 Article {idx + 1} Title (Spanish): {title}")

        a_tag = article.find("a")
        link = a_tag["href"] if a_tag and a_tag.has_attr("href") else None
        if not link:
            print("Skipping article due to missing link.")
            continue

        full_link = f"https://elpais.com{link}" if link.startswith("/") else link
        driver.get(full_link)

        article_soup = BeautifulSoup(driver.page_source, "html.parser")
        paragraphs = article_soup.select("p")
        content = "\n".join(p.get_text() for p in paragraphs[:5])
        print(f"Content:\n{content}")

        image = article_soup.find("img")
        if image and image.get("src"):
            img_url = image["src"]
            if img_url.startswith("http"):
                download_image(img_url, f"article_{idx + 1}.jpg")
            else:
                print(f"Skipping non-http image: {img_url[:30]}...")
        else:
            print("No image found for this article.")

    driver.quit()
    return original_titles

def run_translation_and_analysis(titles):
    # Translate each title to English
    translated = [translate_text(title) for title in titles]
    print("\n\n Translated Titles (English):")
    for i, t in enumerate(translated):
        print(f"{i+1}. {t}")

    # Count and print repeated words across all translated titles
    repeated = get_repeated_words(translated)
    print("\n Repeated Words:")
    for word, count in repeated.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    # Example single run (can be removed when using parallel_runner.py)
    USERNAME = "siddharthsingh_uBV5vj"
    ACCESS_KEY = "iyHTqwghxFYoufAsMiBx"
    titles = scrape_articles(USERNAME, ACCESS_KEY, "Chrome", "Windows", "10")
    run_translation_and_analysis(titles)
