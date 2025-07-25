# 🧠🍜 ChefDao — My AI Chinese Cooking Assistant

**ChefDao** is an intelligent AI cooking assistant that specializes in authentic Chinese cuisine. Powered by a ReAct (Reasoning + Acting) multi-agent architecture, it provides personalized cooking help — from recipe discovery to cultural insights.

---

## ✨ Features

- 🍽️ **Authentic Recipe Discovery** – Get traditional Chinese recipes tailored to your skill level  
- 🛒 **Smart Ingredient Analysis** – Receive shopping lists, substitutions, and sourcing advice  
- 👨‍🍳 **Step-by-Step Instructions** – Easy-to-follow guidance with timing and techniques  
- 🥗 **Nutritional Insights** – Health analysis with Traditional Chinese Medicine (TCM) principles  
- 🏮 **Cultural Context** – Learn the rich stories behind every dish  

---

## 🧠 Architecture Overview

ChefDao uses a modular **ReAct-style multi-agent** framework:

- 🤔 **ReAct Planner** – Analyzes user input and plans which agents to call  
- ⚙️ **Executor** – Coordinates agent execution and manages context  
- 🧾 **Memory System** – Stores user preferences and cooking history  
- 👥 **Specialized Agents**:  
  - `recipe_agent`  
  - `ingredient_agent`  
  - `instruction_agent`  
  - `nutrition_agent`  
  - `culture_agent`  

---

## ⚙️ Prerequisites

- Python 3.8 or higher  
- Google Gemini API key  
- Virtual environment (recommended)

---

## 🛠️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/MITI-Jing/JingLi.git
   cd JingLi
Create and activate a virtual environment

Windows:

bash
Copy code
python -m venv env
.\env\Scripts\activate
macOS/Linux:

bash
Copy code
python3 -m venv env
source env/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Set up environment variables

Create a .env file in the root directory:

ini
Copy code
GEMINI_API_KEY=your_gemini_api_key_here
🔑 You can get a Gemini API key from Google AI Studio.

🗂️ Project Structure
bash
Copy code
JingLi/
├── src/
│   ├── main.py              # CLI entrypoint
│   ├── react_planner.py     # ReAct planning logic
│   ├── executor.py          # Agent coordination and task execution
│   ├── memory.py            # User preference storage and retrieval
│   └── agents/              # Specialized agents (optional)
├── .env                     # API keys (excluded from GitHub)
├── user_memory.json         # User preferences memory
├── README.md                # This file
├── ARCHITECTURE.md          # System design overview
├── EXPLANATION.md           # Agent logic explanation
└── DEMO.md                  # Demo script and examples
🚀 Run the App
bash
Copy code
python -m src.main
Sample prompt:

vbnet
Copy code
Welcome to ChefDao — Your AI Chinese Cooking Assistant!
What would you like to cook or learn today?
> kung pao chicken
💬 Example Queries
"I want to make dumplings"

"How do I cook mapo tofu for beginners?"

"Tell me about the history of Peking duck"

"What ingredients do I need for hot pot?"

"Nutritional info for sweet and sour pork"

🧠 Memory System
ChefDao remembers user preferences between sessions:

Skill Level: Beginner | Intermediate | Advanced

Dietary Restrictions: Vegetarian | Vegan | Allergies

Available Ingredients: Real-time kitchen inventory

Cooking History: Past dishes and interactions

All stored in user_memory.json.

🧪 Configuration Options
🎯 Skill Levels
Beginner: Simple recipes with high guidance

Intermediate: Moderate complexity and cooking techniques

Advanced: Authentic techniques with minimal assistance

🌱 Dietary Customizations
Vegetarian/Vegan adaptations

Gluten-free or low-sodium alternatives

TCM-based dietary therapy recommendations

🙌 Acknowledgements
Inspired by the ReAct agent framework and human-first AI interaction design. Built to make authentic Chinese cooking more accessible and delightful.