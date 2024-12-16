from selenium import webdriver
from PIL import Image
from io import BytesIO
from time import sleep
import os
from datetime import datetime

def from_x(live_url, output_folder, duration=10):
  """
  Capture screenshots from a live stream on X using Selenium.

  Args:
      live_url (str): URL of the live stream on X.
      output_folder (str): Folder to save the screenshots.
      duration (int): Duration in minutes to capture screenshots.
  """
  options = webdriver.FirefoxOptions()
  options.add_argument("--headless")
  options.add_argument("--window-size=1920,1080")

  os.makedirs(output_folder, exist_ok=True)
  
  driver = webdriver.Firefox()

  try:
    driver.get(live_url)
    sleep(5)
    
    for _ in range(duration*60):
      screensot = driver.get_screenshot_as_png()
      image = Image.open(BytesIO(screensot))

      image.show()

      sleep(1)
  except Exception as e:
    print(f"An error occurred: {e}")
  finally:
    driver.quit()