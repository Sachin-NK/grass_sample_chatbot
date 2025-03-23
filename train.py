from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
from datasets import Dataset
from dataset import get_dataset
import torch

# Load dataset
raw_data = get_dataset()
dataset = Dataset.from_dict({
    'input': [item['input'] for item in raw_data],
    'output': [item['output'] for item in raw_data]
})

# Load tokenizer and model
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

# Preprocess the data
def preprocess(example):
    input_encoding = tokenizer(example['input'], padding='max_length', truncation=True, max_length=128, return_tensors="pt")
    target_encoding = tokenizer(example['output'], padding='max_length', truncation=True, max_length=128, return_tensors="pt")

    labels = target_encoding['input_ids']
    labels[labels == tokenizer.pad_token_id] = -100  # ignore padding in loss

    return {
        'input_ids': input_encoding['input_ids'].squeeze(),
        'attention_mask': input_encoding['attention_mask'].squeeze(),
        'labels': labels.squeeze()
    }

tokenized_dataset = dataset.map(preprocess)

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=15,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir='./logs',
    learning_rate=3e-4,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    eval_dataset=tokenized_dataset,
)

# Train
trainer.train()

# Save model
model.save_pretrained('./grass_gis_chatbot_model')
tokenizer.save_pretrained('./grass_gis_chatbot_model')
