import emoji

message = input("Input: ")

emojified_message = emoji.emojize(message, language="alias")

print("Output:", emojified_message)
