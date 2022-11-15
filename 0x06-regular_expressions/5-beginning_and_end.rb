#!/usr/bin/env ruby
# Match any 3 letter words that starts with h and ends with n

puts ARGV[0].scan(/^h.n$/).join
