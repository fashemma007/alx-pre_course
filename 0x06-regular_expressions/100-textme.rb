#!/usr/bin/env ruby
# parse logfile and output [sender],[receiver],[flags]
# The following lines basically:
# 1. \[ & \] escapes the [] character since dey are meta characters
# (?:from:|to:|flags:)
# 2. () is used to create a group
# 3. ?: indicates a truncation at : 
puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
