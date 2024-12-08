import nltk
import random
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

class Chatbot:
    def __init__(self):
        # Define some basic responses
        self.responses = {
            "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"],
            "goodbye": ["Goodbye! Have a great day!", "Bye! Feel free to come back if you need help."],
            "thank_you": ["You're welcome!", "No problem!"],
            "default": ["Sorry, I didn't understand that. Could you ask something else?", "I'm not sure how to respond to that."]
        }
        
    def greet(self):
        """Handle greeting"""
        return random.choice(self.responses["greeting"])
    
    def farewell(self):
        """Handle goodbye"""
        return random.choice(self.responses["goodbye"])
    
    def thank_you_response(self):
        """Handle thank you"""
        return random.choice(self.responses["thank_you"])
    
    def default_response(self):
        """Handle unknown responses"""
        return random.choice(self.responses["default"])
    
    def preprocess_input(self, user_input):
        """Preprocess the input to remove stopwords and punctuation"""
        user_input = user_input.lower()  # Convert to lowercase
        tokens = word_tokenize(user_input)  # Tokenize the input
        tokens = [word for word in tokens if word not in stopwords.words('english') and word not in string.punctuation]
        return tokens
    
    def analyze_input(self, user_input):
        """Analyze the user's input and decide the response"""
        tokens = self.preprocess_input(user_input)
        
        # Simple rule-based keyword matching
        if "hello" in tokens or "hi" in tokens:
            return self.greet()
        elif "bye" in tokens or "goodbye" in tokens:
            return self.farewell()
        elif "thank" in tokens:
            return self.thank_you_response()
        else:
            return self.default_response()

    def chat(self):
        """Main loop for the chatbot to interact with the user"""
        print("Chatbot: Hi, I'm your assistant. Type 'bye' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'bye':
                print(f"Chatbot: {self.farewell()}")
                break
            response = self.analyze_input(user_input)
            print(f"Chatbot: {response}")

# Create an instance of the chatbot
if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()
