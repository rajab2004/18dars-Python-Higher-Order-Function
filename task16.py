malumotlar = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

sozlar = filter(
    lambda element: isinstance(element, str) and len(element) > 5,
    malumotlar
)

print(list(sozlar))

