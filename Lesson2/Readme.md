# Lesson 2: Types and Objects - Meet Python's Data Pokémon! 🎮

## 🌟 Welcome to the Data Type Universe!

Imagine if data types were Pokémon - each one has its own special abilities and personality! In Python's world, every value has its own "type," just like every Pokémon has fire, water, or grass attributes.

Python is a **dynamically typed language**, which means you don't need to tell the computer "this is what type" beforehand - it's like a smartphone that automatically recognizes what you're typing!

## 🎯 The Four Basic Types in Python

### 1. Int (Integer) - Math-type Pokémon 🔢

Integers are like perfect counters - no decimal points, clean and simple!

```python
# Integer examples
my_age = 16
game_score = 9999
temperature = -5
followers = 1000

print(f"I'm {my_age} years old")
print(f"My game score is {game_score}")
print(f"Today's temperature is {temperature}°C")
print(f"I have {followers} followers!")
```

**Integer Superpowers:**
- ➕ Can do all math operations
- 🎯 Precise, no decimal errors
- 💾 Uses relatively less memory

### 2. Float (Floating Point) - Precision-type Pokémon 🎯

Floats are like precision measurement tools that can represent decimals!

```python
# Float examples
height = 165.5
pi = 3.14159
money = 99.99
speed = 2.5e2  # Scientific notation: 250.0

print(f"My height is {height} cm")
print(f"Pi is approximately {pi}")
print(f"This item costs ${money}")
print(f"Light speed is {speed} million km/s")
```

**Float Superpowers:**
- 🎯 Can represent extremely large or small numbers
- 🔬 Perfect for scientific calculations
- 💰 Handles money-related calculations

### 3. Str (String) - Text-type Pokémon 📝

Strings are like talking Pokémon that can contain any text content!

```python
# String examples
username = "SuperGamer123"
message = 'What a beautiful day!'
emoji_text = "🎮💻🚀⭐"
song_lyrics = """
    I'm a little code newbie
    Learning new skills every day
    Python is my best friend
"""

print(f"Username: {username}")
print(f"Today's message: {message}")
print(f"Emojis: {emoji_text}")
print(f"Lyrics: {song_lyrics}")
```

**String Superpowers:**
- 🎨 Can contain any characters (letters, numbers, symbols, emojis)
- 🔤 Can use single quotes, double quotes, or triple quotes
- 🎭 Can simulate conversations and stories

### 4. Bool (Boolean) - Logic-type Pokémon ⚡

Booleans are the simplest yet most important type, with only two values: True and False

```python
# Boolean examples
is_student = True
homework_done = False
game_over = True
weekend = False

print(f"Are you a student? {is_student}")
print(f"Is homework done? {homework_done}")
print(f"Is the game over? {game_over}")
print(f"Is it weekend? {weekend}")
```

**Boolean Superpowers:**
- 🔀 Controls program flow (if/else)
- 🎯 Makes decisions and judgments
- 🔍 Comparison and logical operations

## 🔍 Type Checker - Your Data Detective

Use the `type()` function to check the type of any value:

```python
# Type checking in action
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>

# Check variable types
my_score = 95
print(f"my_score type is: {type(my_score)}")

user_input = input("Enter anything: ")
print(f"Your input type is: {type(user_input)}")  # Hint: Always str!
```

## 🔄 Type Conversion - Data Transformation Magic

Sometimes we need data to "transform" into another type, like Pokémon evolution!

### Complete Conversion Functions:
```python
# Type conversion examples
original_number = 3.14
age_str = "18"
money_str = "99.99"

# Convert to integer
print(f"3.14 to int: {int(original_number)}")        # 3
print(f"'18' to int: {int(age_str)}")                # 18

# Convert to float
print(f"18 to float: {float(18)}")                   # 18.0
print(f"'99.99' to float: {float(money_str)}")       # 99.99

# Convert to string
print(f"123 to string: '{str(123)}'")                # '123'
print(f"3.14 to string: '{str(3.14)}'")              # '3.14'

# Convert to boolean (especially interesting!)
print(f"1 to bool: {bool(1)}")                       # True
print(f"0 to bool: {bool(0)}")                       # False
print(f"'Hello' to bool: {bool('Hello')}")           # True
print(f"'' to bool: {bool('')}")                     # False
```

