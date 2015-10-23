#!/BIN/BASH

if [ ! -d commits_art ]
  then
    mkdir commits_art
    cd commits_art
    git init
    touch commit_drawing.txt
  else
    cd commits_art
fi

NEW_DATE=$(date +"%a %b %d %H:%M:%S %Y %z")

# In Minutes :(
MINUTES_BACK=369

for x in $COMMITS
    do
        for i in $( seq 1 $x )
            do
                NEW_DATE=$(date -v -"$MINUTES_BACK"d +"%a %b %d %H:%M:%S %Y %z")
                echo $NEW_DATE >> commit_drawing.txt
                git add -A
                git commit -m "$NEW_DATE" --date="$NEW_DATE"
            done
        MINUTES_BACK=$[ $MINUTES_BACK-1 ]
    done