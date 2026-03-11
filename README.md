# RPG Game

A simple text-based RPG adventure game where you battle monsters, gain experience, and progress through different stages.

## Features

- **Monster Encounters**: Fight various monsters including Goblins, Skeletons, Orcs, and Slimes
- **Experience & Leveling System**: Gain EXP from battles and level up every 100 points
- **Stage Progression**: Advance through stages with level requirements
- **Boss Fights**: Face powerful bosses for massive experience rewards
- **Save & Load**: Save your game progress and resume later
- **Dynamic Health System**: Your health decreases during battles

## Game Mechanics

### Experience and Leveling
- Defeating monsters grants 5-20 EXP
- Every 100 EXP earned levels up your character
- Each level increases your strength and unlocks higher stages

### Stage System
- Starting at Stage 1
- Must reach `Level = Stage * 2` to advance to the next stage
- Higher stages mean stronger monsters and greater rewards

### Monsters
Each monster has unique stats:
| Monster | Health | EXP | Damage |
|---------|--------|-----|--------|
| Goblin  |   30   | 10  |   5    |
| Skeleton|   40   | 15  |   10   |
| Orc     |   60   | 20  |   15   |
| Slime   |   20   |  5  |   3    |
| Dragon (Boss) | 200 | 100 | 30 |
-----------------------------------
## How to Play

1. **Start the game:**
   ```bash
   python game.py
   ```

2. **Choose your action:**
   - `1` - Fight a Monster: Encounter a random monster and gain experience
   - `2` - Go to Next Stage: Progress your adventure (requires minimum level)
   - `3` - Check Status: View your current Level, EXP, and Stage
   - `4` - Boss Fight: Challenge a powerful dragon (available every 3 stages)
   - `5` - Inventory: View your items (under development gonna be soon)
   - `6` - Save: Save your progress to a file
   - `7` - Exit: Quit the game
   - `8` - Load Game: Resume from a previous save

## Requirements

- Python 3.x
- no any other requirments

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the game with `python game.py`

## Current Status

### Implemented
- ✅ Monster combat system
- ✅ Experience and level progression
- ✅ Stage advancement
- ✅ Health system
- ✅ Save/Load functionality
- ✅ Boss encounters (placeholder)

### In Development
- 🔄 Inventory system
- 🔄 Boss fight mechanics

## Future Improvements

- [ ] Implement full boss fight mechanics
- [ ] Add inventory system with items and equipment
- [ ] Implement special abilities and spells
- [ ] Add difficulty levels
- [ ] Implement NPC interactions
- [ ] Add rewards and loot system
- [ ] Create a proper GUI version

## License

This project is open source and available for modification and distribution.