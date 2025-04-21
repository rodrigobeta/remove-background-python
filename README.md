# Remove Background from Images using Python

A guide to remove backgrounds from images using Python and the `rembg` library.

---

## 📚 Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [How it Works](#how-it-works)
  - [Code Components](#code-components)
  - [Background Removal Process](#background-removal-process)
  - [Error Handling](#error-handling)
- [Output](#output)
- [Project Structure](#project-structure)

---

## ✅ Requirements

- Python 3.x  
- `pip` (Python package installer)  
- Virtual environment (recommended)

---

## ⚙️ Installation

1. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   ```

2. **Activate virtual environment**
   ```bash
   source venv/bin/activate
   ```

3. **Install required libraries**
   ```bash
   python -m pip install rembg pillow
   ```

---

## ▶️ How to Use

1. Place your image in the same directory as the script  
2. Rename your image to `input.png` or modify the `input_path` in the code  
3. Run the script:  
   ```bash
   python main.py
   ```
4. The output will be saved as `output.png`

---

## 🧠 How it Works

### Code Components

#### 1. Imports

- `rembg`: Main library for background removal  
- `PIL`: Python Imaging Library for image processing  
- `os`: For file operations  
- `sys`: For system operations

#### 2. `remove_background()` function

- Checks if input file exists  
- Opens the image using PIL  
- Removes background using rembg  
- Saves the processed image  
- Shows the result

#### 3. `main()` function

- Defines input and output paths  
- Calls `remove_background()` function

---

### 🪄 Background Removal Process

The `rembg` library:

- Uses a deep learning model (U2-Net)  
- Analyzes the image to identify foreground objects  
- Creates an alpha channel mask  
- Removes the background pixels  
- Preserves the foreground with transparency

---

### 🛡️ Error Handling

- Checks for missing input files  
- Handles processing errors gracefully  
- Provides informative error messages

---

## 🖼️ Output

- Saves the processed image in PNG format  
- Preserves transparency  
- Displays the result automatically

---

## 📁 Project Structure

```
remove_background/
├── main.py
├── input.png
├── output.png
└── venv/
```
