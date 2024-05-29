# Store the previously generated output in .txt files with the intent to compare their content to the current update

recursiveSearch() {
    for name in  "${1}"/*
    do
        if [ -d "${name}" ] # If current element is a folder (that contains files), then recursively iterate through its elements 
        then

        recursiveSearch "${name}"

        else
            FILE_EXTENSION=${name##*.}

            # Only execute files with the output extensions in the context of this project
            if [[ "$name" == *.html ]] || [[ "$name" == *.png ]]
            then
                FILE_PATH=\"${name}\" # Add double quotes to command to explicitly tell compiler that white spaces in the path to the .py file is compilable
                
                MY_COMMAND="${commandsMap[$FILE_EXTENSION]} ${FILE_PATH}"

                FILE_NAME=${name##*/}        # String for file name and extension e.g "1-advertise-tv-units-sold.png"
                FILE_ONLY=${FILE_NAME%.*}    # String for file name only e.g "1-advertise-tv-units-sold"

                cat "output-current/${FILE_EXTENSION}/${FILE_NAME}" > "output-previous/${FILE_EXTENSION}/${FILE_ONLY}.txt"
            fi
        fi
    done
}


###   STEP 1 - STORE PREVIOUSLY GENERATED OUTPUT AS .txt FILES in parallel directory   ###

START="./output-current" # Start folder
recursiveSearch "${START}"


###   STEP 2 - REMOVE THE PREVIOUSLY GENERATED OUTPUT FILES   ###

# Remove the previously generated output
rm -r output-current/*/*.html
rm -r output-current/*/*.png


###   STEP 3 - GENERATE NEW OUTPUT   ###

python relational-analysis.py