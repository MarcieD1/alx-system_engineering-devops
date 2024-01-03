# Regular Expressions Project

This project involves creating Ruby scripts that utilize regular expressions using the Oniguruma library. Each script is designed to match specific patterns or criteria.

## Scripts and Descriptions

### 0-simply_match_school.rb

This script matches the string "School" in the input.

### 1-repetition_token_0.rb

Matches strings that contain "hb", followed by zero or more "t" characters, and ending with "n".

### 2-repetition_token_1.rb

Matches strings that start with "h", followed by one to four occurrences of "b" or "t", and ending with "n".

### 3-repetition_token_2.rb

Matches strings that start with "h", followed by "bt", and ending with zero or more "n" characters.

### 4-repetition_token_3.rb

Matches strings that start with "h", followed by any character except "b", "t", "n", "r", "u", or "e", and ending with "n".

### 5-beginning_and_end.rb

Matches strings that start with "h", followed by any character, and ending with "n".

### 6-phone_number.rb

Matches 10-digit phone numbers.

### 7-OMG_WHY_ARE_YOU_SHOUTING.rb

Matches capital letters in a given string.

## Usage

To run any of the scripts, use the following format:

```bash
./script_name.rb "input_string"
Replace script_name.rb with the desired script and "input_string" with the input you want to test.

Example
bash
Copy code
./0-simply_match_school.rb "Best School"

# Output: School

### Requirements
Ruby

Oniguruma library
Ubuntu 20.04 LTS

Author
Marcia
