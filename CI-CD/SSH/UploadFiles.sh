USER_NAME="Test"
SERVER="101.101.01.10"
SOURCE_FOLDER="C:/Users/ME/Documents/Study/Mastering-Snowflake"
DESTINATION_FOLDER="destination/folder"

echo "scp -r ${USER_NAME}@${SERVER}:${DESTINATION_FOLDER} $SOURCE_FOLDER"

for file in ${SOURCE_FOLDER}/*; do
    echo "$file is found"
done

read -p "entry any key to stop"