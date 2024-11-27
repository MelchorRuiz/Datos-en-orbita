from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--window-size=1920,1080")

  os.makedirs(output_folder, exist_ok=True)
  
  driver = webdriver.Chrome(options=chrome_options)

  try:
    driver.get(live_url)
    sleep(5)
    
    for _ in range(duration*60):
      timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
      screenshot_path = os.path.join(output_folder, f"screenshot_{timestamp}.png")
      driver.save_screenshot(screenshot_path)
      print(f"Screenshot saved: {screenshot_path}")
      
      sleep(1)
  except Exception as e:
    print(f"An error occurred: {e}")
  finally:
    driver.quit()