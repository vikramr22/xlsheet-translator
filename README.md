## Excel Sheet Translator

A simple Python script to translate Excel sheets using Google Translate.

### Installation

Make sure you have the required packages installed:

```bash
pip install googletrans==3.1.0a0 pandas
```

### Usage  
Run the script from the command line:

```bash
python xl_translation.py <xl file path>
```
Replace <xl file path> with the path to your Excel file.

Example
Assuming you have an Excel file named example.xlsx:

```bash
python xl_translation.py example.xlsx
```
The translated file (example_translated.xlsx) will be created in the same directory.

### Features 
•Translates Excel columns from any language to English. <br>
•Utilizes Google Translate API for efficient translation. <br>
•Supports parallel translation for improved performance. <br>

### Contributing
Feel free to contribute to the project by opening issues or submitting pull requests.
