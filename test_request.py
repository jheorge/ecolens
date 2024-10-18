import requests
import os


def get_image_path():
    # Get the directory of the current script
    dir = os.path.dirname(__file__)
    # Construct the full path to the image
    image_path = os.path.join(dir, 'images', 'test-3.jpg')
    print(image_path)  # Optional: Print the path to verify it's correct
    return image_path

# Endpoint URL
url = 'http://localhost:5000/process-image'
image_path = get_image_path()
# Open the image file in binary mode
with open(image_path, 'rb') as image_file:
    # Create a dictionary with the file
    files = {'image': image_file}
    
    # Send the POST request
    response = requests.post(url, files=files)

# Print the response from the server
print(response.text)    