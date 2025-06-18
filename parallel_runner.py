from concurrent.futures import ThreadPoolExecutor
from main import scrape_articles, run_translation_and_analysis

USERNAME = "siddharthsingh_uBV5vj"
ACCESS_KEY = "iyHTqwghxFYoufAsMiBx"

# 5 different browser + OS combos
configs = [
    {"browser": "Chrome", "os_name": "Windows", "os_version": "10"},
    {"browser": "Firefox", "os_name": "Windows", "os_version": "11"},
    {"browser": "Safari", "os_name": "OS X", "os_version": "Monterey"},
    {"browser": "Chrome", "os_name": "Android", "os_version": "12.0"},
    {"browser": "Safari", "os_name": "iOS", "os_version": "15"}
]

def task_runner(cfg):
    print(f"\n🚀 Starting test: {cfg}")
    titles = scrape_articles(
        USERNAME,
        ACCESS_KEY,
        cfg["browser"],
        cfg["os_name"],
        cfg["os_version"]
    )
    run_translation_and_analysis(titles)
    print(f"✅ Finished test: {cfg}")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(task_runner, configs)
