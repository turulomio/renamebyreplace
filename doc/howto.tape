# VHS documentation
#
# Output:
#   Output <path>.gif               Create a GIF output at the given <path>
#   Output <path>.mp4               Create an MP4 output at the given <path>
#   Output <path>.webm              Create a WebM output at the given <path>
#
# Require:
#   Require <string>                Ensure a program is on the $PATH to proceed
#
# Settings:
#   Set FontSize <number>           Set the font size of the terminal
#   Set FontFamily <string>         Set the font family of the terminal
#   Set Height <number>             Set the height of the terminal
#   Set Width <number>              Set the width of the terminal
#   Set LetterSpacing <float>       Set the font letter spacing (tracking)
#   Set LineHeight <float>          Set the font line height
#   Set LoopOffset <float>%         Set the starting frame offset for the GIF loop
#   Set Theme <json|string>         Set the theme of the terminal
#   Set Padding <number>            Set the padding of the terminal
#   Set Framerate <number>          Set the framerate of the recording
#   Set PlaybackSpeed <float>       Set the playback speed of the recording
#   Set MarginFill <file|#000000>   Set the file or color the margin will be filled with.
#   Set Margin <number>             Set the size of the margin. Has no effect if MarginFill isn't set.
#   Set BorderRadius <number>       Set terminal border radius, in pixels.
#   Set WindowBar <string>          Set window bar type. (one of: Rings, RingsRight, Colorful, ColorfulRight)
#   Set WindowBarSize <number>      Set window bar size, in pixels. Default is 40.
#   Set TypingSpeed <time>          Set the typing speed of the terminal. Default is 50ms.
#
# Sleep:
#   Sleep <time>                    Sleep for a set amount of <time> in seconds
#
# Type:
#   Type[@<time>] "<characters>"    Type <characters> into the terminal with a
#                                   <time> delay between each character
#
# Keys:
#   Escape[@<time>] [number]        Press the Escape key
#   Backspace[@<time>] [number]     Press the Backspace key
#   Delete[@<time>] [number]        Press the Delete key
#   Insert[@<time>] [number]        Press the Insert key
#   Down[@<time>] [number]          Press the Down key
#   Enter[@<time>] [number]         Press the Enter key
#   Space[@<time>] [number]         Press the Space key
#   Tab[@<time>] [number]           Press the Tab key
#   Left[@<time>] [number]          Press the Left Arrow key
#   Right[@<time>] [number]         Press the Right Arrow key
#   Up[@<time>] [number]            Press the Up Arrow key
#   Down[@<time>] [number]          Press the Down Arrow key
#   PageUp[@<time>] [number]        Press the Page Up key
#   PageDown[@<time>] [number]      Press the Page Down key
#   Ctrl+<key>                      Press the Control key + <key> (e.g. Ctrl+C)
#
# Display:
#   Hide                            Hide the subsequent commands from the output
#   Show                            Show the subsequent commands in the output

Output howto.gif

Require echo

Set Shell "bash"
Set FontSize 14
Set Width 1200
Set Height 800
Set WindowBar Colorful

# Espera un segundo para que la terminal aparezca
Sleep 1s
Type "# This is a video to show how to use 'toomanyfiles' command" Sleep 1s Enter
Type "# We have a directory with 100 files that have a time pattern '%Y%m%d %H%M' with a day variation" Sleep 1s Enter
Type "# We are going to see the 5 last files of this directory" Sleep 1s Enter
Type "ls -la | tail -n 5" Sleep 1s Enter
Type "# We use to find this kind of files in automatic backups, logs, ..." Sleep 1s Enter
Type "# If you want to save our disk space and you want to keep some of them, you can use TooManyFiles program" Sleep 1s Enter
Type "# So, you want to keep the last 5 files because they are too recent." Sleep 1s Enter
Type "# And, you want to keep the first file of each month from the rest of the files until a max number the files of 15." Sleep 1s Enter
Type "toomanyfiles --too_young_to_delete 5 --max_files_to_store 15 --time_pattern '%Y%m%d %H%M' --remove" Sleep 1s Enter
Sleep 5s
Type "ls -la" Sleep 1s Enter
Type "You can use other parameters like --list or --pretend before --remove to check files to delete" Sleep 10s Enter



