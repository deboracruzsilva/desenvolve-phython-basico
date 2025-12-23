import emoji

print("Emojis disponíveis:")
print(emoji.emojize(':thumbs_up:')," - :thumbs_up:" )
print(emoji.emojize(':red_heart:')," - :red_heart:" )
print(emoji.emojize(':thinking_face:')," - :thinking_face:" )
print(emoji.emojize(':partying_face:')," - :partying_face:" )
print(emoji.emojize(':smiling_face_with_hearts:')," - :smiling_face_with_hearts:" )
print(emoji.emojize(':sparkles:')," - :sparkles:" )

frase = input("Digite uma frase e ela será emogizada: ")
print("n\Frase emogizada:")
print(emoji.emojize(frase, language='alias'))

