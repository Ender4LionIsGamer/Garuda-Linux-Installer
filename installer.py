print("Garuda Linux ISO Installer")
print("Please Relax While It Installs!")
# imported the requests library
import requests
iso_url = "https://sourceforge.net/projects/garuda-linux/files/garuda/dr460nized/220101/garuda-dr460nized-linux-zen-220101.iso/download"
  
# URL of the image to be downloaded is defined as image_url
r = requests.get(iso_url) # create HTTP response object
  
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("garuda-dr460nized-linux-zen-220101.iso",'wb') as f:
  
    # Saving received content as a png file in
    # binary format
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)
print("Installed garuda-dr460nized-linux-zen-220101.iso!")
