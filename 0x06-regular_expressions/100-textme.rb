#!/usr/bin/env ruby
# parse logfile and output [sender],[receiver],[flags]
# The following lines basically:
# 1. \[ & \] escapes the [] character since dey are meta characters
# (?:from:|to:|flags:)
# 2. () is used to create a group
# 3. ?: indicates that the groups should not be included in the capture,
# 	i.e. 'from:' would be omitted but values after it would be displayed
# 4. . permits any random character; since it is followed by * dat makes it any random chars
# 5. ? is used in this case to break words i.e. once a whitespace occurs, group the next chars are diff grp
puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
