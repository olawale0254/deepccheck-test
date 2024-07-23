import json

import requests

# Base URL of the API
BASE_URL = "http://localhost:8000"

# Simulated LLM interactions
interactions = [
    {"input": "What is Deepchecks?", "output": "Deepchecks is an LLM Evaluation Tool"},
    {
        "input": "When was Deepchecks founded?",
        "output": "Deepchecks was founded in 2024",
    },
    {"input": "How are you doing?", "output": "I’m doing just fine, how about you?"},
    {
        "input": "What is the weather today?",
        "output": "Today should be warm with a late breeze",
    },
    {
        "input": "Tell me a joke.",
        "output": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    },
    {
        "input": "To be or not to be—that is the question.",
        "output": "Whether ’tis nobler in the mind to suffer The slings and arrows of outrageous fortune Or to take arms against a sea of troubles And by opposing end them.",
    },
    {"input": "A" * 150, "output": "Short response"},  # threshold alert for input
    {"input": "Short input", "output": "B" * 300},  # outlier alert for output
    {
        "input": "Explain quantum computing in simple terms.",
        "output": "Quantum computing is a type of computation that harnesses the collective properties of quantum states.",
    },
    {
        "input": "How does a neural network work?",
        "output": "A neural network works by simulating the behavior of a human brain's neurons.",
    },
    {
        "input": "What is the capital of France?",
        "output": "The capital of France is Paris.",
    },
    {"input": "C" * 200, "output": "D" * 10},  # threshold alert for input
    {"input": "E" * 10, "output": "F" * 250},  # outlier alert for output
    {
        "input": "What is the square root of 16?",
        "output": "The square root of 16 is 4.",
    },
    {
        "input": "How do you make a sandwich?",
        "output": "To make a sandwich, you need bread and fillings such as meat, cheese, or vegetables.",
    },
    {"input": "G" * 180, "output": "H" * 15},  # threshold alert for input
    {"input": "I" * 15, "output": "J" * 280},  # outlier alert for output
]


def log_interaction(interaction):
    url = f"{BASE_URL}/interactions"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(interaction), headers=headers)
    return response.json()


def get_metrics():
    url = f"{BASE_URL}/metrics"
    response = requests.get(url)
    return response.json()


def get_alerts():
    url = f"{BASE_URL}/alerts"
    response = requests.get(url)
    return response.json()


def simulate_interactions():
    for interaction in interactions:
        result = log_interaction(interaction)
        print(f"Logged Interaction: {result}")


def retrieve_metrics():
    metrics = get_metrics()
    print(f"Retrieved Metrics: {json.dumps(metrics, indent=2)}")


def retrieve_alerts():
    alerts = get_alerts()
    print(f"Retrieved Alerts: {json.dumps(alerts, indent=2)}")


if __name__ == "__main__":
    print("Simulating LLM interactions...")
    simulate_interactions()
    print("\nRetrieving metrics...")
    retrieve_metrics()
    print("\nRetrieving alerts...")
    retrieve_alerts()
