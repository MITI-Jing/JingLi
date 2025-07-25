"""
Culture Agent - Specializes in Chinese culinary history, traditions, and cultural context
"""

class CultureAgent:
    def __init__(self):
        self.name = "culture_agent"
        self.specialty = "Chinese Culinary Culture & History"
    
    def explain_dish_history(self, dish: str, region: str = None) -> str:
        """
        Provide historical and cultural context for a Chinese dish.
        """
        region_context = f" from {region}" if region else ""
        
        prompt = f"""
As a Chinese culinary historian, provide the cultural and historical background of {dish}{region_context}:

Please cover:
1. Historical origins and development
2. Cultural significance and symbolism
3. Regional variations and migration
4. Traditional occasions when served
5. Social and economic context
6. How preparation methods evolved
7. Modern adaptations and global influence

Include interesting stories, legends, or cultural anecdotes associated with this dish.
"""
        return prompt
    
    def explain_cooking_philosophy(self, concept: str) -> str:
        """
        Explain Chinese cooking philosophy and principles.
        """
        prompt = f"""
As a Chinese culinary philosopher, explain the concept of {concept} in Chinese cooking:

Please explore:
1. Traditional Chinese culinary theory
2. Balance principles (yin-yang, five elements)
3. Texture and flavor harmony
4. Seasonal cooking wisdom
5. Health and medicinal aspects
6. Social and family dining customs
7. How this applies to modern cooking

Connect ancient wisdom to practical cooking applications.
"""
        return prompt
    
    def festival_food_traditions(self, festival: str = None, season: str = None) -> str:
        """
        Explain Chinese festival foods and seasonal eating traditions.
        """
        context = ""
        if festival:
            context = f"for {festival}"
        elif season:
            context = f"during {season}"
        else:
            context = "in general"
        
        prompt = f"""
As a Chinese cultural expert, explain traditional foods and eating customs {context}:

Please include:
1. Symbolic meanings of traditional foods
2. Preparation rituals and customs
3. Family and community dining traditions
4. Regional variations in celebration foods
5. Stories and legends behind the traditions
6. How traditions have evolved over time
7. Modern ways to honor these traditions

Focus on the deeper cultural meanings behind the food choices and customs.
"""
        return prompt
    
    def dining_etiquette_guide(self, occasion: str = "family dinner") -> str:
        """
        Provide Chinese dining etiquette and customs guide.
        """
        prompt = f"""
As a Chinese etiquette expert, explain proper dining customs for {occasion}:

Please cover:
1. Table setting and seating arrangements
2. Serving and sharing protocols
3. Chopstick etiquette and taboos
4. Toast and drinking customs
5. Host and guest responsibilities
6. Conversation and behavior guidelines
7. Gift-giving traditions related to food

Include both traditional rules and modern adaptations for different settings.
"""
        return prompt
    
    def regional_cuisine_overview(self, region: str) -> str:
        """
        Provide overview of regional Chinese cuisine characteristics.
        """
        prompt = f"""
As a Chinese regional cuisine expert, provide a comprehensive overview of {region} cuisine:

Please include:
1. Geographic and climate influences
2. Signature ingredients and flavors
3. Characteristic cooking techniques
4. Famous dishes and specialties
5. Historical development and influences
6. Cultural significance within China
7. How it differs from other regions
8. Modern evolution and global spread

Focus on what makes this regional cuisine unique and culturally significant.
"""
        return prompt
    
    def tea_culture_pairing(self, dish: str = None, meal_type: str = "dinner") -> str:
        """
        Explain Chinese tea culture and food pairing principles.
        """
        context = f"with {dish}" if dish else f"for {meal_type}"
        
        prompt = f"""
As a Chinese tea master, explain tea culture and pairing principles {context}:

Please cover:
1. Traditional tea ceremony elements
2. Tea selection principles for food pairing
3. Seasonal tea preferences
4. Health and digestive benefits
5. Regional tea traditions
6. Proper brewing and serving techniques
7. Modern tea culture adaptations

Connect traditional tea wisdom to modern dining experiences.
"""
        return prompt
    
    def symbolism_and_meaning(self, food_item: str, context: str = "general") -> str:
        """
        Explain the symbolic meaning of foods in Chinese culture.
        """
        prompt = f"""
As a Chinese cultural symbolism expert, explain the meaning of {food_item} in {context} context:

Please explore:
1. Traditional symbolic meanings
2. Color, shape, and texture symbolism
3. Linguistic connections and wordplay
4. Use in ceremonies and celebrations
5. Regional variations in meaning
6. Historical evolution of symbolism
7. Modern interpretations and uses

Include folklore, proverbs, or traditional sayings related to this food item.
"""
        return prompt