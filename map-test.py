import sys,webbrowser

address = ' '.join(sys.argv[1:])

if len(sys.argv) > 1:
  address = ' '.join(sys.argv[1:])
# else:
#   address = pypaperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

