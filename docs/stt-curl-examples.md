# 🛰️ Sample `curl` Commands for Azure STT API

This document contains concise `curl` examples for using Azure's Speech-to-Text Batch Transcription API.

---

## 📤 Create a Transcription Job

```bash
curl -X POST "https://<REGION>.api.cognitive.microsoft.com/speechtotext/v3.2/transcriptions" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/json" \
  -d @payload.json
```

---

## 🔄 Check Job Status

```bash
curl -X GET "https://<REGION>.api.cognitive.microsoft.com/speechtotext/v3.2/transcriptions/<TRANSCRIPTION_ID>" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY"
```

---

## 📂 Get Transcription Result Files

```bash
curl -X GET "https://<REGION>.api.cognitive.microsoft.com/speechtotext/v3.2/transcriptions/<TRANSCRIPTION_ID>/files" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY"
```
