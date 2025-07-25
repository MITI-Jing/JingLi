"""
Recipe Agent - Specializes in finding authentic Chinese recipes
"""

class RecipeAgent:
    def __init__(self):
        self.name = "recipe_agent"
        self.specialty = "Authentic Chinese Recipe Discovery"
    
    def find_recipe(self, dish: str, skill_level: str = "beginner", dietary_restrictions: str = "none") -> str:
        """
        Find an authentic Chinese recipe based on dish name and user preferences.
        """
        base_prompt = f"""
As an expert Chinese chef and cookbook author, provide an authentic recipe for {dish}.

Requirements:
- Skill level: {skill_level}
- Dietary restrictions: {dietary_restrictions}
- Focus on traditional preparation methods
- Include ingredient quantities and cooking times
- Mention regional variations if applicable

Please provide:
1. Brief dish description and origin
2. Complete ingredient list with measurements
3. Equipment needed
4. Preparation overview
5. Any special tips for authenticity

Keep the recipe appropriate for a {skill_level} cook while maintaining authenticity.
"""
        return base_prompt
    
    def get_recipe_variations(self, dish: str, region: str = None) -> str:
        """
        Get regional variations of a Chinese dish.
        """
        region_context = f" from {region}" if region else ""
        
        prompt = f"""
As a Chinese culinary historian, explain the different regional variations of {dish}{region_context}.

Please cover:
1. Original/traditional version
2. Popular regional adaptations (Sichuan, Cantonese, Hunan, etc.)
3. Key differences in ingredients and techniques
4. Which version is best for home cooking
5. Cultural significance of each variation

Focus on authentic preparations, not westernized versions.
"""
        return prompt
    
    def adapt_for_skill(self, recipe: str, current_skill: str, target_skill: str) -> str:
        """
        Adapt a recipe for different skill levels.
        """
        prompt = f"""
Take this Chinese recipe and adapt it from {current_skill} level to {target_skill} level:

{recipe}

Please modify:
1. Complexity of techniques
2. Ingredient accessibility
3. Equipment requirements
4. Step-by-step detail level
5. Time management tips

Maintain authenticity while adjusting difficulty.
"""
        return prompt
    
    def suggest_similar_dishes(self, dish: str, preferences: dict = None) -> str:
        """
        Suggest similar Chinese dishes based on user preferences.
        """
        pref_text = ""
        if preferences:
            pref_text = f"""
User preferences:
- Spice level: {preferences.get('spice_level', 'medium')}
- Protein preference: {preferences.get('protein', 'any')}
- Cooking method: {preferences.get('cooking_method', 'any')}
- Region interest: {preferences.get('region', 'any')}
"""
        
        prompt = f"""
Based on interest in {dish}, suggest 5 similar authentic Chinese dishes.

{pref_text}

For each suggestion provide:
1. Dish name (Chinese and English)
2. Brief description
3. Why it's similar to {dish}
4. Difficulty level
5. Key flavor profile

Focus on dishes that share cooking techniques, flavor profiles, or ingredients with {dish}.
"""
        return prompt