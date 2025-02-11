def main():
    # Prompt user for file name and convert to lowercase for case-insensitivity
    file_name = input("Enter the file name: ").strip().lower()

    # Define a dictionary for known file extensions and their corresponding media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Check the file extension in the media_types dictionary
    for extension in media_types:
        if file_name.endswith(extension):
            print(media_types[extension])
            return

    # Default to application/octet-stream if no known extension is found
    print("application/octet-stream")

# Run the main function
if __name__ == "__main__":
    main()
