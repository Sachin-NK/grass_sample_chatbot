import gradio as gr
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the model
model = T5ForConditionalGeneration.from_pretrained('./grass_gis_chatbot_model')
tokenizer = T5Tokenizer.from_pretrained('./grass_gis_chatbot_model')

def generate_response(user_input):
    prompt = "gis: " + user_input.strip()
    input_ids = tokenizer(prompt, return_tensors='pt').input_ids

    output_ids = model.generate(
        input_ids,
        max_length=64,
        repetition_penalty=2.5,      # reduce repeated tokens
        num_beams=5,                 
        early_stopping=True,
        no_repeat_ngram_size=2      
    )

    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return response



interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Ask something about GRASS GIS..."),
    outputs="text",
    title="GRASS GIS Chatbot"
)

interface.launch()
