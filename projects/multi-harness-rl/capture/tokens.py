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



def detokenize(ids, vocab):
    inv = {v: k for k, v in vocab.items()}
    for i in ids:
        if i not in inv:
            raise KeyError(f"unknown token id {i}")
    return ''.join(inv[i] for i in ids)


def drifts(ids, vocab):
    """True if detokenizing then re-tokenizing does not give back the same ids."""
    return tokenize(detokenize(ids, vocab), vocab) != list(ids)
