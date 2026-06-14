import whisper
import math
import os
import gradio as gr

print("⏳ Loading AI model, please wait...")
model = whisper.load_model("base")
print("✅ Model loaded and ready!")

def seconds_to_srt_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - math.floor(seconds)) * 1000))
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def to_srt(segments):
    lines = []
    for i, seg in enumerate(segments, start=1):
        start = seconds_to_srt_time(seg["start"])
        end = seconds_to_srt_time(seg["end"])
        text = seg["text"].strip()
        lines.append(f"{i}\n{start} --> {end}\n{text}\n")
    return "\n".join(lines)

def convert(audio_file, language):
    if audio_file is None:
        return None, "❌ Please upload an audio file."
    lang_code = {
        "Italian": "it", "English": "en", "Turkish": "tr",
        "Azerbaijani": "az", "Russian": "ru", "Spanish": "es",
        "French": "fr", "German": "de", "Arabic": "ar",
        "Japanese": "ja", "Chinese": "zh", "Portuguese": "pt"
    }[language]
    result = model.transcribe(audio_file, language=lang_code)
    srt_content = to_srt(result["segments"])
    original_name = os.path.splitext(os.path.basename(audio_file))[0]
    srt_path = f"/tmp/{original_name}.srt"
    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content)
    return srt_path, f"✅ Done! '{original_name}.srt' is ready."

custom_css = """
* { box-sizing: border-box; }
body, .gradio-container {
    background-color: #0f0f0f !important;
    color: #f0f0f0 !important;
    font-family: 'Segoe UI', sans-serif !important;
}
.gradio-container {
    max-width: 900px !important;
    margin: 0 auto !important;
    padding: 20px !important;
}
#title {
    text-align: center;
    padding: 40px 0 20px 0;
    border-bottom: 1px solid #2a2a2a;
    margin-bottom: 30px;
}
#title h1 {
    font-size: 2.2em !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    letter-spacing: -0.5px;
}
#title p {
    color: #888 !important;
    font-size: 1em !important;
    margin-top: 8px;
}
.gr-block, .gr-box, .gr-panel {
    background-color: #1a1a1a !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 12px !important;
}
label, .gr-label {
    color: #aaa !important;
    font-size: 0.85em !important;
    font-weight: 500 !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
input, select, textarea, .gr-input, .gr-dropdown {
    background-color: #222 !important;
    border: 1px solid #333 !important;
    color: #f0f0f0 !important;
    border-radius: 8px !important;
}
button.primary {
    background: #ffffff !important;
    color: #000000 !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 1em !important;
    padding: 12px 24px !important;
    cursor: pointer !important;
    transition: opacity 0.2s !important;
}
button.primary:hover { opacity: 0.85 !important; }
#footer {
    text-align: center;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #2a2a2a;
    color: #555 !important;
    font-size: 0.85em;
}
#footer a { color: #888 !important; text-decoration: none; }
"""

with gr.Blocks(css=custom_css, title="MP3 to SRT Converter") as demo:
    gr.Markdown("""
# 🎵 MP3 to SRT Converter
Convert any audio file into SRT subtitles — powered by OpenAI Whisper
    """, elem_id="title")
    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(label="Upload your audio file", type="filepath")
            language_input = gr.Dropdown(
                choices=["English", "Italian", "Turkish", "Azerbaijani", "Russian",
                         "Spanish", "French", "German", "Arabic", "Japanese",
                         "Chinese", "Portuguese"],
                value="English",
                label="Select audio language"
            )
            convert_btn = gr.Button("Convert to SRT →", variant="primary", size="lg")
        with gr.Column():
            status_output = gr.Textbox(label="Status", interactive=False)
            file_output = gr.File(label="Download SRT File")
    gr.Markdown("""
---
**How to use:** Upload audio → Select language → Click Convert → Click filename → Ctrl+S to save

Supported: MP3, WAV, M4A, OGG, FLAC, MP4 &nbsp;|&nbsp; [OpenAI Whisper](https://github.com/openai/whisper)
    """, elem_id="footer")
    convert_btn.click(fn=convert, inputs=[audio_input, language_input], outputs=[file_output, status_output])

demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
