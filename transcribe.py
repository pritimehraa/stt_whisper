import gradio as gr
import whisper

model = whisper.load_model("base")

def transcribe(audio):
    if audio is None:
        return "Please upload an audio file."
    result = model.transcribe(audio)
    return result["text"]

with gr.Blocks(theme=gr.themes.Default()) as demo:
    gr.Markdown("# Convert Audio To Text")
    with gr.Row():
        audio_input = gr.Audio(type="filepath", label="Upload an audio file")
        output_text = gr.Textbox(label="Transcription Output", interactive=False)
    with gr.Row():
        transcribe_btn = gr.Button("Transcribe")
        clear_btn = gr.ClearButton([audio_input, output_text])
    
    transcribe_btn.click(transcribe, inputs=[audio_input], outputs=[output_text])
demo.launch()
