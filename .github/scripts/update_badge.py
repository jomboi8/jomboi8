import os
import urllib.request
import sys

def update_badge():
    url = "https://tryhackme.com/api/v2/badges/public-profile?userPublicId=2970720"
    output_path = os.path.join("assets", "tryhackme-badge.png")
    
    try:
        print(f"Downloading badge from {url}...")
        # Add a User-Agent header to avoid 403 Forbidden errors
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        )
        with urllib.request.urlopen(req) as response, open(output_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Badge saved to {output_path}")
    except Exception as e:
        print(f"Error downloading badge: {e}")
        sys.exit(1)

if __name__ == "__main__":
    update_badge()
