class ModelConfig:
    def __init__(self,  model_name, learning_rate):
        self.model_name = model_name
        self.__learning_rate = learning_rate
    def get_learning_rate(self):
            return self.__learning_rate
    
    def set_learning_rate(self, new_rate):
        if 0 < new_rate <= 1:
            self.__learning_rate = new_rate
            print("Learning rate updated successfully!")
        else:
            print("Error: Learning rate must be between 0 and 1.")
    def show_config(self):
        print("Model Name:", self.model_name)
        print("Learning rate:",self.__learning_rate)

# Create model
model = ModelConfig("VED-CL", 0.01)
model.show_config()
print("\nCurrent MOdel Learning Rate:", model.get_learning_rate())

# Updat with a valid value
model.set_learning_rate(1.00)
model.show_config()

# Try to with invalid value
model.set_learning_rate(1.20)