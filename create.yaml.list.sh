set -x
HANDLED_FILE="$1"
REPLACE_MARK="$2"
SOURCE_VARIABLE="$(echo $@ | awk '{for (i=3; i<=NF; i++) printf $i}')"

# echo "$@" >> /tmp/bootstrap.output.txt

if [ "${SOURCE_VARIABLE}" == "~" ]
  then
    sed -i "s/${REPLACE_MARK}/~/g" ${HANDLED_FILE}
  else
    FINAL_VARIABLE=$(echo ${SOURCE_VARIABLE} | sed 's/ //g' | awk -F ',' '
    BEGIN {printf "["}
    {for (i=1; i<NF; i++) printf "\"" $i "\", "}
    END {printf "\"" $NF "\"]"}
    ')

    sed -i "s/${REPLACE_MARK}/${FINAL_VARIABLE}/g" ${HANDLED_FILE}
fi
