from pytube import YouTube
link = input("Enter the link: ")
file_loc = input("Enter the file loction: ")
print("Downloading...")
YouTube(link).streams.first().download('file_loc')
print("Video downloaded successfully")
