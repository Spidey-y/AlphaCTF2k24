#!/bin/rbash

banner="======================================================"
alpha='^[a-zA-Z]+$'
numeric='^[0-9]+$'
underscore='^[_]+$'
pattern='^[a-zA-Z0-9_]+$'
blacklist=("env" "FLAG" "set" "declare" "{")


while true
do
    read -p "gimme somethin and i'll sing u a song: " input
    command="echo Your input was \"$input\""
    echo 

    if [[ "$input" == "exit" ]]; then
        exit

    else
        for word in "${blacklist[@]}"; do
            if [[ $input == *"$word"* ]]; then
                echo "Hacking Attempt Detected!🚨" >&2
                exit 1
            fi
        done

        if echo "$input" | grep -qE "$alpha"; then
            echo "$banner"
            echo "In a world of letters, your input shines bright,
            A symphony of alphabets, dancing in the light.
            No digits or symbols, just A to Z's delight,
            Your input, a poem, feels just right."
            echo "$banner"

            eval "$command"
            echo 

        elif [ "$(echo "$input" | tr -cd "$numeric")" = "$input" ]; then
            echo "$banner"
            echo "Your input sails with numbers bold,
            A symphony of digits, a story to be told.
            From zero to nine, a numeric dance,
            In the realm of numbers, we step in advance."
            echo "$banner"

            eval "$command"
            echo

        elif echo "$input" | sed -n -E "/$pattern/p" | grep -q .; then
            echo "$banner"
            echo " Characters unite,
            like they're ready to fight."
            echo "$banner"

            eval "$command"
            echo

        elif [[ "$input" =~ "$underscore" ]]; then
            echo "$banner"
            echo "In the code's whisper, where characters underscore,"
            echo "A story unfolds, ready to soar."
            echo "$banner"

            eval "$command"
            echo

        else
            echo "Invalid input: $input" >&2
        fi
    fi
done
