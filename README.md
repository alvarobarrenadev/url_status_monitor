# URL Status Monitor

This project monitors the status of a list of URLs and logs their availability to a file.

## Requirements

- Python 3.13
- `urllib3` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/alvarobarrena02/url_status_monitor.git
    cd website_conectivity_checker
    ```

2. Install the required library:
    ```sh
    pip install urllib3
    ```

## Usage

1. Run the script to monitor the URLs:
    ```sh
    python main.py
    ```

2. The script will check the status of the URLs and log the results to `status.txt`.

## Configuration

- You can modify the list of URLs to be monitored by editing the `url_list` variable in `main.py`.

## How It Works

- The script uses `urllib3` to send HTTP GET requests to each URL in the list.
- The status of each URL is checked and logged to the console and `status.txt`.
- The script is designed to run continuously, checking the URLs every 5 seconds (currently commented out).

## Example Output

The `status.txt` file will contain entries like:
```
2024-11-12 13:38:53 - https://www.google.com - 200 OK
2024-11-12 13:39:40 - https://www.example.com - 404 Error
```