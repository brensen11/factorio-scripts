-- convert.lua

-- Load the dkjson library
local dkjson = require("dkjson")

-- Load the data file. The dofile() function returns the last value, which is the data table.
local data = dofile("raw.lua")

-- Encode the Lua table into a JSON string.
-- The optional second argument is for pretty printing (indentation).
local json_string = dkjson.encode(data, {indent = true})

-- Write the JSON string to a new file.
local output_file = io.open("raw.json", "w")
if output_file then
    output_file:write(json_string)
    output_file:close()
    print("Successfully converted data-final-fixes.lua to output.json")
else
    print("Error: Could not open output.json for writing.")
end