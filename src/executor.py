import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def call_gemini(prompt: str) -> str:
    """
    Call Gemini API with the given prompt.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"

def build_prompt(agent_name: str, action: str, params: dict, context: dict = None) -> str:
    """
    Build prompts for different agents with context from previous agents.
    """
    dish = params.get("dish", "unknown dish")
    skill = params.get("skill", "beginner")
    diet = params.get("diet", "none")
    
    if action == "dynamic":
        if agent_name == "recipe_agent":
            return f"""As an expert Chinese chef, provide an authentic recipe for {dish} suitable for a {skill} cook with {diet} dietary restrictions.

Include:
1. Brief dish description and origin
2. Complete ingredient list with measurements
3. Equipment needed
4. Step-by-step preparation instructions
5. Cooking tips for authenticity

Keep it appropriate for a {skill} cook while maintaining authenticity."""

        elif agent_name == "ingredient_agent":
            recipe_text = context.get("recipe_agent", "") if context else ""
            if recipe_text:
                return f"""Based on this Chinese recipe: {recipe_text[:500]}...

Please provide:
1. Essential vs optional ingredients
2. Where to source authentic Chinese ingredients
3. Substitutions for hard-to-find items (maintaining authenticity)
4. Storage tips for specialty ingredients
5. Shopping list organized by priority
6. Cost-effective alternatives

Focus on maintaining authentic flavors while being practical for home cooks."""
            else:
                return f"Analyze ingredients needed for {dish} and provide shopping guidance for a {skill} cook."

        elif agent_name == "instruction_agent":
            recipe_text = context.get("recipe_agent", "") if context else ""
            if recipe_text:
                return f"""Based on this Chinese recipe: {recipe_text[:300]}...

Provide detailed step-by-step cooking instructions for {dish} suitable for a {skill} cook:

1. Preparation timeline and mise en place
2. Step-by-step cooking with timing
3. Visual and sensory cues for each step
4. Temperature and heat level guidance
5. Common mistakes to avoid
6. Troubleshooting tips
7. Final plating and serving

Make instructions clear and detailed for the skill level."""
            else:
                return f"Provide detailed cooking instructions for {dish} suitable for a {skill} cook."

        elif agent_name == "nutrition_agent":
            return f"""As a nutritionist specializing in Chinese cuisine, analyze {dish}:

Provide:
1. Estimated calorie content and macronutrient breakdown
2. Key vitamins and minerals
3. Health benefits of main ingredients
4. Traditional Chinese medicine (TCM) properties
5. Dietary considerations (sodium, sugar, fat)
6. Portion size recommendations
7. How to make it healthier while maintaining authenticity

Include both modern nutrition and traditional Chinese health perspectives."""

        elif agent_name == "culture_agent":
            return f"""As a Chinese culinary historian, provide cultural background for {dish}:

Cover:
1. Historical origins and development
2. Cultural significance and symbolism
3. Regional variations
4. Traditional occasions when served
5. Social and economic context
6. How preparation evolved over time
7. Modern adaptations

Include interesting stories or cultural anecdotes."""

    return "No prompt defined for this agent and action."

def execute_tasks(tasks: list) -> str:
    """
    Execute tasks with context sharing between agents.
    """
    results = []
    context = {}
    
    for task in tasks:
        agent_name = task["agent"]
        action = task.get("action", "dynamic")
        params = task.get("params", {})

        prompt = build_prompt(agent_name, action, params, context)
        response = call_gemini(prompt)
        
        # Store result for future agents
        context[agent_name] = response
        
        # Format response
        agent_titles = {
            "recipe_agent": "🍽️ Authentic Chinese Recipe",
            "ingredient_agent": "🛒 Ingredient Analysis & Shopping Guide", 
            "instruction_agent": "👨‍🍳 Detailed Cooking Instructions",
            "nutrition_agent": "🥗 Nutritional Information",
            "culture_agent": "🏮 Cultural Background"
        }
        
        title = agent_titles.get(agent_name, agent_name)
        results.append(f"=== {title} ===\n{response}\n")

    return "\n".join(results)