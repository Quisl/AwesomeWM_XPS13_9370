--[[
MIT License

Copyright (c) 2020 Jonas Christian Rabe aka Quisl (https://github.com/Quisl)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
--]]
local wibox = require("wibox")
local awful = require("awful")
local gears = require("gears")
local watch = require("awful.widget.watch")

system_widget = wibox.widget{
    font = "Play 9",
    widget = wibox.widget.textbox,
    markup = ""
}

watch(
    "python ".. configpath .."scripts/memory.py", 3,
    function(widget, stdout, stderr, exitreason, exitcode)
        system_widget.markup=stdout
    end
)
