from src.memory import load_memory, save_memory
from src.executor import execute_tasks
from src.react_planner import react_plan as plan_tasks


def main():
    print("Welcome to ChefDao — Your AI Chinese Cooking Assistant!")
    user_input = input("What would you like to cook or learn today? ")

    user_id = "default_user"  # Replace with dynamic user ID if available

    # 1. Load memory
    user_memory = load_memory(user_id)

    # 2. Plan sub-tasks
    tasks = plan_tasks(user_input, user_memory)

    # 3. Execute sub-tasks
    response = execute_tasks(tasks)

    # 4. Save memory (optional, can update based on interaction)
    save_memory(user_id, user_memory)

    # 5. Output final combined response
    print("\nHere is your personalized cooking plan:\n")
    print(response)

if __name__ == "__main__":
    main()
