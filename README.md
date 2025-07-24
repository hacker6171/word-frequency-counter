# Word Frequency Counter

A simple Python script to analyze a text file, count the frequency of each word, and display basic statistics about the content.

## Features

- Reads a text file provided by the user
- Counts the frequency of each word (case-insensitive)
- Displays the top 10 most frequent words
- Reports the total number of words and sentences
- Calculates the average sentence length (in words)

## How It Works

1. **Load a Text File:**  
   The script prompts you for the file path of the text document you want to analyze.

2. **Process the Text:**  
   - Converts text to lowercase for accurate counting  
   - Uses regular expressions to identify words and sentences

3. **Compute Statistics:**  
   - Total number of words  
   - Total number of sentences  
   - Average words per sentence  
   - The ten most common words and their frequencies

4. **Displays Results:**  
   All results are printed to the console for quick review.

## Usage

1. **Clone or Download this Repository**

2. **Add the Script**  
   Save the code as `word_frequency_counter.py` in your local directory.

3. **Run the Script**

4. **Follow Prompts**  
Enter the path to your text file when asked.

## Example Output

Total words: 523
Total sentences: 42
Average sentence length (words): 12.45

Word Frequency (top 10):
the: 45
and: 31
to: 28
of: 25
a: 23
in: 20
it: 17
is: 14
that: 13
for: 12


## Requirements

- Python 3.7 or above

## Customization Ideas

- Exclude common stop words (`the`, `and`, etc.)  
- Output results to a file (CSV or text)  
- Analyze multiple files in one command  
- Build a simple graphical or web interface

## License

This project is licensed under the None. Feel free to use, modify, and share!

## Contributing

Pull requests and suggestions are welcome. If you notice a bug or have ideas for improvements, please open an issue or submit a pull request.
