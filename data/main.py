from capture_screenshots import from_x

# Capture screenshots from a live stream on X

broadcasts = [
  {
    'url' : 'https://x.com/i/broadcasts/1RDGlydZAeOJL',
    'output_folder' : 'screenshots/flight_6',
    'duration': 109,
    'platform': 'x'
  }
]

for broadcast in broadcasts:
  if (broadcast['platform'] == 'x'):
    from_x(broadcast['url'], broadcast['output_folder'], broadcast['duration'])
