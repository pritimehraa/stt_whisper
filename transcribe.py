import gradio as gr
import whisper

model = whisper.load_model("base")
file_name = "s.m4a"  

def transcribe_file():
    try:
        result = model.transcribe(file_name)
        return result["text"]
    except Exception as e:
        return f"Error: {e}"

with gr.Blocks(theme=gr.themes.Default()) as demo:
    gr.Markdown("## 🎧 Converted Audio to Text")
    
    output_text = gr.Textbox(
        label="Transcription Output",
        value=transcribe_file(),
        lines=15,
        interactive=False
    )
demo.launch()