import requests

def download_video(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print("Download completed.")
    else:
        print(response.status_code, "Failed to download the video.")

if __name__ == "__main__":
    video_url = "https://13616-2.b.cdn13.com/disk2/movies/Dum%20Laga%20Ke%20Haisha.mp4"
    save_location = "Dum Laga Ke Haisha.mp4"  # Change this to the desired save location

    download_video(video_url, save_location)
