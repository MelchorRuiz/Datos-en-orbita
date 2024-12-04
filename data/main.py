import os
from capture_screenshots import from_x
from cut_images import crop_images_in_folder
from process_images import process_images

broadcasts = [
  {
    'id': 'flight_6',
    'url' : 'https://x.com/i/broadcasts/1RDGlydZAeOJL',
    'duration': 109,
    'platform': 'x'
  }
]

def get_files(folder_path):
  for root, _, files in os.walk(folder_path):
    if root == folder_path:
      return files

for broadcast in broadcasts:
  if (broadcast['platform'] == 'x'):
    pass
    # from_x(broadcast['url'], broadcast['output_folder'], broadcast['duration'])
  folder_path = 'screenshots/' + broadcast['id']
  files = get_files(folder_path)
  # crop_images_in_folder(files, folder_path, delete_originals=False)
  process_images(broadcast['id'], folder_path, files, delete_originals=False)
