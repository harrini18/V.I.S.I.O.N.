from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests

# Paths
PICS_FOLDER = "trending_pics"

# Create directory if it doesn't exist
if not os.path.exists(PICS_FOLDER):
    os.makedirs(PICS_FOLDER)

# Set up Selenium WebDriver (using Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

def scrape_threads():
    print("Scraping Threads...")
    driver.get("https://www.threads.net/")
    time.sleep(5)

    # Scroll to load more posts
    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    # Find images
    images = driver.find_elements(By.TAG_NAME, "img")
    for idx, img in enumerate(images[:10]):  # Limit to 10 images
        try:
            src = img.get_attribute("src")
            if src and "media" in src:
                img_data = requests.get(src).content
                img_path = os.path.join(PICS_FOLDER, f"threads_pic_{idx}.jpg")
                with open(img_path, "wb") as f:
                    f.write(img_data)
                print(f"Saved {img_path}")
        except Exception as e:
            print(f"Error downloading image {idx}: {str(e)}")

    driver.quit()
    print("Threads scraping complete!")

if __name__ == "__main__":
    scrape_threads()