from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import urllib.request

# Set up the toy car (Selenium)
driver = webdriver.Chrome()  # You need Chrome and a ChromeDriver installed
driver.get("https://www.instagram.com/explore/")

# Wait for the page to load (like waiting for a toy to start)
time.sleep(5)

# Find pictures (look for <img> tags)
images = driver.find_elements(By.TAG_NAME, "img")

# Make a folder to save pictures
if not os.path.exists("trending_pics"):
    os.makedirs("trending_pics")

# Save each picture
for i, img in enumerate(images):
    src = img.get_attribute("src")  # Get the picture's URL
    if src:
        urllib.request.urlretrieve(src, f"trending_pics/pic_{i}.jpg")
        print(f"Saved picture {i}")

# Close the toy car
driver.quit()