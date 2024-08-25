from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the T5 model and tokenizer
model_name = "t5-small"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Example text to summarize
example_text = """
Deep learning (also known as deep structured learning) is part of a broader family of machine learning
methods based on artificial neural networks with representation learning. 
Learning can be supervised, semi-supervised or unsupervised. Deep-learning architectures such as 
deep neural networks, deep belief networks, deep reinforcement learning, 
recurrent neural networks and convolutional neural networks have been applied to 
fields including computer vision, speech recognition, natural language processing,
machine translation, bioinformatics, drug design, medical image analysis, 
material inspection and board game programs, where they have produced results 
comparable to and in some cases surpassing human expert performance. 
Artificial neural networks (ANNs) were inspired by information processing and 
distributed communication nodes in biological systems. ANNs have various differences 
from biological brains. Specifically, neural networks tend to be static and symbolic,
while the biological brain of most living organisms is dynamic (plastic) and analogue.
The adjective "deep" in deep learning refers to the use of multiple layers in the network.
Early work showed that a linear perceptron cannot be a universal classifier, 
but that a network with a nonpolynomial activation function with one hidden layer of 
unbounded width can. Deep learning is a modern variation which is concerned with an 
unbounded number of layers of bounded size, which permits practical application and 
optimized implementation, while retaining theoretical universality under mild conditions. 
In deep learning the layers are also permitted to be heterogeneous and to deviate widely 
from biologically informed connectionist models, for the sake of efficiency, trainability 
and understandability, whence the structured part."""

# Preprocess the input text
preprocessed_text = "summarize: " + example_text
inputs = tokenizer.encode(preprocessed_text, return_tensors="pt", max_length=512, truncation=True)

# Generate the summary
summary_ids = model.generate(inputs, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)

# Decode the summarized text
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Print the summary
print("Original Text Length:", len(example_text))
print("\nSummary:")
print(summary)
