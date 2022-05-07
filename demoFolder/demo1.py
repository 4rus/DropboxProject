import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BHFKfZ0GXlVLwCDjDRwoJGrH3Dg5Xj8T2ldLFnIy-bgGHeLIRu0o9RK4dm2JBzKxs1-0x5ov9N9HIei0qKPG6mTfpQrpoHO9Xdqhxe7eQNDrV3gOBq8eb9AhvKN2KKtZfv_5BqTz8bh3'
    transferData = TransferData(access_token)

    file_from = '1.jpg'
    file_to = '/test_dropbox/test.jpg'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()