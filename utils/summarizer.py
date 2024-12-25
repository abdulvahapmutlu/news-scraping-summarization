from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load the FLAN-T5-XL model and tokenizer
model_name = "google/flan-t5-xl"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to("cuda")

def summarize_text_flan_t5(text, min_length=50, max_length=200):
    """
    Summarizes the input text using the FLAN-T5-XL model.
    Args:
        text (str): The text to summarize.
        min_length (int): Minimum length of the summary.
        max_length (int): Maximum length of the summary.
    Returns:
        str: Summarized text.
    """
    try:
        input_chunks = [text[i:i+400] for i in range(0, len(text), 400)]
        summaries = []
        for chunk in input_chunks:
            input_text = f"summarize: {chunk}"
            inputs = tokenizer(
                input_text,
                return_tensors="pt",
                truncation=True,
                max_length=512,
                padding="longest"
            ).to("cuda")
            summary_ids = model.generate(
                inputs.input_ids,
                max_length=max_length,
                min_length=min_length,
                num_beams=5,
                early_stopping=True
            )
            summaries.append(tokenizer.decode(summary_ids[0], skip_special_tokens=True))
        return " ".join(summaries)
    except Exception as e:
        print(f"An error occurred during summarization: {e}")
        return "Summarization failed."
