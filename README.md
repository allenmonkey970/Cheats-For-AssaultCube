# Cheats For AssaultCube

This repository contains a cheat engine for the game AssaultCube, implemented in Python using the `pymem` library. The code allows manipulation of various in-game values such as health, armor, and ammunition.

## Features

- **Health Pointer:** Modify the player's health value.
- **Default Gun Pointer:** Adjust the default gun's attributes.
- **Armor Pointer:** Change the armor value.
- **Grenades Pointer:** Control the number of grenades.
- **Pistol Pointer:** Tweak the pistol's attributes.
- **Dual Pistols Pointer:** Modify the dual pistols' properties.

## Prerequisites

- Python 3.x
- `pymem` library

Install `pymem` using pip:

```bash
pip install pymem
```

## Usage

1. Download and install AssaultCube from the following link: [AssaultCube v1.2.0.2](https://github.com/assaultcube/AC/releases/tag/v1.2.0.2)
2. Ensure the game is running.
3. Run the script:

```bash
python your_script.py
```

## Description

The script initializes `pymem` and the game module, then fetches various pointers related to in-game values. It provides functions to get pointer addresses, continuously write values, and toggle writing on and off.

## Functions

- `get_ptr_addr(base, offsets)`: Retrieves the pointer address based on base and offsets.
- `get_ptrs()`: Fetches and returns a tuple of pointers and their descriptions.
- `infinite_write(hack_ptrs)`: Continuously writes values to the pointers.
- `toggle_writing()`: Toggles the infinite writing on and off based on user input.

## Running the Script

1. Start the game.
2. Run the script using Python.
3. Press Enter to toggle infinite writing on and off.

## Notes

- Ensure the game is running before starting the script.
- The script will continuously write values to the pointers until stopped.

## Project Note

This project was created as the final assignment for my CSCI 110 class.

Feel free to contribute and improve the code!