### 💡 Secret Rules for Boolean Conversion:
```python
# These values become False when converted to boolean:
print(bool(0))          # False - number zero
print(bool(0.0))        # False - float zero
print(bool(""))         # False - empty string
print(bool(None))       # False - null value

# All other values become True:
print(bool(1))          # True
print(bool(-1))         # True
print(bool("0"))        # True (Note: this is a string!)
print(bool("False"))    # True (Note: this is also a string!)
```

## 🎮 Hands-on Practice: Personal Data Processor

Let's create an interesting personal data processing program:

```python
print("🎮 Welcome to the Personal Data Processor!")
print("=" * 40)

# Collect data
name = input("What's your nickname? ")
age_str = input("How old are you? ")
height_str = input("What's your height in cm? ")
is_gamer = input("Do you like gaming? (yes/no) ")

# Type conversion
age = int(age_str)
height = float(height_str)
likes_gaming = is_gamer.lower() == "yes"

# Data analysis
is_teenager = 13 <= age <= 19
is_tall = height > 170
next_year_age = age + 1

# Display results
print(f"\n🎉 {name}'s profile analysis complete!")
print(f"📊 Age: {age} years old (Type: {type(age).__name__})")
print(f"📏 Height: {height} cm (Type: {type(height).__name__})")
print(f"🎮 Likes gaming: {likes_gaming} (Type: {type(likes_gaming).__name__})")
print(f"🧒 Is teenager: {is_teenager}")
print(f"🏀 Is tall: {is_tall}")
print(f"🎂 Next year will be {next_year_age} years old!")
```

## 🧩 Challenge Missions: Data Type Master

### Mission 1: Type Detective
```python
# Predict the types of these variables, then verify with code:
mystery_1 = 42
mystery_2 = "42"
mystery_3 = 4.2
mystery_4 = True
mystery_5 = "True"

# Your predictions:
# mystery_1 is _____ type
# mystery_2 is _____ type
# mystery_3 is _____ type
# mystery_4 is _____ type
# mystery_5 is _____ type

# Verify answers:
print(f"mystery_1 type: {type(mystery_1)}")
print(f"mystery_2 type: {type(mystery_2)}")
print(f"mystery_3 type: {type(mystery_3)}")
print(f"mystery_4 type: {type(mystery_4)}")
print(f"mystery_5 type: {type(mystery_5)}")
```

### Mission 2: Type Conversion Challenge
```python
# Complete these conversions and handle possible errors:
test_values = ["123", "45.67", "True", "0", "", "abc", "3.14.15"]

for value in test_values:
    print(f"\nOriginal value: '{value}' (Type: {type(value).__name__})")

    # Try converting to different types
    try:
        print(f"✅ To integer: {int(value)}")
    except ValueError:
        print("❌ To integer: Failed")

    try:
        print(f"✅ To float: {float(value)}")
    except ValueError:
        print("❌ To float: Failed")

    print(f"✅ To boolean: {bool(value)}")
```

## 🌟 Key Points Summary

- ✅ **int (Integer)**: Numbers without decimal points, perfect for counting
- ✅ **float (Floating Point)**: Numbers with decimal points, perfect for precision
- ✅ **str (String)**: Text content, wrapped in quotes
- ✅ **bool (Boolean)**: Only True or False
- ✅ **type()** function: Your data type detective
- ✅ **Type conversion**: int(), float(), str(), bool() for data transformation

## 💡 Real-Life Applications

Mastering data types lets you:
- 🎮 Create game scoring systems (int)
- 💰 Handle shopping cart price calculations (float)
- 💬 Design chatbots (str)
- 🔍 Build smart decision systems (bool)

## 🚀 Next Lesson Preview

Next, we'll learn **Arithmetic Operations** - turn your program into a super calculator! Ready to solve all kinds of math problems with Python? 🔥
