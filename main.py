import os
import time
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_tharun.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    print(f"flow: {flow}")
    credentials = flow.run_console()
    print(f"credentials: {credentials}")
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey="AIzaSyAoI5m8YhrOXNfZrcCr4bxX3sHvZ7TgXK0")
    print(f"youtube: {youtube}")
    """BjCXfQsNeMLuUi_um9M5 - ZzJ"""
    # prev = -1
    # while True:
    #     request = youtube.videos().list(
    #         part="snippet,contentDetails,statistics",
    #         id="GVGmKoQ_MPI"
    #     )
    #     response = request.execute()
    #     views = response['items'][0]['statistics']['viewCount']
    #
    #     if prev != views:
    #         request1 = youtube.videos().update(
    #             part="snippet,status,localizations",
    #             body={
    #               "id": "GVGmKoQ_MPI",
    #               "localizations": {
    #                 "es": {
    #                   "title": "no hay nada a ver aqui",
    #                   "description": "Esta descripcion es en español."
    #                 }
    #               },
    #               "snippet": {
    #                 "categoryId": 22,
    #                 "defaultLanguage": "en",
    #                 "description": "This description is in English.",
    #                 "tags": [
    #                   "new tags"
    #                 ],
    #                 "title": "This video has " + str(views) + " views"
    #               },
    #               "status": {
    #                 "privacyStatus": "public"
    #               }
    #             }
    #         )
    #         response = request1.execute()
    #         prev = views
    #     time.sleep(10)
    #     print(response)

if __name__ == "__main__":
    main()