RIDDLES = [
    {
        "id": 0,
        "question": "I have keys but no locks. I have a space but no room. You can enter, but never leave. What am I?",
        "answer": "keyboard",
        "hint": "Think about what's in front of you right now."
    },
    {
        "id": 1,
        "question": "What has to be broken before you can use it?",
        "answer": "egg",
        "hint": "It's a common breakfast item."
    },
    {
        "id": 2,
        "question": "I’m tall when I’m young, and I’m short when I’m old. What am I?",
        "answer": "candle",
        "hint": "It provides light and melts over time."
    },
    {
        "id": 3,
        "question": "What month of the year has 28 days?",
        "answer": "all",
        "hint": "Don't overthink the calendar."
    },
    {
        "id": 4,
        "question": "What is full of holes but still holds water?",
        "answer": "sponge",
        "hint": "You use it in the kitchen or bath."
    },
    {
        "id": 5,
        "question": "What question can you never answer yes to?",
        "answer": "are you asleep",
        "hint": "Think about what happens when you are unconscious at night."
    },
    {
        "id": 6,
        "question": "What is always in front of you but can’t be seen?",
        "answer": "future",
        "hint": "It hasn't happened yet."
    },
    {
        "id": 7,
        "question": "There’s a one-story house in which everything is yellow. Yellow walls, yellow doors, yellow furniture. What color are the stairs?",
        "answer": "none",
        "hint": "Read the description of the house carefully."
    },
    {
        "id": 8,
        "question": "What can you break, even if you never pick it up or touch it?",
        "answer": "promise",
        "hint": "It's something you make to someone."
    },
    {
        "id": 9,
        "question": "What goes up but never comes down?",
        "answer": "age",
        "hint": "It changes every birthday."
    },
    {
        "id": 10,
        "question": "A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?",
        "answer": "bald",
        "hint": "Think about his hairstyle."
    },
    {
        "id": 11,
        "question": "What gets wet while drying?",
        "answer": "towel",
        "hint": "You use it after a shower."
    },
    {
        "id": 12,
        "question": "I can be cracked, made, told, and played. What am I?",
        "answer": "joke",
        "hint": "It makes people laugh."
    },
    {
        "id": 13,
        "question": "What has a thumb and four fingers, but is not a hand?",
        "answer": "glove",
        "hint": "You wear it in the winter."
    },
    {
        "id": 14,
        "question": "What has many needles, but cannot sew?",
        "answer": "pine tree",
        "hint": "It's a type of evergreen."
    },
    {
        "id": 15,
        "question": "What has a head and a tail but no body?",
        "answer": "coin",
        "hint": "You use it to buy things or flip for a choice."
    },
    {
        "id": 16,
        "question": "What has many keys but can’t even open a single door?",
        "answer": "piano",
        "hint": "It's a musical instrument."
    },
    {
        "id": 17,
        "question": "What has one eye, but can’t see?",
        "answer": "needle",
        "hint": "You use it for sewing."
    },
    {
        "id": 18,
        "question": "What has legs, but doesn’t walk?",
        "answer": "table",
        "hint": "You eat your dinner on it."
    },
    {
        "id": 19,
        "question": "What has many teeth, but cannot bite?",
        "answer": "comb",
        "hint": "You use it to fix your hair."
    },
    {
        "id": 20,
        "question": "What has words, but never speaks?",
        "answer": "book",
        "hint": "You find these in a library."
    }
]

def get_riddle(level):
    if 0 <= level < len(RIDDLES):
        return RIDDLES[level]
    return None

def get_hint(level):
    riddle = get_riddle(level)
    return riddle.get('hint') if riddle else None

def check_answer(level, user_answer):
    riddle = get_riddle(level)
    if riddle and user_answer.lower().strip() == riddle['answer'].lower():
        return True
    return False
