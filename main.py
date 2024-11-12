import urllib3
import time
from datetime import datetime

# Initialize urllib3 and url lists
http = urllib3.PoolManager()
url_list = ["https://open.spotify.com/", "https://www.google.com/", "https://x.com/"]

# Function to check the status of the URL
def check_url_status(url):
    try:
        # Get the response from the URL
        response = http.request('GET', url)

        # Verify the response status
        if response.status == 200:
            return f"{response.status} OK"
        else:
            return f"{response.status} Error"
    except Exception as e:
        return f"Error: {e}"

# Main function to monitor the URLs
def monitor_urls():
    # List to hold statuses
    statuses = []
    # Check the status of the URLs
    for url in url_list:
        status = check_url_status(url)
        statuses.append((url, status))
        print(f"{datetime.now()} - {url}: {status}")
    
    # Write the statuses to a file
    with open("status.txt", "a") as file:
        for url, status in statuses:
            file.write(f"{datetime.now()} - {url}: {status}\n")

# Main loop to monitor the URLs every 5 seconds
# while True:
#     monitor_urls()
#     time.sleep(5)

# Run the main loop
if __name__ == "__main__":
    monitor_urls()