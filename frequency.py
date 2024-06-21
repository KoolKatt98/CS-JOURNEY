def word_frequency(text):
  text_lower = text.lower()
  words = text_lower.split()
  frequency = {}

  for word in words:
    if word in frequency:
      frequency[word] += 1
    else:
      frequency[word] = 1

  return frequency

def main():
  text = "Hello world Hello everyone hello cat hello dog"
  print(word_frequency(text))

main()
