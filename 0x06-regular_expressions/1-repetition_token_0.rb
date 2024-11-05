#!/usr/bin/env ruby

import ARGV

regex = /hb?t/

input_text = ARGV[0]

if input_text =~ regex
  puts input_text
end
