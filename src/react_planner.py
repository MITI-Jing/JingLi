import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def react_plan(user_input: str, memory: dict) -> list:
    prompt = build_react_prompt(user_input, memory)

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')  # Use correct Gemini model name
        response = model.generate_content(prompt)
        thought_chain = response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        # Return a basic fallback plan
        return [
            {"agent": "recipe_agent", "action": "dynamic", "params": {"dish": user_input, "skill": "beginner"}},
            {"agent": "instruction_agent", "action": "dynamic", "params": {"dish": user_input, "skill": "beginner"}}
        ]

    print("REACT THOUGHTS:\n", thought_chain)
    return extract_tasks_from_chain(thought_chain)

def build_react_prompt(user_input, memory):
    skill = memory.get("skill_level", "beginner")
    diet = memory.get("dietary_restrictions", "none")
    available = memory.get("available_ingredients", [])

    return f"""
You are a culinary AI planning assistant for ChefDao, helping users cook authentic Chinese dishes. 

User request: "{user_input}"
User profile: {skill} cook, {diet} diet, available ingredients: {', '.join(available) or 'none'}

Plan the most helpful sequence of agent calls. Think step by step:

Thought: [Your reasoning about what the user needs]
Action: call <agent_name> with {{"dish": "specific_dish", "skill": "{skill}"}}

Available agents:
- recipe_agent: Find authentic Chinese recipes
- ingredient_agent: Analyze ingredients, substitutions, shopping lists  
- instruction_agent: Detailed cooking steps and techniques
- nutrition_agent: Health and nutritional information
- culture_agent: Cultural background and history

RULES:
1. Always start with recipe_agent if user wants to cook something
2. Include instruction_agent for cooking guidance
3. Use proper JSON format with double quotes
4. Limit to 3-4 most useful agents
5. Be specific about the dish name

Example:
Thought: User wants to cook a Chinese dish but was vague. I should suggest a popular, beginner-friendly option.
Action: call recipe_agent with {{"dish": "steamed seabass", "skill": "beginner"}}
    """.strip()

def extract_tasks_from_chain(chain_text: str) -> list:
    """
    Parses the LLM response into task dictionaries.
    """
    import re
    import json
    
    tasks = []
    lines = chain_text.split("\n")
    
    for line in lines:
        if line.strip().startswith("Action:"):
            try:
                # Extract agent name and parameters using regex
                match = re.search(r'call\s+(\w+)\s+with\s+(\{.*\})', line.strip())
                if match:
                    agent_name = match.group(1)
                    params_str = match.group(2)
                    
                    # Try to parse as JSON
                    try:
                        params = json.loads(params_str)
                    except json.JSONDecodeError:
                        # Fallback: create basic params
                        params = {"dish": "fish", "skill": "beginner"}
                    
                    tasks.append({
                        "agent": agent_name.strip(),
                        "action": "dynamic", 
                        "params": params
                    })
                    
            except Exception as e:
                print(f"Error parsing line: {line} - {e}")
                # Add a fallback task
                if "recipe_agent" in line:
                    tasks.append({
                        "agent": "recipe_agent",
                        "action": "dynamic",
                        "params": {"dish": "fish", "skill": "beginner"}
                    })
    
    # If no tasks were extracted, provide fallback
    if not tasks:
        tasks = [
            {"agent": "recipe_agent", "action": "dynamic", "params": {"dish": "fish", "skill": "beginner"}},
            {"agent": "instruction_agent", "action": "dynamic", "params": {"dish": "fish", "skill": "beginner"}}
        ]
    
    return tasks