HANDLED_FILE=$1
REPLACE_MARK=$2
SOURCE_VARIABLE=$(echo $@ | awk '{for (i=3; i<=NF; i++) printf $i}')

# echo "Entered variable: \"${SOURCE_VARIABLE}\""

FINAL_VARIABLE=$(echo ${SOURCE_VARIABLE} | sed 's/ //g' | awk -F ',' '
BEGIN {printf "["}
{for (i=1; i<NF; i++) printf "\"" $i "\", "}
END {printf "\"" $NF "\"]"}
')

# echo "Final variable: ${FINAL_VARIABLE}"
# echo "${HANDLED_FILE}"
# echo "${REPLACE_MARK}"
# echo "${FINAL_VARIABLE}"

sed -i "s/${REPLACE_MARK}/${FINAL_VARIABLE}/g" ${HANDLED_FILE}
