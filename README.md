# Automate Mail Genarator

This project generates personalized invitation letters by replacing placeholders in a starting letter template with names from a list. Each generated invitation letter is saved as a separate text file ready to be sent.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:
`git clone https://github.com/Alisadaintanvir/automate-mail.git`

2. Change to the project directory:
 `cd automate-mail`

## Usage
1. Prepare the list of invited names:

Create a file named invited_names.txt in the ./Input/Names/ directory.
Add each invited name on a separate line in the file.

2. Customize the starting letter template:

Open the file ./Input/Letters/starting_letter.txt and replace the placeholder [name] with the appropriate variable or content.

3. Generate invitation letters:

### Run the following command:
`python main.py`

4. Find the generated invitation letters:

- The generated invitation letters will be saved as separate text files in the 
- `./Output/ReadyToSend/` directory with filenames corresponding to the invited names.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or inquiries, please contact:

Email: alisadaintanvir@gmail.com

