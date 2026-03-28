# lumina_mood.py

def lumina_response(mood):
    responses = {
        "sad": "Don't be sad. God loves you and has a purpose for your life.",
        "worried": "Have peace in God. He carries your worries. Rest in Him.",
        "happy": "I'm glad you're happy. Keep shining, God created you with joy.",
        "afraid": "Do not be afraid. God is always with you."
    }
    return responses.get(mood, "God bless you.")


mood = input("Hello, how are you feeling today? ").strip().lower()

print(lumina_response(mood))