import random

knowledge = {
    "artificial intelligence": [
        "Artificial Intelligence (AI) is a branch of computer science "
        "that enables machines to perform tasks requiring human intelligence."
    ],

    "machine learning": [
        "Machine Learning is a subset of AI that allows computers "
        "to learn from data and improve their performance."
    ],

    "deep learning": [
        "Deep Learning is a subset of Machine Learning that uses "
        "multi-layered neural networks to learn complex patterns."
    ],

    "neural network": [
        "A Neural Network is a computing system inspired by the "
        "human brain. It consists of connected artificial neurons."
    ],

    "types of ai": [
        "The three commonly discussed types of AI are Narrow AI, "
        "General AI and Super AI."
    ],

    "narrow ai": [
        "Narrow AI is designed to perform a specific task. "
        "Examples include voice assistants and recommendation systems."
    ],

    "general ai": [
        "General AI refers to a theoretical AI system that could "
        "perform a wide range of intellectual tasks like a human."
    ],

    "super ai": [
        "Super AI is a hypothetical form of AI that would exceed "
        "human intelligence in almost every area."
    ],

    "applications of ai": [
        "AI is used in healthcare, education, banking, agriculture, "
        "transportation, robotics and entertainment."
    ],

    "advantages of ai": [
        "Advantages of AI include automation, faster decision-making, "
        "reduced human effort and improved accuracy in many tasks."
    ],

    "disadvantages of ai": [
        "Disadvantages include high development costs, privacy concerns, "
        "job displacement, bias and dependence on technology."
    ],

    "examples of ai": [
        "Examples of AI include ChatGPT, Google Assistant, "
        "face recognition, recommendation systems and self-driving cars."
    ],

    "supervised learning": [
        "Supervised Learning trains a model using labelled data. "
        "The model learns from input-output examples."
    ],

    "unsupervised learning": [
        "Unsupervised Learning uses unlabelled data to discover "
        "hidden patterns and groups."
    ],

    "reinforcement learning": [
        "Reinforcement Learning allows an agent to learn through "
        "rewards and penalties."
    ],

    "what is chatbot": [
        "A chatbot is a software application that communicates "
        "with users through text or voice."
    ]
}


def get_response(message):

    question = message.lower().strip()

    if not question:
        return "Please enter a question."

    if any(word in question for word in ["hello", "hi", "hey"]):
        return "Hello! Welcome to AI Basics Chatbot. What would you like to learn about AI?"

    if "your name" in question or "who are you" in question:
        return "I am AI Basics Chatbot, an educational assistant designed to explain Artificial Intelligence concepts."

    if "thank" in question:
        return "You're welcome! Keep learning about Artificial Intelligence."

    if "bye" in question:
        return "Goodbye! Thank you for using AI Basics Chatbot."

    # Find matching topic
    for topic, answers in knowledge.items():

        if topic in question:
            return random.choice(answers)

    # Additional keyword matching
    if "what is ai" in question or "define ai" in question:
        return knowledge["artificial intelligence"][0]

    if "what is ml" in question or "define ml" in question:
        return knowledge["machine learning"][0]

    if "what is dl" in question:
        return knowledge["deep learning"][0]

    return (
        "Sorry, I don't have an answer for that question yet. "
        "Please ask about Artificial Intelligence, Machine Learning, "
        "Deep Learning, Neural Networks or AI applications."
    )