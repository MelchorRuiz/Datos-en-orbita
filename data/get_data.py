from selenium import webdriver
from PIL import Image
from io import BytesIO
from time import sleep
import os
from datetime import datetime
from cut_image import divide_image

def from_x(live_url, duration=10):
  """
  Capture screenshots from a live stream on X using Selenium.

  Args:
      live_url (str): URL of the live stream on X.
      duration (int): Duration in minutes to capture screenshots.
  """
  options = webdriver.FirefoxOptions()
  options.add_argument("--headless")
  options.add_argument("--window-size=1920,1080")
  
  driver = webdriver.Firefox(options=options)

  try:
    driver.get(live_url)
    sleep(5)
    
    for _ in range(duration*60):
      screensot = driver.get_screenshot_as_png()
      image = Image.open(BytesIO(screensot))

      cropped_images = divide_image(image)
      time = datetime.now().strftime("%Y%m%d%H%M%S")
      for part, cropped_image in cropped_images.items():
        cropped_image.save(f"screenshots/{time}_{part}.png")

      sleep(1)
  except Exception as e:
    print(f"An error occurred: {e}")
  finally:
    driver.quit()