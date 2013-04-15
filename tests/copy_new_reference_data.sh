#!/bin/sh
cd reference_data
for filename in `/bin/ls`; do
    if [ -f ../$filename ]; then
        cp ../$filename $filename
    fi
done

