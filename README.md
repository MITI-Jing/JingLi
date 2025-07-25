ChefDao - AI Chinese Cooking Assistant
ChefDao is an intelligent AI cooking assistant specialized in authentic Chinese cuisine. It uses a ReAct (Reasoning and Acting) agent architecture to provide comprehensive cooking guidance, from recipe discovery to cultural context.

Features

🍽️ Authentic Recipe Discovery: Find traditional Chinese recipes tailored to your skill level
🛒 Smart Ingredient Analysis: Get shopping lists, substitutions, and sourcing advice
👨‍🍳 Detailed Cooking Instructions: Step-by-step guidance with timing and techniques
🥗 Nutritional Information: Health analysis with Traditional Chinese Medicine insights
🏮 Cultural Context: Learn the history and traditions behind each dish

Architecture
It uses a multi-agent ReAct architecture:

ReAct Planner: Analyzes user input and plans which specialized agents to call
Executor: Coordinates agent calls and manages context sharing
Memory System: Stores user preferences and cooking history
Specialized Agents: Recipe, Ingredient, Instruction, Nutrition, and Culture experts

Prerequisites

Python 3.8 or higher
Google Gemini API key
Virtual environment (recommended)

Installation

Clone the repository
bash
git clone <https://github.com/MITI-Jing/JingLi.git>


Create and activate virtual environment
bashpython -m venv env

# On Windows
env\Scripts\activate

# On macOS/Linux
source env/bin/activate

Install dependencies
bash
pip install google-generativeai python-dotenv

Set up environment variables
Create a .env file in the root directory:
GEMINI_API_KEY=your_gemini_api_key_here

To get a Gemini API key:

Go to Google AI Studio
Create a new API key
Copy the key to your .env file



Project Structure
JingLi/
├── src/
│   ├── main.py              # CLI entrypoint
│   ├── react_planner.py     # ReAct planning logic
│   ├── executor.py          # Agent coordination and execution
│   ├── memory.py           # User memory management
│   └── agents/             # Specialized agent classes (optional)
├── .env                    # Environment variables
├── user_memory.json       # User preferences storage
├── README.md              # This file
├── ARCHITECTURE.md        # System design documentation
├── EXPLANATION.md         # Detailed explanation of agent behavior
└── DEMO.md               # Demo video and examples


Start the application
bash
python -m src.main

Interact with ChefDao
Welcome to ChefDao — Your AI Chinese Cooking Assistant!
What would you like to cook or learn today? kung pao chicken

Example queries

"I want to make dumplings"
"How do I cook mapo tofu for beginners?"
"Tell me about the history of Peking duck"
"What ingredients do I need for hot pot?"
"Nutritional information for sweet and sour pork"



Memory System
ChefDao remembers your preferences:

Skill Level: Beginner, Intermediate, Advanced
Dietary Restrictions: Vegetarian, Vegan, Allergies, etc.
Available Ingredients: What you have in your kitchen
Cooking History: Previous dishes and preferences

Memory is stored in user_memory.json and persists between sessions.
Configuration
Skill Levels

Beginner: Simple recipes with detailed instructions
Intermediate: More complex dishes with moderate techniques
Advanced: Authentic recipes with professional techniques

Dietary Options

Vegetarian/Vegan adaptations
Gluten-free modifications
Low-sodium alternatives
Traditional dietary therapy (TCM)
