import time
import requests

# Replace the following values with your own Azure Speech resource information
SPEECH_SUBSCRIPTION_KEY = "[YOUR_SUBSCRIPTION_KEY]"
SPEECH_ENDPOINT = "[YOUR_ENDPOINT]"
DESTINATION_CONTAINER_URL = "[YOUR_DESTINATION_CONTAINER_URL]"
TEST_WAV_URL = "[YOUR_TEST_WAV_URL]"

def create_transcription(audio_url, subscription_key, endpoint, destination_url):
    url = "https://[REGION].api.cognitive.microsoft.com/speechtotext/v3.2/transcriptions"
    # The header must contain the subscription key and specify JSON content.
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/json"
    }

    # The payload configures transcription properties:
    #  - contentUrls: the audio file(s) to transcribe
    #  - diarizationEnabled: whether to separate speakers (False here)
    #  - wordLevelTimestampsEnabled: whether to include word-level timestamps (False here)
    #  - channels: which audio channels to transcribe (here, channels 0 & 1)
    #  - punctuationMode: how punctuation is handled
    #  - profanityFilterMode: how profanity is handled
    #  - destinationContainerUrl: where to place result files
    #  - locale: specifies language/locale (en-GB here)
    #  - displayName: a friendly name for the transcription job
    
    payload = {
        "contentUrls": [audio_url],
        "properties": {
            "diarizationEnabled": False,
            "wordLevelTimestampsEnabled": False,
            "displayFormWordLevelTimestampsEnabled": False,
            "channels": [0, 1],
            "punctuationMode": "DictatedAndAutomatic",
            "profanityFilterMode": "Masked",
            "destinationContainerUrl": destination_url
        },
        "locale": "en-GB",
        "displayName": "transcriptiontest"
    }

    try:
        # Create a transcription job via a POST request.
        resp = requests.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating transcription job: {e}")
        if resp is not None:
            print(f"Response status code: {resp.status_code}, body: {resp.text}")
        return None

def get_transcription_result(status_url, subscription_key):
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    start_time = time.time()

    while True:
        try:
            # Check the current status of our transcription job with a GET request.
            resp = requests.get(status_url, headers=headers)
            resp.raise_for_status()
            status_info = resp.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting transcription status: {e}")
            return None

        # The 'status' field can be NotStarted, Running, Succeeded or Failed.
        status = status_info.get("status")
        
        if status == "Succeeded":
            # If succeeded, retrieve the files link that should contain the final transcripts
            files_url = status_info["links"]["files"]
            try:
                files_resp = requests.get(files_url, headers=headers)
                files_resp.raise_for_status()
                return files_resp.json()
            except requests.exceptions.RequestException as e:
                print(f"Error getting final files: {e}")
                return None

        elif status in ("Running", "NotStarted"):
             # If still running, keep waiting and polling.
            # We only print a status message every 30 seconds.
            elapsed = int(time.time() - start_time)
            if elapsed % 30 == 0:
                print(f"Transcription still in progress... elapsed={elapsed}s")
            time.sleep(5)

        elif status == "Failed":
            # If job has failed, print the status info and stop polling.
            print("Transcription job failed.")
            return status_info
        else:
            print("Unexpected status:", status)
            return status_info

def main():
    # Main function to:
    # 1. Create a transcription job
    # 2. Poll its status
    # 3. Print out the final files (if any) when complete
    print("Creating transcription job...")
    # 1. Create the transcription job
    creation_result = create_transcription(
        audio_url=TEST_WAV_URL,
        subscription_key=SPEECH_SUBSCRIPTION_KEY,
        endpoint=SPEECH_ENDPOINT,
        destination_url=DESTINATION_CONTAINER_URL
    )

    # If creation fails, we cannot proceed
    if not creation_result:
        print("Job creation failed; cannot continue.")
        return

    # The 'self' link from the creation result is used to poll the status
    status_url = creation_result["self"]
    print(f"Polling transcription status at: {status_url}")

    # 2. Poll for the final result
    result = get_transcription_result(status_url, SPEECH_SUBSCRIPTION_KEY)
    if not result:
        print("No result obtained. Check logs.")
        return

    # 3. Print the resulting file information if transcription succeeded
    print("\n TRANSCRIPTION RESULT FILES:")
    for item in result.get("values", []):
        print(f"- Name: {item.get('name')}")
        print(f"  Kind: {item.get('kind')}")
        print(f"  Links: {item.get('links')}")
        print()

if __name__ == "__main__":
    main()
