# Phonetic Alphabet Converter

This Python script allows you to convert any given word into its phonetic code words using the NATO phonetic alphabet. The script reads the NATO phonetic alphabet from a CSV file and creates a dictionary for easy lookup. 

## Installation

1. Clone the repository or download the script files.
2. Make sure you have Python installed on your system. This script requires Python 3.x.
3. Install the necessary Python packages using pip:
    ```sh
    pip install pandas
    ```

## Usage

1. Ensure you have a CSV file named `nato_phonetic_alphabet.csv` in the same directory as the script. The CSV should have the following format:
    ```
    letter,code
    A,Alfa
    B,Bravo
    C,Charlie
    ...
    ```

2. Run the script:
    ```sh
    python phonetic_converter.py
    ```

3. Follow the prompt to enter a word. The script will output the phonetic code words for each letter in the word.

## Script Details

The script performs the following steps:

1. **Importing Pandas:**
    ```python
    import pandas
    ```

2. **Reading the CSV file:**
    ```python
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    df = pandas.DataFrame(data)
    ```

3. **Creating the dictionary:**
    ```python
    new_dict = {row.letter: row.code for (index, row) in df.iterrows()}
    ```

4. **Generating the phonetic code words:**
    ```python
    def generate_phonetic():
        word = input("Enter a word: ").upper()
        new_list = [char for char in word]

        try:
            result = [new_dict[letter] for letter in new_list]
        except KeyError:
            print("Sorry, only letters in the alphabet, please")
            generate_phonetic()
        else:
            print(result)

    generate_phonetic()
    ```

## Example

Here is an example of how the script works:

- If the user inputs the word `Hello`, the script will output:
    ```
    ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
    ```

## Error Handling

The script includes basic error handling to ensure that only alphabetic characters are processed. If the user enters a non-alphabetic character, they will be prompted to enter a valid word again.

