import requests
import os
import hashlib
from urllib.parse import urlparse

def get_file_hash(content):
    """Generate SHA256 hash for file content."""
    return hashlib.sha256(content).hexdigest()

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs from user
    urls = input("Please enter image URLs (separate with spaces or newlines):\n").split()

    # Directory for saving images
    os.makedirs("Fetched_Images", exist_ok=True)

    # Keep track of downloaded file hashes to prevent duplicates
    downloaded_hashes = set()

    for url in urls:
        try:
            print(f"\nFetching: {url}")

            # Send request with a timeout
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()

            # Validate Content-Type header
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipped: Not an image (Content-Type: {content_type})")
                continue

            # Validate Content-Length (skip if too large, e.g., > 10MB)
            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > 10 * 1024 * 1024:
                print(f"✗ Skipped: File too large ({int(content_length) / 1024 / 1024:.2f} MB)")
                continue

            # Download the content
            content = response.content

            # Compute hash to check for duplicates
            file_hash = get_file_hash(content)
            if file_hash in downloaded_hashes:
                print("✗ Skipped: Duplicate image detected")
                continue
            downloaded_hashes.add(file_hash)

            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = f"downloaded_{len(downloaded_hashes)}.jpg"

            filepath = os.path.join("Fetched_Images", filename)

            # Save file
            with open(filepath, 'wb') as f:
                f.write(content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")

    print("\nAll downloads complete. Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
