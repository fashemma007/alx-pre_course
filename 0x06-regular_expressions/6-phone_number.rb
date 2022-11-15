#!/usr/bin/env ruby
# Match a string starting wit a number and has exactly 10 numbers, not more not less

puts ARGV[0].scan(/^[0-9]{10}$/).join
