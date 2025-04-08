# Azure Speech-to-Text Versioning

### 1. **Speech SDK**
- **Use for**: Real-time transcription, microphone input, interactive apps.
- **Languages**: Python, C#, JavaScript, Java, C++ and more.
- **Features**: 
  - Streaming transcription
  - Easy integration of advanced features (diarization, custom models etc.)
  - Works with audio streams and files

---

### 2. **Batch Transcription (REST API - v3.x)**
- **Use for**: Long audio files (minutes to hours) and async processing.
- **Endpoint Format**: https://[REGION].api.cognitive.microsoft.com/speechtotext/v3.2/transcriptions
- **Versions**:
- **v3.0** – Initial batch API version
- **v3.1** – Minor improvements, better error handling
- **v3.2** – Recommended version  
  - Advanced options: `displayFormWordLevelTimestampsEnabled`, better punctuation, multi-channel support etc.
- **Workflow**:
1. Submit audio + settings (as JSON)
2. Poll job status
3. Download result files from Azure Storage


## Deprecated / Legacy

### Bing Speech API (Predecessor)
- Deprecated and replaced by Azure Cognitive Services.

### Cognitive Services Speech v1
- Legacy REST API with limited features.
