#!/usr/local/bin/bash

THIS="$0"
[[ "$THIS" == "-bash" ]] && THIS="$1"

BASE="$(readlink -f "$THIS")"
BASE="$(dirname "$BASE")"

echo BASE=$BASE

find . -name *.html 				|\
grep -v node_modules 				|\
while read FILE
do
	SHOT="${FILE/.html/.png}"
	SHOT="${SHOT/solution/exercise}"

	FLDR="${SHOT%/*}"
	SHOT="${FLDR}/SOLUTION.png"

	echo "$FILE -> $SHOT"

	node $BASE/screenshot.js  "$FILE" "$SHOT"
done

