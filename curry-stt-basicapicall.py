import time
import requests
from tqdm import tqdm

SPEECH_SUBSCRIPTION_KEY = "" 
SPEECH_ENDPOINT = ""  
DESTINATION_CONTAINER_URL = (
    ""
)


TEST_WAV_URL = (
    ""
)

def create_transcription(audio_url, subscription_key, endpoint, destination_url):
    """
    Creates a transcription job via Azure Speech-to-Text REST API.
    Returns a dict containing the job resource info, or None on error.
    """
    url = "https://swedencentral.api.cognitive.microsoft.com/speechtotext/v3.2/transcriptions"
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/json"
    }

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
        "displayName": "Debug Transcription"
    }

    try:
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
            resp = requests.get(status_url, headers=headers)
            resp.raise_for_status()
            status_info = resp.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting transcription status: {e}")
            return None

        status = status_info.get("status")
        if status == "Succeeded":
            files_url = status_info["links"]["files"]
            try:
                files_resp = requests.get(files_url, headers=headers)
                files_resp.raise_for_status()
                return files_resp.json()
            except requests.exceptions.RequestException as e:
                print(f"Error getting final files: {e}")
                return None

        elif status in ("Running", "NotStarted"):
            elapsed = int(time.time() - start_time)
            if elapsed % 30 == 0:
                print(f"Transcription still in progress... elapsed={elapsed}s")
            time.sleep(5)

        elif status == "Failed":
            print("Transcription job failed.")
            return status_info
        else:
            print("Unexpected status:", status)
            return status_info

def main():
    print("Creating transcription job...")
    creation_result = create_transcription(
        audio_url=TEST_WAV_URL,
        subscription_key=SPEECH_SUBSCRIPTION_KEY,
        endpoint=SPEECH_ENDPOINT,
        destination_url=DESTINATION_CONTAINER_URL
    )
    if not creation_result:
        print("Job creation failed; cannot continue.")
        return

    status_url = creation_result["self"]
    print(f"Polling transcription status at: {status_url}")

    result = get_transcription_result(status_url, SPEECH_SUBSCRIPTION_KEY)
    if not result:
        print("No result obtained. Check logs.")
        return

    print("\n TRANSCRIPTION RESULT FILES:")
    for item in result.get("values", []):
        print(f"- Name: {item.get('name')}")
        print(f"  Kind: {item.get('kind')}")
        print(f"  Links: {item.get('links')}")
        print()

if __name__ == "__main__":
    main()
