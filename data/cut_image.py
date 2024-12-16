import cv2
import os

def divide_image(image):
  """
  Divide an image into 5 parts and return a dictionary with these parts.

  Args:
      image (PIL.Image): The image to divide.

  Returns:
      dict: A dictionary with 5 parts of the image.
  """
  parts = {
    'time': (1283, 525, 94, 16),
    'speed_superheavy': (1224, 507, 64, 12),
    'altitude_superheavy': (1043, 524, 46, 12),
    'speed_starship': (1578, 508, 64, 12),
    'altitude_starship': (1596, 524, 46, 12)
  }
  
  cropped_images = {}

  for part, coordinates in parts.items():
    x, y, w, h = coordinates
    cropped_images[part] = image.crop((x, y, x+w, y+h))
  
  return cropped_images