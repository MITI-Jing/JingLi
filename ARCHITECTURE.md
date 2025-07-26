# ChefDao System Architecture

## Overview

ChefDao implements a **ReAct (Reasoning and Acting) Agent Architecture** specialized for Chinese cooking assistance. The system combines planning, reasoning, and execution to provide comprehensive culinary guidance.

## High-Level Architecture

```ascii
┌─────────────────────────────────────────────────────────────────┐
│                        ChefDao System                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐    ┌──────────────┐    ┌─────────────────┐    │
│  │    User     │───▶│    Main      │───▶│     Memory      │    │
│  │   Input     │    │  Interface   │    │   Management    │    │
│  └─────────────┘    └──────────────┘    └─────────────────┘    │
│                              │                                  │
│                              ▼                                  │
│                    ┌──────────────┐                            │
│                    │    ReAct     │                            │
│                    │   Planner    │                            │
│                    └──────────────┘                            │
│                              │                                  │
│                              ▼                                  │
│                    ┌──────────────┐                            │
│                    │   Executor   │                            │
│                    │ Coordinator  │                            │
│                    └──────────────┘                            │
│                              │                                  │
│         ┌────────────────────┼────────────────────┐            │
│         ▼                    ▼                    ▼            │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│  │   Recipe    │    │ Ingredient  │    │ Instruction │        │
│  │   Agent     │    │   Agent     │    │   Agent     │        │
│  └─────────────┘    └─────────────┘    └─────────────┘        │
│         ▼                    ▼                    ▼            │
│  ┌─────────────┐    ┌─────────────┐                           │
│  │ Nutrition   │    │  Culture    │                           │
│  │   Agent     │    │   Agent     │                           │
│  └─────────────┘    └─────────────┘                           │
│                              │                                  │
│                              ▼                                  │
│                    ┌──────────────┐                            │
│                    │   Response   │                            │
│                    │ Aggregation  │                            │
│                    └──────────────┘                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Main Interface (`main.py`)
**Purpose**: Entry point and user interaction management

```ascii
┌─────────────────┐
│   User Input    │
│  "kung pao      │
│   chicken"      │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ Load User       │
│ Memory/Prefs    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ Call ReAct      │
│ Planner         │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ Execute Tasks   │
│ via Executor    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ Save Memory &   │
│ Return Response │
└─────────────────┘
```

### 2. ReAct Planner (`react_planner.py`)
**Purpose**: Intelligent task planning using reasoning chains

```ascii
User Input: "steamed seabass"
    │
    ▼
┌─────────────────────────────────────────┐
│ ReAct Reasoning Process                 │
├─────────────────────────────────────────┤
│                                         │
│ Thought: User wants steamed seabass     │
│          Need recipe first              │
│ Action: call recipe_agent with         │
│         {"dish": "steamed seabass"}     │
│                                         │
│ Thought: Need ingredient analysis       │
│ Action: call ingredient_agent with     │
│         recipe context                  │
│                                         │
│ Thought: Need cooking instructions      │
│ Action: call instruction_agent with    │
│         recipe + ingredients            │
│                                         │
└─────────────────────────────────────────┘
    │
    ▼
Task List: [recipe_agent, ingredient_agent, instruction_agent]
```

### 3. Executor (`executor.py`)
**Purpose**: Agent coordination and context management

```ascii
┌─────────────────┐    ┌─────────────────┐
│  Task Queue     │───▶│   Context       │
│                 │    │   Storage       │
│ [recipe_agent,  │    │                 │
│  ingredient_   │    │ {recipe: "...", │
│  instruction_   │    │  ingredients:   │
│  agent]         │    │  [...]}         │
└─────────────────┘    └─────────────────┘
         │                       ▲
         ▼                       │
