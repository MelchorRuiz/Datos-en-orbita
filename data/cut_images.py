import cv2
import os

def crop_image(filename, folder_path, output_folder, crop_coords):
  """
  Crop a specific region from an image using OpenCV.

  Args:
    filename (str): Name of the image file.
    folder_path (str): Path to the folder containing the image file.
    output_folder (str): Path to the folder where the cropped image will be saved.
    crop_coords (tuple): Coordinates for cropping the image in the format (x, y, width, height).
  """
  try:
    image_path = os.path.join(folder_path, filename)
    image = cv2.imread(image_path)

    if image is None:
      raise ValueError(f"Cannot load image: {image_path}")
    
    x, y, width, height = crop_coords
    cropped_image = image[y:y + height, x:x + width]

    if cropped_image is not None:
      output_path = os.path.join(output_folder, filename)
      cv2.imwrite(output_path, cropped_image)
      print(f"Processed and saved: {output_path}")
    else:
      print(f"Skipping file due to error: {image_path}")
      
  except Exception as e:
    print(f"Error cropping image {image_path}: {e}")

def process_images_in_folder(files, folder_path,delete_originals=False):
  """
  Process all image files in a folder by cropping them based on the given coordinates.

  Args:
    files (list): List of image files in the folder.
    folder_path (str): Path to the folder containing the image files.
    delete_originals (bool): Whether to delete the original images after processing.
  """
  
  def get_output_folder(folder):
    output_folder = os.path.join(folder_path, folder)
    os.makedirs(output_folder, exist_ok=True)
    return output_folder
    
  try:
    output_folder_time = get_output_folder('time')
    output_folder_spped_superheavy = get_output_folder('speed_superheavy')
    output_folder_altitude_superheavy = get_output_folder('altitude_superheavy')
    output_folder_speed_starship = get_output_folder('speed_starship')
    output_folder_altitude_starship = get_output_folder('altitude_starship')

    for filename in files:
      crop_image(filename, folder_path, output_folder_time, (1283, 525, 94, 16))
      crop_image(filename, folder_path, output_folder_spped_superheavy, (1224, 507, 64, 12))
      crop_image(filename, folder_path, output_folder_altitude_superheavy, (1043, 524, 46, 12))
      crop_image(filename, folder_path, output_folder_speed_starship, (1578, 508, 64, 12))
      crop_image(filename, folder_path, output_folder_altitude_starship, (1596, 524, 46, 12))

      if delete_originals:
        os.remove(os.path.join(folder_path, filename))

  except Exception as e:
    print(f"Error processing folder {folder_path}: {e}")
