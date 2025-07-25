"""
Instruction Agent - Specializes in detailed cooking instructions and techniques
"""

class InstructionAgent:
    def __init__(self):
        self.name = "instruction_agent"
        self.specialty = "Detailed Chinese Cooking Instructions & Techniques"
    
    def generate_detailed_instructions(self, dish: str, skill_level: str = "beginner", available_equipment: list = None) -> str:
        """
        Generate step-by-step cooking instructions for a Chinese dish.
        """
        equipment_text = ""
        if available_equipment:
            equipment_text = f"\nAvailable equipment: {', '.join(available_equipment)}"
        
        prompt = f"""
As an experienced Chinese cooking instructor, provide detailed step-by-step instructions for making {dish}:

Skill level: {skill_level}{equipment_text}

Please include:
1. Preparation timeline and mise en place
2. Step-by-step cooking instructions with timing
3. Visual and sensory cues for each step
4. Temperature and heat level guidance
5. Common mistakes to avoid
6. Troubleshooting tips
7. How to know when each step is complete
8. Final plating and serving suggestions

Tailor the detail level and explanations to a {skill_level} cook.
"""
        return prompt
    
    def explain_technique(self, technique: str, dish_context: str = None) -> str:
        """
        Explain specific Chinese cooking techniques in detail.
        """
        context_text = f" in the context of making {dish_context}" if dish_context else ""
        
        prompt = f"""
As a Chinese culinary technique expert, explain the {technique} technique{context_text}:

Please cover:
1. Purpose and benefits of this technique
2. Equipment needed and setup
3. Step-by-step execution
4. Temperature and timing considerations
5. Visual and tactile indicators of success
6. Common beginner mistakes
7. Advanced tips for mastery
8. When and why to use this technique

Make the explanation clear and actionable for home cooks.
"""
        return prompt
    
    def troubleshoot_cooking_issues(self, dish: str, problem: str, current_stage: str = None) -> str:
        """
        Provide troubleshooting advice for cooking problems.
        """
        stage_text = f" at the {current_stage} stage" if current_stage else ""
        
        prompt = f"""
As a Chinese cooking troubleshooting expert, help solve this problem with {dish}{stage_text}:

Problem: {problem}

Please provide:
1. Likely causes of this issue
2. Immediate steps to salvage the dish
3. How to prevent this problem in the future
4. Alternative approaches if the dish can't be saved
5. Learning points for next time
6. When to start over vs. continue fixing

Focus on practical solutions and learning opportunities.
"""
        return prompt
    
    def adapt_for_equipment(self, dish: str, original_equipment: str, available_equipment: str) -> str:
        """
        Adapt cooking instructions for different equipment.
        """
        prompt = f"""
As a Chinese cooking adaptation expert, modify the {dish} recipe from using {original_equipment} to using {available_equipment}:

Please provide:
1. Equipment-specific technique adjustments
2. Temperature and timing modifications
3. Alternative methods for key steps
4. What results to expect with different equipment
5. Workarounds for missing features
6. How the final dish might differ
7. Additional tools or accessories that might help

Ensure the recipe remains authentic and achievable with the available equipment.
"""
        return prompt
    
    def timing_and_coordination(self, dishes: list, total_cooking_time: str = None) -> str:
        """
        Provide timing and coordination advice for multiple dishes.
        """
        dishes_list = '\n'.join([f"- {dish}" for dish in dishes])
        time_text = f"\nTarget total cooking time: {total_cooking_time}" if total_cooking_time else ""
        
        prompt = f"""
As a Chinese kitchen coordination expert, create a cooking timeline for these dishes:

{dishes_list}{time_text}

Please provide:
1. Optimal cooking order and timing
2. Which dishes can be prepared in advance
3. Multi-tasking opportunities and warnings
4. Equipment scheduling (wok, steamer, etc.)
5. Temperature management for serving hot
6. Last-minute tasks and coordination
7. Backup plans if timing goes wrong

Focus on practical kitchen management for home cooks.
"""
        return prompt
    
    def ingredient_prep_guide(self, dish: str, ingredients: list = None) -> str:
        """
        Provide detailed ingredient preparation instructions.
        """
        ingredients_text = ""
        if ingredients:
            ingredients_text = f"\nIngredients to prep: {', '.join(ingredients)}"
        
        prompt = f"""
As a Chinese mise en place expert, provide detailed ingredient preparation for {dish}:

{ingredients_text}

Please include:
1. Specific cutting techniques and sizes
2. Marinating and seasoning instructions
3. Preparation timing and order
4. Storage methods between prep and cooking
5. Visual guides for proper preparation
6. How prep affects final dish quality
7. Make-ahead possibilities
8. Organization tips for efficient prep

Focus on precision and efficiency in ingredient preparation.
"""
        return prompt
    
    def advanced_technique_mastery(self, technique: str, mastery_level: str = "intermediate") -> str:
        """
        Provide advanced instruction for mastering Chinese cooking techniques.
        """
        prompt = f"""
As a Chinese culinary master, provide advanced training for the {technique} technique at {mastery_level} level:

Please include:
1. Advanced applications and variations
2. Professional tips and shortcuts
3. How to achieve restaurant-quality results
4. Regional or style variations
5. Integration with other techniques
6. Quality benchmarks and assessment
7. Practice exercises and progressions
8. Common plateau points and how to overcome them

Focus on developing true mastery and understanding of the technique.
"""
        return prompt
    
    def safety_and_best_practices(self, cooking_method: str, dish_type: str = None) -> str:
        """
        Provide safety guidelines and best practices for Chinese cooking methods.
        """
        context_text = f" when making {dish_type}" if dish_type else ""
        
        prompt = f"""
As a Chinese cooking safety expert, provide safety guidelines and best practices for {cooking_method}{context_text}:

Please cover:
1. Essential safety precautions
2. Proper equipment handling
3. Food safety considerations
4. Kitchen organization and cleanliness
5. Temperature control and monitoring
6. What to do in case of accidents
7. Long-term equipment care
8. Environmental considerations (ventilation, etc.)

Prioritize safety while maintaining cooking quality and efficiency.
"""
        return prompt