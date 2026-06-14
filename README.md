MP3 to SRT Converter

Convert MP3 audio files to SRT subtitle files using OpenAI Whisper — free, no installation needed.

---

 User Guide

**Step 1 — Run Cell 1**
Click ▶, wait until ✅ appears. Whisper and FFmpeg will be installed (~2 minutes).

**Step 2 — Run Cell 2**
Wait until "✅ Model loaded and ready!" appears.

**Step 3 — Run Cell 3**
- Select the language of your audio from the dropdown
- Click "Browse and select your MP3 file"
- Select and upload your MP3 file
- Wait — your SRT file will download automatically

**Step 4 — Done!**
Your `.srt` file is ready in your Downloads folder.

> ⚠️ When the file picker opens, always select a file — never close it without choosing!

---

## ⚙️ How It Works

**FFmpeg** splits the audio into processable chunks.

**OpenAI Whisper** converts each chunk into text using AI trained on 680,000 hours of audio.

**Timestamp calculator** finds the exact start and end time of each sentence.

**SRT formatter** writes everything into subtitle blocks and saves as `.srt`.

---

## 🌍 Supported Languages

| Language | Code |
|----------|------|
| Italian | `it` |
| English | `en` |
| Turkish | `tr` |
| Russian | `ru` |
| Spanish | `es` |
| French | `fr` |
| German | `de` |
| Arabic | `ar` |
| Japanese | `ja` |
| Chinese | `zh` |
| Portuguese | `pt` |

---

## 📁 Supported Input Formats

MP3, WAV, M4A, OGG, FLAC, MP4

---

## ⚠️ Notes

- First run takes ~2 minutes (model download)
- Free Google Colab has limited GPU time
- Large files may take longer to process

---

## 🛠️ Built With

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Google Colab](https://colab.research.google.com)
