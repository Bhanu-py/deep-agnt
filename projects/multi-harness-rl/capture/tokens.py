def tokenize(text, vocab):
    """Greedy longest-match tokenizer: at each position take the longest vocab entry
    that is a prefix of the remaining text. Unknown characters map to '<unk>'."""
    max_len = max((len(t) for t in vocab), default=1)
    ids = []
    i = 0
    while i < len(text):
        for length in range(min(max_len, len(text) - i), 0, -1):
            piece = text[i:i + length]
            if piece in vocab:
                ids.append(vocab[piece])
                i += length
                break
        else:
            ids.append(vocab["<unk>"])
            i += 1
    return ids
