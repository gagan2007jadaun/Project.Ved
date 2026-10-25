# Polymorphism
'''
Polymorphism ka meaning hai “one interface, multiple forms.” Matlab, same method name different classes mein different behaviour perform kar sakta hai.
1. Real-world example
Project VED mein imagine kar ki hum different AI models ko run karna chahte hain. Har model ka run() method ho sakta hai, lekin har model apna kaam alag tareeke se karega.
'''

class ChatModel:
    def run(self):
        print("ChatModel is generating text.")

class ImageModel:
    def run(self):
        print("ImageModel is generating on Image.")

class AudioModel:
    def run(self):
        print("AudioModel is processing audio.")

# Create objects
models = [
    ChatModel(),
    ImageModel(),
    AudioModel()
]

# Same method, different behaviour
for model in models:
    model.run()

'''
Ye kaise work karta hai?
1. Teeno classes mein run() method hai.
2. models list mein different classes ke objects hain.
3. Loop har object par run() call karta hai.
4. Python us object ki class ke corresponding method ko execute karta hai.
Is approach se hum common interface ke through different objects ke saath kaam kar sakte hain.
'''