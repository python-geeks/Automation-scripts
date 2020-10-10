import torch
import torch.nn as nn
import torch.nn.functional as F

import re

device = torch.device("cpu")


class NGramModel(nn.Module):
    """
    A simple Neural Network - for the sake of this tutorial
    """

    def __init__(self, vocab_size, embedding_dim, context_size):
        super(NGramModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.linear1 = nn.Linear(context_size * embedding_dim, 128)
        self.linear2 = nn.Linear(128, vocab_size)

    def forward(self, inputs):
        embeds = self.embedding(inputs).view((1, -1))
        x = F.relu(self.linear1(embeds))
        x = self.linear2(x)
        log_probs = F.log_softmax(x, dim=1)
        return log_probs


def make_inference(model, inputs, word_dict):
    # Re-map dict
    reverted_dict = dict(map(reversed, word_ixs.items()))

    model.eval()
    with torch.no_grad():
        # Processing input
        idxs = torch.tensor(
            [word_dict[w] for w in inputs], dtype=torch.long, device=device
        )

        # Forward pass
        log_probs = model(idxs)

        # Obtain probs
        probs = torch.exp(log_probs)

        # obtain prediction
        _, pred = torch.max(probs, 1)

        # Obtain predicted word index
        pred_idx = pred.detach().cpu().numpy()[0]

        # Get predicted word from remapped dict
        out = reverted_dict[pred_idx]

    return pred_idx, out


def generate_text_ngram(model, inputs, word_dict, n_words):
    # Preprocess input
    inputs = inputs.lower().split()

    # Get n, to slice out last n words from the predicted sentence
    n = len(inputs)

    # Keep track of predicted words
    pred_sent = inputs
    # Collect pred indexes
    pred_idxs = []

    for w in range(n_words):
        pred_idx, pred_w = make_inference(model, inputs, word_dict)
        pred_sent.append(pred_w)
        pred_idxs.append(pred_idx)
        inputs = pred_sent[-n:]

    return pred_sent, pred_idxs


if __name__ == "__main__":
    with open("tale_of_2_cities.txt", "r", encoding="utf-8") as f:
        book = f.read()

    # Replace newline characters
    book = re.sub("\n", " ", book)
    book = re.sub("\ufeff", "", book)

    # Preprocess text
    train_text = book.lower().split()

    # create vocabulary
    vocabulary = set(train_text)
    vocab_len = len(vocabulary)

    # Create word tokens
    word_ixs = {word: i for i, word in enumerate(vocabulary)}

    # Making ngrams is also easy, you should be using (n-1) in slicing
    def make_n_grams(text, n):
        return [(text[i: i + n], text[i + n]) for i in range(len(text) - n)]

    # Define hyperparameters
    N = 8
    EMBED_DIM = 32
    CONTEXT_LEN = N

    # create ngrams
    n_grams = make_n_grams(train_text, N)

    model = NGramModel(vocab_len, EMBED_DIM, CONTEXT_LEN).to(device)
    model.load_state_dict(torch.load("ngram_model_trained.ckpt"))

    d_sents = [
        "Yes, sir. We have oftentimes the honour to",
        "You know that your parents had a great",
        "London is a place where I'd love to",
        "A large cask of wine has been dropped",
    ]

    print("Choose from default sentences or enter you own!")
    option = input("Enter 1 to choose from defaults: ")

    if option == "1":
        print("Here are the default sentences...")
        print("=====================================================")
        print(f"Sentence 1 - {d_sents[0]}")
        print(f"Sentence 2 - {d_sents[1]}")
        print(f"Sentence 3 - {d_sents[2]}")
        print(f"Sentence 4 - {d_sents[3]}")
        print("=====================================================")
        choice = int(input("Enter your choice (1-4): ")) - 1
        input_text = d_sents[choice]
    else:
        input_text = input("""Please enter an 8 word sentence
                            (Since loaded model uses 8-gram):""")

    n_seq = int(input("Enter number of more words to generate: "))

    if len(input_text.split()) < 8:
        raise("""Please enter an 8 word sentence
              to start with or choose from defaults!!!""")

    out = " ".join(generate_text_ngram(model, input_text, word_ixs, n_seq)[0])

    print(f"""\n\nThe Generated Text is: \n============================\n{out}
          \n============================""")