┌─────────────────┐             │
│  Execute Task   │─────────────┘
│                 │
│ 1. Build Prompt │
│ 2. Call Gemini  │
│ 3. Store Result │
│ 4. Pass Context │
└─────────────────┘
```

### 4. Memory System (`memory.py`)
**Purpose**: Persistent user preference storage

```ascii
┌─────────────────────────────────┐
│        User Memory              │
├─────────────────────────────────┤
│                                 │
│ {                               │
│   "user_id": {                  │
│     "skill_level": "beginner",  │
│     "dietary_restrictions":     │
│       ["vegetarian"],           │
│     "available_ingredients":    │
│       ["soy_sauce", "rice"],    │
│     "cooking_history": [        │
│       "mapo_tofu",              │
│       "fried_rice"              │
│     ],                          │
│     "preferences": {            │
│       "spice_level": "mild",    │
│       "region": "Sichuan"       │
│     }                           │
│   }                             │
│ }                               │
│                                 │
└─────────────────────────────────┘
```

## Agent Specializations

### Recipe Agent 🍽️
- **Input**: Dish name, skill level, dietary restrictions
- **Output**: Authentic Chinese recipes with measurements
- **Specialization**: Traditional cooking methods, regional variations

### Ingredient Agent 🛒
- **Input**: Recipe context, available ingredients
- **Output**: Shopping lists, substitutions, sourcing advice
- **Specialization**: Chinese ingredient knowledge, authenticity preservation

### Instruction Agent 👨‍🍳
- **Input**: Recipe context, skill level, equipment
- **Output**: Step-by-step cooking instructions
- **Specialization**: Cooking techniques, timing, troubleshooting

### Nutrition Agent 🥗
- **Input**: Dish name, ingredients
- **Output**: Nutritional analysis, health benefits
- **Specialization**: Modern nutrition + Traditional Chinese Medicine

### Culture Agent 🏮
- **Input**: Dish name, regional context
- **Output**: Historical background, cultural significance
- **Specialization**: Culinary history, traditions, symbolism

## Tool Integrations

### Google Gemini API
```ascii
┌─────────────────┐
│   Agent Prompt  │
│                 │
│ "As a Chinese   │
│ cooking expert, │
│ provide recipe  │
│ for kung pao    │
│ chicken..."     │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Gemini Model   │
│ gemini-1.5-     │
│ flash           │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ Structured      │
│ Response        │
│                 │
│ Recipe with     │
│ ingredients &   │
│ instructions    │
└─────────────────┘
```

### Configuration Management
- Environment variables via `.env`
- API key security
- Model selection flexibility

## Data Flow

### Request Processing Flow
```ascii
User Input → Memory Load → ReAct Planning → Task Generation → 
Agent Execution → Context Sharing → Response Aggregation → 
Memory Update → User Output
```

### Context Sharing Between Agents
```ascii
Recipe Agent Output
         │
         ▼
┌─────────────────┐
│   Context       │
│   Store         │
│                 │
│ {recipe_agent:  │
│  "recipe text"} │
└─────────────────┘
         │
         ▼
Ingredient Agent Input (with recipe context)
         │
         ▼
┌─────────────────┐
│   Updated       │
│   Context       │
│                 │
│ {recipe_agent:  │
│  "recipe text", │
│  ingredient_    │
│  agent: "..."}  │
└─────────────────┘
```

## Logging and Observability

### Console Logging
- ReAct reasoning chains visible to user
- Error messages with context
- Agent execution progress

### Debug Information
```python
print("REACT THOUGHTS:\n", thought_chain)  # Planning visibility
print(f"Error parsing line: {line} - {e}")  # Error tracking
```

### Memory Persistence
- JSON-based user preference storage
- Session continuity
- Preference learning over time

## Error Handling and Resilience

### API Failure Recovery
```ascii
┌─────────────────┐
│  Gemini API     │
│  Call Fails     │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Fallback       │
│  Response       │
│                 │
│ "Error calling  │
│ Gemini API: X"  │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  System         │
│  Continues      │
│  Operation      │
└─────────────────┘
```

### Task Parsing Failures
- Regex-based parsing with fallbacks
- Default task generation for unrecognized input
- Graceful degradation

## Performance Considerations

### Optimization Strategies
- Context size management (limit to 500 chars for long recipes)
- Sequential agent execution (no parallel processing)
- Memory-based personalization reduces repeated queries

### Scalability Notes
- Single-user design (can be extended for multi-user)
- Stateless agent execution
- JSON file storage (suitable for prototype, database recommended for production)

## Security Considerations

### API Key Management
- Environment variable storage
- No hardcoded credentials
- Local .env file (not committed to version control)

### Input Validation
- JSON parsing with error handling
- Safe parameter extraction
- No direct code execution from LLM output

## Future Architecture Enhancements

### Potential Improvements
1. **Parallel Agent Execution**: Speed up response times
2. **Database Integration**: Replace JSON file storage
3. **Caching Layer**: Store common recipe/ingredient data
4. **Multi-modal Input**: Image recognition for ingredients
5. **Real-time Feedback**: Interactive cooking assistance
6. **Recipe Rating System**: User feedback integration