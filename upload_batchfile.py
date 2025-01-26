from openai import OpenAI
from store_requests import BATCHFILE

def upload_batchfile(filename):
    client = OpenAI()

    batch_input_file = client.files.create(
        file=open(filename, "rb"),
        purpose="batch"
    )

    print("Input File Details")
    print("\t📁 Name", batch_input_file.filename)
    print("\t🆔 ID", batch_input_file.id)
    print("\t💾 Bytes", batch_input_file.bytes)
    print("\t📊 Status", batch_input_file.status)

    return batch_input_file

if __name__ == "__main__":
    upload_batchfile(BATCHFILE)
