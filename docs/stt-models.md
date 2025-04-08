## Baseline Speech Models (with Model IDs)

You can optionally specify one of the following **baseline models** by including the `model` field in your transcription payload.

- **Whisper Large V2**
  - Release Date: 2024-02-28
  - Model ID: `d3529250-b525-4294-9ecd-fcb7e360140d`
  - Notes: Whisper-powered speech model

- **Batch Transcription**
  - Release Date: 2024-06-14
  - Model ID: `30888a08-5aec-4034-bfb9-14b7e2898bee`
  - Notes: Latest engine for general batch jobs

- **2024-12-18**
  - Model ID: `6009c964-2cc3-4ec4-bfa9-cc2691a3a06f`

- **2024-10-24**
  - Model ID: `28b864db-276f-48f0-af55-56ebed510c6a`

- **2024-04-17**
  - Model ID: `ea07bcdd-f416-40c2-8bb8-439e8ebd3fd4`

- **2023-10-20**
  - Model ID: `64867906-37f1-41c6-97e0-e464d93e710a`

- **2022-11-10**
  - Model ID: `00b43bff-578e-490a-ac5a-d2c454e978a1`
  - Notes: Older generation model



### Example Usage:
```json
{
  "model": "30888a08-5aec-4034-bfb9-14b7e2898bee",
  "locale": "en-GB",
  "displayName": "transcriptiontest",
}
