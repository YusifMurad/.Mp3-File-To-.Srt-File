İşte son README — GitHub'da README.md'yi aç, içini tamamen sil, bunu yapıştır:
markdown# 🎵 MP3 to SRT Converter

Convert MP3 audio files to SRT subtitle files using OpenAI Whisper — free, no installation needed.

## 🚀 Try it Live

👉 [Open on Hugging Face Spaces](https://huggingface.co/spaces/YusifMurad/mp3-to-srt-converter)

---

## 📖 User Guide

**Step 1 — Open the app**
Click the link above to open the app on Hugging Face Spaces.

**Step 2 — Upload your file**
- Select the language of your audio from the dropdown
- Upload your audio file
- Click **Convert to SRT →**

**Step 3 — Download your SRT**
- Click the filename (e.g. `audio.srt`) under **Download SRT File**
- A new tab will open showing the subtitle text
- Press **Ctrl+S** (Windows) or **Cmd+S** (Mac) to save the file

> ⚠️ Make sure to run Cell 1 fully before running Cell 2 if using Google Colab!

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
| Azerbaijani | `az` |
| Russian | `ru` |
| Spanish | `es` |
| French | `fr` |
| German | `de` |
| Arabic | `ar` |
| Japanese | `ja` |
| Chinese | `zh` |
| Portuguese | `pt` |

---

## 📁 Files

| File | Purpose |
|------|---------|
| `Mp3toSrt.ipynb` | Open in Google Colab to run manually |
| `app.py` | Powers the Hugging Face Space |
| `requirements.txt` | Python dependencies |

---

## 📁 Supported Input Formats

MP3, WAV, M4A, OGG, FLAC, MP4

---

## ⚠️ Notes

- First run takes ~2 minutes (model download)
- Free Google Colab has limited GPU time
- Large files may take longer to process
- The public link expires after 1 week — simply re-run Cell 2 to get a new one

---

## 🛠️ Built With

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Google Colab](https://colab.research.google.com)
- [Gradio](https://gradio.app)
- [Hugging Face Spaces](https://yusifmurad-mp3-to-srt-converter.hf.space/)
