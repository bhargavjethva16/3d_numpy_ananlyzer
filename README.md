# NumPy Analyzer

## Overview

- NumPy Analyzer is a menu-driven Python application developed using the NumPy library. It allows users to create and manipulate 1D, 2D, and 3D arrays and perform various mathematical, searching, sorting, filtering, and statistical operations.
- The program provides an interactive command-line interface where users can select different operations and view their results directly in the terminal.

## Project Objective

- The objective of this project is to understand and demonstrate the practical use of NumPy in Python. It focuses on array creation, array manipulation, mathematical operations, searching, sorting, filtering, and basic statistical analysis through a simple menu-driven application.

## Features

- **Array Creation:** Create 1D, 2D, and 3D NumPy arrays.
- **Indexing and Slicing:** Access individual array elements and extract specific portions of an array.
- **Mathematical Operations:** Perform addition, subtraction, multiplication, and division between arrays.
- **Array Combining and Splitting:** Combine arrays or divide an existing array into multiple parts.
- **Searching and Sorting:** Search for specific values and arrange array elements in sorted order.
- **Filtering:** Select array elements based on less-than and greater-than conditions.
- **Statistical Operations:** Calculate the sum, mean, and median of array elements.
- **Input Validation:** Check certain user inputs, including array sizes and division by zero.
- **Interactive Menu:** Access the program's features through a numbered main menu.

## Requirements

- Python 3.x
- NumPy library
- Git
- GitHub
- Visual Studio Code (VS Code), or another Python-compatible editor

## Installation

### 1. Install Python

Download and install Python 3.x from the official website:

[https://www.python.org/](https://www.python.org/)

### 2. Install NumPy

Open the terminal and run the following command:

```bash
python -m pip install numpy
```

### 3. Open the Project

Open the project folder in VS Code or your preferred code editor.

## How to Run

1. Save the Python code in a file named `main.py`.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python main.py
```

4. The NumPy Analyzer main menu will appear in the terminal.
5. Enter the number corresponding to the operation you want to perform.

## Main Menu Explanation

The program provides six main menu options.

### 1. Create a NumPy Array

This option allows users to create an array of their preferred dimension.

**Available array types:**

- **1D Array:** Creates a one-dimensional array containing integer elements.
- **2D Array:** Creates a two-dimensional array using the specified number of rows and columns.
- **3D Array:** Creates a three-dimensional array using the specified number of layers, rows, and columns.

After selecting the array type, users enter the required elements. The program converts the input into a NumPy array, stores it, and displays the created array.

### 2. Perform Mathematical Operations

This option performs mathematical calculations between the existing array and a second array of the same shape.

**Available operations:**

- **Addition:** Adds corresponding elements of the two arrays.
- **Subtraction:** Subtracts each element of the second array from the corresponding element of the original array.
- **Multiplication:** Multiplies corresponding elements of both arrays.
- **Division:** Divides each element of the original array by the corresponding element of the second array.

The program checks whether the number of entered elements matches the size of the original array. It also prevents division when the second array contains zero.

### 3. Combine or Split Arrays

This option allows users to combine arrays or divide an existing array into smaller parts.

**Available operations:**

- **Combine Array:** Takes another array with the same shape as the original array and combines them. For 1D arrays, concatenation is used. For multidimensional arrays, vertical stacking is used.
- **Split Array:** Divides the original array into a specified number of parts using NumPy's `array_split()` function.

The resulting combined array or individual split parts are displayed in the terminal.

### 4. Search, Sort, or Filter Arrays

This option provides tools for finding values and organizing array data.

**Available operations:**

- **Search a Value:** Searches for a specific integer in the array and displays its index location if found. If the value does not exist, the program displays a message.
- **Sort the Array:** Arranges the array elements in sorted order using NumPy's `sort()` function.
- **Filter Values:** Selects array elements according to a specified condition.

The filtering feature includes two options:

- **Values Less Than:** Displays elements smaller than the entered value.
- **Values Greater Than:** Displays elements larger than the entered value.

These operations help users locate, organize, and analyze specific array elements.

### 5. Compute Aggregates and Statistics

This option calculates basic statistical values from the existing array.

**Available operations:**

- **Sum:** Calculates the total of all elements using `numpy.sum()`.
- **Mean:** Calculates the arithmetic average of the elements using `numpy.mean()`.
- **Median:** Calculates the middle value of the elements using `numpy.median()`.

The program displays the original array along with the calculated result.

### 6. Exit

This option terminates the program. A closing message is displayed to indicate that the user has exited the NumPy Analyzer.

## Indexing and Slicing

The program also contains an indexing and slicing function that can be used to access individual elements or selected ranges of an array.

### Indexing

Indexing retrieves a specific element from an array.

- **1D Array:** Uses one index to access an element.
- **2D Array:** Uses a row index and a column index.
- **3D Array:** Uses a layer index, row index, and column index.

### Slicing

Slicing extracts a selected range of elements from an array.

- **1D Array:** Selects elements using a start and end index.
- **2D Array:** Selects a range of rows and columns.
- **3D Array:** Selects a range of layers, rows, and columns.

The slicing ranges follow NumPy's standard convention: the start index is included, while the end index is excluded.

**Note:** In the supplied code, indexing and slicing are implemented in a separate function, but they are not connected to an option in the main menu. The function must be called separately to access these features.

## Technologies Used

- **Python:** Used to develop the program and implement its logic.
- **NumPy:** Used for array creation, mathematical calculations, sorting, filtering, splitting, and statistical operations.
- **Visual Studio Code:** Can be used to write, edit, and run the Python program.
- **Git and GitHub:** Can be used for version control and project sharing.



## Project Structure

/

├── main.py

├── output.png

└── README.md



## Output

![Program Output](output.pnj)

##

## Conclusion

NumPy Analyzer brings several fundamental array-processing operations together in one interactive Python program. It helps users understand how NumPy simplifies numerical computations and data manipulation while providing practical experience with Python programming.



## Author

Bhargav

