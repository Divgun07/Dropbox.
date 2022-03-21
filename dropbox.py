import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BEP8ddM4hBTZamTfcp9WlT0mLiKJ2TeyE-XfgRNq3UjqW53r8QOVFmnZxe9qtOC8g5ig6kWE63tBXvqVZNbyZ6tSuOmf0-ZXEbZ-jPAWyF99_ihtjrWmUrj9-8DGHYL7ytaGfWI'
    transferData = TransferData(access_token)

    file_from = 'text.txt'
    file_to = '/Divgun/text.txt'  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()