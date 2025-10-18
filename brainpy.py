import os
import google.generativeai as genai

class PersonalAI:
    def __init__(self):
        """
        Initializes the AI with memory and configures the Gemini API.
        """
        self.memory = {}
        try:
            # Configure the Gemini API using an environment variable
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                print("GEMINI_API_KEY environment variable not found.")
                # Handle the case where the API key is not set
                self.model = None
            else:
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')
                print("PersonalAI brain initialized. Memory is empty. Gemini model loaded.")
        except Exception as e:
            print(f"Error initializing Gemini model: {e}")
            self.model = None

    def learn(self, key, value):
        """
        Adds or updates a piece of information in the AI's memory.
        """
        self.memory[key.lower()] = value
        return f"Okay, I've learned that '{key}' is '{value}'."

    def recall(self, key):
        """
        Retrieves a piece of information from the AI's memory.
        """
        return self.memory.get(key.lower(), f"Sorry, I don't have any information about '{key}'.")

    def forget(self, key):
        """
        Removes a piece of information from the AI's memory.
        """
        if key.lower() in self.memory:
            del self.memory[key.lower()]
            return f"I have forgotten about '{key}'."
        else:
            return f"I can't forget about '{key}' because I don't know anything about it."

    def get_generative_response(self, prompt):
        """
        Gets a conversational response from the Gemini API.
        """
        if not self.model:
            return "Sorry, the generative AI model is not configured. Please check your API key."
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error getting response from Gemini: {e}")
            return "Sorry, I'm having trouble thinking right now."


    def process_input(self, user_input):
        """
        Parses the user's input and decides which action to take.
        If it's not a known command, it sends the input to the Gemini model.
        """
        parts = user_input.lower().strip().split()

        if len(parts) < 1:
            return "I'm listening."
            
        command = parts[0]
        
        # Command: "learn that [key] is [value]" or "remember that [key] is [value]"
        if (command == "learn" or command == "remember") and "that" in user_input and " is " in user_input:
            try:
                key_part = user_input.split(" that ")[1].split(" is ")[0]
                value_part = user_input.split(" is ")[1]
                return self.learn(key_part, value_part)
            except IndexError:
                return "The 'learn' command format is: 'learn that [key] is [value]'."

        # Command: "what is [key]" or "recall [key]"
        elif command == "what" and len(parts) > 1 and parts[1] == "is":
            key = " ".join(parts[2:]).replace('?', '')
            return self.recall(key)
        elif command == "recall" and len(parts) > 1:
            key = " ".join(parts[1:])
            return self.recall(key)

        # Command: "forget [key]"
        elif command == "forget" and len(parts) > 1:
            key = " ".join(parts[1:])
            return self.forget(key)

        # If it's not a specific command, send it to the generative AI
        else:
            return self.get_generative_response(user_input)


# ... (The __main__ block for terminal testing can remain the same)
if __name__ == '__main__':
    ai = PersonalAI()
    # ... rest of the test code
