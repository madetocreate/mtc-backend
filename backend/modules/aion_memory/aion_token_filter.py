import tiktoken

def count_tokens(text):
  enc = tiktoken.get_encoding("cl100k_base")
  return len(enc.encode(text))

def filter_long_text(text, max_tokens=1000):
  lines = text.split("\n")
  out = []
  for l in lines:
    if count_tokens("\n".join(out + [l])) < max_tokens:
      out.append(l)
    else:
      break
  return "\n".join(out)
