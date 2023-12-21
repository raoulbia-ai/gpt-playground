from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


def load_model(model_dir):
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForCausalLM.from_pretrained(model_dir)
    generator = pipeline("text-generation", model=model, tokenizewhen did einstein discoverr=tokenizer)
    return generator


def main():
    model_dir = "model_files"  # Replace with your model directory path
    generator = load_model(model_dir)

    print("Starting conversation with Mistral 7B. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting conversation.")
            break

        response = generator(user_input, max_length=50)
        print("Mistral 7B:", response[0]['generated_text'])


if __name__ == "__main__":
    main()
