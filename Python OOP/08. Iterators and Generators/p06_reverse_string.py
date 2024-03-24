def reverse_text(text: str):
    current_index = len(text) - 1
    start_index = 0
    while current_index >= start_index:
        yield text[current_index]
        current_index -= 1
