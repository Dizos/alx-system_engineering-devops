#!/usr/bin/env ruby

import ARGV

regex = /hb{1,3}t/

input_text = ARGV[0]

if input_text =~ regex
  puts input_text
end
