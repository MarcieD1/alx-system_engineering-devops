#!/usr/bin/env ruby

log_line = ARGV[0]

# Regular expression to extract relevant information
regex = /\[from:(?<sender>[\w+\d]+)\] \[to:(?<receiver>[\+\d]+)\] \[flags:(?<flags>[-\d:]+)\]/

# Match the regular expression against the log line
match_data = log_line.match(regex)

# Output the results in the specified format
if match_data
  sender = match_data[:sender]
  receiver = match_data[:receiver]
  flags = match_data[:flags]

  puts "#{sender},#{receiver},#{flags}"
else
  puts "No match found in the log line."
end
