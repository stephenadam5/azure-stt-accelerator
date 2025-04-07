# Azure STT v3.2: `properties` Overview

## Overview

This document describes the configurable `properties` for Azure STT Batch Transcription. These settings allow you to control output formatting, speaker separation, profanity filtering and more.

## Example Transcription Payload

```json
{
  "contentUrls": ["https://example.com/audio.wav"],
  "properties": {
    "diarizationEnabled": true,
    "wordLevelTimestampsEnabled": true,
    "displayFormWordLevelTimestampsEnabled": true,
    "channels": [0, 1],
    "punctuationMode": "DictatedAndAutomatic",
    "profanityFilterMode": "Masked",
    "profanityMarker": "*",
    "wordLevelConfidence": true,
    "timeToLive": "P1D",
    "destinationContainerUrl": "https://yourstorage.blob.core.windows.net/container..."
  },
  "locale": "en-GB",
  "displayName": "testtranscription"
}
```

## **diarizationEnabled**

**What it does:** Tells the system to recognize different speakers.

- `true` = Show separate speakers  
- `false` = Don’t separate speakers (default)

## **wordLevelTimestampsEnabled**

**What it does:** Adds the time each word was spoken.

- `true` = Show timestamps for every word  
- `false` = Don’t show them

## **displayFormWordLevelTimestampsEnabled**

**What it does:** Adds timestamps to text that looks clean (with punctuation and casing).

- Only works if `wordLevelTimestampsEnabled` is `true`  
- `true` = Use formatted text  
- `false` = Use plain text

## **channels**

**What it does:** Choose which audio channels to transcribe.

- Example:  
  - `[0]` = Only the first channel  
  - `[0, 1]` = Both left and right
- If you skip this, it uses all channels.

## **punctuationMode**

**What it does:** Decides how punctuation is added.

- `"None"` = No punctuation  
- `"Dictated"` = Only what was spoken  
- `"DictatedAndAutomatic"` = Spoken + automatic (recommended)

## **profanityFilterMode**

**What it does:** Filters or hides bad words.

- `"Masked"` = Hide with `****`  
- `"Removed"` = Delete them  
- `"Raw"` = Leave as-is

## **destinationContainerUrl**

**What it does:** Tells the system where to save results.

- Use a full SAS URL to an Azure Blob Storage container  
- Example:  
  `https://yourstorage.blob.core.windows.net/container...`

## Other Properties

### **profanityMarker**

**What it does:** Sets the symbol used to mask bad words.

- Example: `"*"` or `"#"`

### **wordLevelConfidence**

**What it does:** Shows how confident the system is for each word.

- `true` = Show confidence  
- `false` = Don’t show (default)

### **timeToLive**

**What it does:** Sets how long the results are saved.

- Format: ISO 8601 (e.g. `"PT1H"` = 1 hour, `"P1D"` = 1 day)  
- Default: 1 day
