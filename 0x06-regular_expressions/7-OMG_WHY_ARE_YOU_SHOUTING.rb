#!/usr/bin/env ruby

import ARGV

# The regular expression to match capital letters
regex = /[A-Z]+/

# Get the argument passed to the script
input_text = ARGV[0]

# Find all matches in the input text
matches = input_text.scan(regex)

# Print the matched capital letters
puts matches.join
end
