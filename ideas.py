import random

ideas = [
    "Freestyle", "Make a video", "Learn a language", "Make a PiHole",
    "Do a backflip", "Make an expensive purchase", "Rawdog a flight",
    "Watch Tiktoks", "Make a new friend", "Take a walk",
    "Watch an episode of Talk Tuah", "Find God", "Text your ex",
    "Talk to your mom", "Eat a burger"]

def get_idea():
    return random.choice(ideas)

user_query = input("Bored? Ask me for an idea! ")

if "idea!" in user_query:
            idea = get_idea()
            print(idea)
            
else:
    print("I don't know what that means. Please try again.")