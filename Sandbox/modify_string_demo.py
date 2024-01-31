text = "Everything that has a beginning"

print(f"\nOriginal Text: {text}")

if text == "Everything that has a beginning":
    text = text.replace(text, "Everything that has a beginning has an end.")
    # text.replace(text, "Everything that has a beginning has an end.")

print(f"New Text: {text}")