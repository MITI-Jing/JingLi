"""
Ingredient Agent - Specializes in ingredient analysis, substitutions, and sourcing
"""

class IngredientAgent:
    def __init__(self):
        self.name = "ingredient_agent"
        self.specialty = "Chinese Ingredient Management & Substitutions"
    
    def analyze_ingredients(self, ingredients: list, available_ingredients: list = None) -> str:
        """
        Analyze recipe ingredients and suggest substitutions based on availability.
        """
        available_text = ""
        if available_ingredients:
            available_text = f"\nAvailable ingredients: {', '.join(available_ingredients)}"
        
        ingredients_list = '\n'.join([f"- {ing}" for ing in ingredients])
        
        prompt = f"""
As a Chinese cooking expert, analyze these recipe ingredients:

{ingredients_list}{available_text}

Please provide:
1. Essential vs optional ingredients
2. Where to source authentic Chinese ingredients
3. Substitutions for hard-to-find items (maintaining authenticity)
4. Storage tips for specialty ingredients
5. Cost-effective alternatives
6. Which ingredients can be prepared in advance

Focus on maintaining authentic flavors while being practical for home cooks.
"""
        return prompt
    
    def suggest_substitutions(self, ingredient: str, dietary_restrictions: str = "none", available_ingredients: list = None) -> str:
        """
        Suggest substitutions for specific ingredients.
        """
        available_text = ""
        if available_ingredients:
            available_text = f"\nMust use from these available ingredients: {', '.join(available_ingredients)}"
        
        prompt = f"""
As a Chinese culinary expert, suggest authentic substitutions for: {ingredient}

Dietary restrictions: {dietary_restrictions}
{available_text}

Please provide:
1. Best authentic substitute (closest flavor/texture)
2. Easily available alternatives
3. How the substitution changes the dish
4. Quantity adjustments needed
5. Any technique modifications required

Prioritize maintaining the dish's authentic character and flavor profile.
"""
        return prompt
    
    def optimize_ingredient_list(self, recipe_ingredients: list, pantry_staples: list = None, budget_conscious: bool = False) -> str:
        """
        Optimize ingredient list for cost and availability.
        """
        staples_text = ""
        if pantry_staples:
            staples_text = f"\nPantry staples available: {', '.join(pantry_staples)}"
        
        budget_text = "\nPrioritize cost-effective options." if budget_conscious else ""
        
        ingredients_list = '\n'.join([f"- {ing}" for ing in recipe_ingredients])
        
        prompt = f"""
Optimize this Chinese recipe ingredient list for home cooking:

{ingredients_list}{staples_text}{budget_text}

Please provide:
1. Ingredients you likely already have
2. Must-buy specialty items
3. Money-saving bulk purchase suggestions
4. Multi-recipe ingredient uses
5. Brand recommendations for key items
6. Shopping list organized by store section

Focus on building a practical Chinese pantry while maintaining authenticity.
"""
        return prompt
    
    def explain_ingredient_purpose(self, ingredient: str, dish_context: str = None) -> str:
        """
        Explain the role and importance of specific ingredients in Chinese cooking.
        """
        context_text = f" in the context of {dish_context}" if dish_context else ""
        
        prompt = f"""
As a Chinese culinary expert, explain the role of {ingredient}{context_text}:

Please cover:
1. Flavor profile contribution
2. Texture/mouthfeel impact
3. Cultural/traditional significance
4. Cooking technique implications
5. How it interacts with other ingredients
6. What happens if omitted
7. Quality indicators when purchasing

Provide both culinary and cultural context for this ingredient's importance.
"""
        return prompt
    
    def seasonal_ingredient_guide(self, season: str, region: str = "general") -> str:
        """
        Provide seasonal ingredient recommendations for Chinese cooking.
        """
        prompt = f"""
As a Chinese market expert, provide a seasonal ingredient guide for {season} cooking:

Region focus: {region}

Please include:
1. Peak seasonal vegetables and their uses
2. Seasonal protein recommendations
3. Traditional seasonal flavor combinations
4. Preservation techniques for seasonal abundance
5. Classic dishes that highlight seasonal ingredients
6. Shopping tips for best quality and price

Focus on how seasonality affects authentic Chinese cooking and flavor development.
"""
        return prompt