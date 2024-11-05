#!/usr/bin/env ruby

import ARGV

regex = /hbt*/

input_text = ARGV[0]

if input_text =~ regex
  puts input_text
end
