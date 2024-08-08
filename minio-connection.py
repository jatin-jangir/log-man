from minio import Minio
from minio.error import S3Error

def main():
    # Initialize a Minio client
    client = Minio(
        "localhost:31422",  # Replace with your MinIO server URL
        access_key="ZK1KrWTumiVmPcHvs35e",
        secret_key="Uw5mbs2oJKnsMTsWtsnyutRXQT1FiCR80IcBN8xZ",
        secure=False    # Set to False if you're not using HTTPS
    )

    # Bucket name
    bucket_name = "logs"

    # Create a new bucket if it doesn't exist
    try:
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created successfully.")
        else:
            print(f"Bucket '{bucket_name}' already exists.")
    except S3Error as e:
        print(f"Error occurred: {e}")
        return

    # File to upload
    file_path = "hello.txt"
    object_name = "hello.txt"

    # Create a simple text file
    with open(file_path, "w") as file:
        file.write("Hello, MinIO!")

    # Upload the file
    try:
        client.fput_object(bucket_name, object_name, file_path)
        print(f"File '{file_path}' uploaded successfully to bucket '{bucket_name}'.")
    except S3Error as e:
        print(f"Error occurred while uploading the file: {e}")
        return

    # Download the file
    downloaded_file_path = "downloaded_hello.txt"

    try:
        client.fget_object(bucket_name, object_name, downloaded_file_path)
        print(f"File '{object_name}' downloaded successfully as '{downloaded_file_path}'.")
    except S3Error as e:
        print(f"Error occurred while downloading the file: {e}")
        return

    # Read and print the contents of the downloaded file
    with open(downloaded_file_path, "r") as file:
        content = file.read()
        print("File Content:", content)

if __name__ == "__main__":
    main()
