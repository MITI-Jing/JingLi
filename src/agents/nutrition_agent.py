"""
Nutrition Agent - Specializes in nutritional analysis and health aspects of Chinese cuisine
"""

class NutritionAgent:
    def __init__(self):
        self.name = "nutrition_agent"
        self.specialty = "Chinese Food Nutrition & Health Analysis"
    
    def analyze_dish_nutrition(self, dish: str, ingredients: list = None, serving_size: str = "1 serving") -> str:
        """
        Provide nutritional analysis for a Chinese dish.
        """
        ingredients_text = ""
        if ingredients:
            ingredients_text = f"\nKey ingredients: {', '.join(ingredients)}"
        
        prompt = f"""
As a nutritionist specializing in Chinese cuisine, analyze the nutritional profile of {dish}:

Serving size: {serving_size}{ingredients_text}

Please provide:
1. Estimated calorie content and macronutrient breakdown
2. Key vitamins and minerals
3. Health benefits of main ingredients
4. Traditional Chinese medicine (TCM) properties
5. Dietary considerations (sodium, sugar, fat content)
6. Portion size recommendations
7. How to make it healthier while maintaining authenticity

Include both modern nutritional science and traditional Chinese health perspectives.
"""
        return prompt
    
    def healthy_modifications(self, dish: str, health_goals: list = None, dietary_restrictions: str = "none") -> str:
        """
        Suggest healthy modifications for Chinese dishes.
        """
        goals_text = ""
        if health_goals:
            goals_text = f"\nHealth goals: {', '.join(health_goals)}"
        
        prompt = f"""
As a Chinese cuisine nutritionist, suggest healthy modifications for {dish}:

Dietary restrictions: {dietary_restrictions}{goals_text}

Please provide:
1. Ingredient substitutions for better nutrition
2. Cooking method modifications
3. Portion control strategies
4. Ways to increase vegetable content
5. Reducing sodium/oil without losing flavor
6. Adding beneficial ingredients
7. Maintaining authentic taste while improving health profile

Focus on practical changes that preserve the dish's cultural identity.
"""
        return prompt
    
    def tcm_food_properties(self, ingredient_or_dish: str, health_concern: str = None) -> str:
        """
        Explain Traditional Chinese Medicine food properties.
        """
        concern_text = f" for {health_concern}" if health_concern else ""
        
        prompt = f"""
As a Traditional Chinese Medicine food therapy expert, explain the properties of {ingredient_or_dish}{concern_text}:

Please cover:
1. TCM classification (hot, cold, warm, cool, neutral)
2. Flavor properties (sweet, sour, bitter, spicy, salty)
3. Organ meridian connections
4. Therapeutic effects and health benefits
5. Seasonal eating recommendations
6. Who should avoid or favor this food
7. How to balance with other foods

Connect traditional wisdom with practical dietary advice.
"""
        return prompt
    
    def balanced_meal_planning(self, main_dish: str, dietary_needs: dict = None) -> str:
        """
        Create balanced Chinese meal suggestions around a main dish.
        """
        needs_text = ""
        if dietary_needs:
            needs_text = f"""
Dietary needs:
- Calories: {dietary_needs.get('calories', 'moderate')}
- Activity level: {dietary_needs.get('activity', 'moderate')}
- Health goals: {dietary_needs.get('goals', 'general health')}
- Age group: {dietary_needs.get('age_group', 'adult')}
"""
        
        prompt = f"""
As a Chinese nutrition expert, create a balanced meal plan around {main_dish}:

{needs_text}

Please suggest:
1. Complementary side dishes for nutritional balance
2. Appropriate soup or beverage pairings
3. Vegetable dishes to complete the meal
4. Portion size recommendations
5. Timing and eating order for optimal digestion
6. TCM balance principles applied
7. Make-ahead and leftover strategies

Focus on creating harmonious, nutritionally complete Chinese meals.
"""
        return prompt
    
    def ingredient_health_benefits(self, ingredient: str, preparation_method: str = "general") -> str:
        """
        Explain health benefits of specific Chinese cooking ingredients.
        """
        prompt = f"""
As a food science expert specializing in Chinese ingredients, explain the health benefits of {ingredient} when prepared using {preparation_method} methods:

Please cover:
1. Nutritional composition and bioactive compounds
2. Health benefits supported by research
3. How preparation method affects nutrients
4. Traditional medicinal uses
5. Optimal consumption amounts
6. Potential interactions or cautions
7. Best food combinations for enhanced benefits

Combine modern nutritional science with traditional Chinese medicine insights.
"""
        return prompt
    
    def dietary_adaptation_guide(self, original_dish: str, dietary_pattern: str) -> str:
        """
        Adapt Chinese dishes for specific dietary patterns.
        """
        prompt = f"""
As a specialized Chinese cuisine dietitian, adapt {original_dish} for a {dietary_pattern} dietary pattern:

Please provide:
1. Key ingredient modifications needed
2. Cooking technique adjustments
3. Nutritional impact of changes
4. Flavor compensation strategies
5. Additional seasonings or ingredients to add
6. Portion and frequency recommendations
7. How to maintain cultural authenticity

Ensure the adapted version remains satisfying and culturally respectful.
"""
        return prompt
    
    def seasonal_eating_guide(self, season: str, constitution_type: str = "balanced") -> str:
        """
        Provide seasonal eating recommendations based on TCM principles.
        """
        prompt = f"""
As a TCM nutrition expert, provide seasonal eating guidance for {season} for someone with a {constitution_type} constitution:

Please include:
1. Ideal food temperatures and cooking methods
2. Beneficial ingredients and flavors for the season
3. Foods to emphasize or avoid
4. Meal timing and eating habits
5. Hydration and beverage recommendations
6. Common seasonal health concerns and food remedies
7. Sample daily meal structure

Connect seasonal wisdom to practical modern Chinese cooking and eating habits.
"""
        return prompt