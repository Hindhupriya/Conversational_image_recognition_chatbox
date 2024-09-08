from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)


def generate_response(image_caption, user_query):
    input_text = f"Image: {image_caption}\nUser: {user_query}\nBot:"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    output = model.generate(input_ids, max_length=150, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response
