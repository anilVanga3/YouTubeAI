import random

# Topics list
TOPICS = [
    "Business ideas in India",
    "Global education insights",
    "Anime updates / recaps / wow moments",
    "Daily world news",
    "Motivational quotes",
    "Sports (cricket-focused)",
    "Health tips, exercises & yoga",
    "Untold history of the world",
    "Facts about the universe"
]

def get_random_topics(n):
    return random.sample(TOPICS, n)