# El País BrowserStack Scraper

## Features
✅ Web scraping with Selenium  
✅ Free translation using googletrans  
✅ Download article images  
✅ Text analysis of translated titles  
✅ Designed for BrowserStack testing

## Setup
```bash
git clone <your_repo_url>
cd el-pais-browserstack
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
```

## Run locally
```bash
python main.py
```

## BrowserStack
Sign up: https://www.browserstack.com/users/sign_up  
After getting credentials, configure `browserstack_config.py` (to be added)

## Notes
- Free googletrans used
- Images saved in `images/`
