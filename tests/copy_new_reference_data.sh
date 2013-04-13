#!/bin/sh
cd reference_data
for filename in `/bin/ls`; do
    cp ../$filename $filename
done

