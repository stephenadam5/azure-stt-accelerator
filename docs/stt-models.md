# Baseline Speech Models (with Model IDs)

You can optionally specify one of the following baseline models by including the `model` field in your transcription payload.

## Whisper Large V2  
**Release Date:** 2024-02-28  
**Model ID:** `d3529250-b525-4294-9ecd-fcb7e360140d`  
**Notes:** OpenAI Whisper speech model  

## Batch Transcription  
**Release Date:** 2024-12-18  
**Model ID:** `ce71c8c8-ef61-4a09-b198-edd0f6a631df`  
**Notes:** Latest engine for general batch jobs  

## Other Available Models

- **2024-10-01**  
  Model ID: `49850eb7-3a87-460b-87b0-42c38e8abd6e`

- **2024-06-14**  
  Model ID: `7411100d-d474-4336-998a-8add699c20d1`

- **2024-03-27**  
  Model ID: `19891583-6a67-4c0b-bd78-698c06e6055f`

- **2024-02-28 (Whisper Large V2)**  
  Model ID: `7eabb5c6-7c7f-45fb-a0de-2593374180d`

- **2024-01-11**  
  Model ID: `d8071287-0259-aeee-9912-d73f91a2c39b`

- **2023-11-29**  
  Model ID: `e44eb4c4-8d54-4b77-a087-da9894dd42b6`

- **2023-10-05**  
  Model ID: `4e410048-c266-4eb1-be25-faedf905fab7`

- **2023-07-24**  
  Model ID: `3b75a4c2-d814-492c-bbf4-d897fb6c0a65`

- **2023-03-15**  
  Model ID: `2cd371f9-8cf5-4b2e-9193-df4d3247ffd7`

- **2022-11-10**  
  Model ID: `00b43bff-578e-490a-ac5a-d2c454e978a1`  

---

## Example Usage

```json
{
  "model": "ce71c8c8-ef61-4a09-b198-edd0f6a631df",
  "locale": "en-GB",
  "displayName": "transcriptiontest"
}
