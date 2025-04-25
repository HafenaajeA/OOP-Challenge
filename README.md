# 🐶 Python OOP Challenge: Build Your Own Digital Pet

Welcome to this week's Python challenge! 🎉

This challenge focuses on creating a virtual pet using Object-Oriented Programming (OOP) concepts in Python. You'll learn to implement classes, attributes, methods, and constructors while building a fun interactive pet simulation.

## 🎯 Core Features

Your `Pet` class should include:

### Attributes
| Attribute | Description | Range |
|-----------|-------------|--------|
| `name` | Your pet's name | string |
| `hunger` | Pet's hunger level | 0 (full) - 10 (starving) |
| `energy` | Pet's energy level | 0 (exhausted) - 10 (energetic) |
| `happiness` | Pet's mood level | 0 (sad) - 10 (very happy) |

### Methods
- `eat()`: Feed your pet (-3 hunger, +1 happiness)
- `sleep()`: Let your pet rest (+5 energy)
- `play()`: Play with your pet (-2 energy, +2 happiness, +1 hunger)
- `get_status()`: Display pet's current stats

### 🌟 Bonus Features
- `train(trick)`: Teach your pet new tricks
- `show_tricks()`: Display all learned tricks

## 🚀 Getting Started

1. Clone this repository
2. Navigate to the project directory
3. Run `python main.py` to test your implementation

## 📝 Example Usage

```python
my_pet = Pet("Max")
my_pet.eat()
my_pet.play()
my_pet.train("roll over")
my_pet.get_status()
```

## 💡 Implementation Tips

- Use `max()` and `min()` to keep attribute values between 0 and 10
- Add input validation for methods
- Consider adding custom behaviors or pet types
- Use emojis to make output more engaging

## 🏆 Bonus Challenge Ideas

- Add different pet types (dog, cat, rabbit, etc.)
- Implement a time system (day/night cycle)
- Add a health system
- Create an interactive menu system

## 📫 Submission

Submit your solution by:
1. Forking this repository
2. Implementing your solution
3. Creating a pull request or sharing your repository link

Happy Coding! 🎈
