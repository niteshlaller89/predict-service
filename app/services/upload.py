from fastapi import UploadFile
from loguru import logger


class UploadService:
    def __init__(self):
        logger.info("init upload service.")

    def start(self, file: UploadFile):
        if not file:
            return {"message": "No upload file sent"}
        else:
            # blob_service_client = BlobServiceClient.from_connection_string(connection_string)
            # blob_client = blob_service_client.get_blob_client(container=container_name, blob=name)

            # try:
            #     contents = file.file.read()
            #     file.file.seek(0)
            #     blob_client.upload_blob(contents)
            # except Exception:
            #     raise HTTPException(status_code=500, detail='Something went wrong')
            # finally:
            #     file.file.close()

            return {"message": "File uploaded successfully to Azure Cloud"}
