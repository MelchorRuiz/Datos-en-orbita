import os
from capture_screenshots import from_x
from cut_images import process_images_in_folder

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
    from_x(broadcast['url'], broadcast['output_folder'], broadcast['duration'])
  folder_path = 'screenshots/' + broadcast['id']
  files = get_files(folder_path)
  process_images_in_folder(files, folder_path, delete_originals=True)
