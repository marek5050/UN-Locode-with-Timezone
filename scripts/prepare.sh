sed 's/\"\"\"/\"/g' ./data/*.csv > ./data/all_data.csv

echo 'db="""' > ./endpoint/main.py
cat ./data/all_data.csv >> ./endpoint/main.py
echo '"""' >> ./endpoint/main.py
cat ./endpoint/main.t.py >> ./endpoint/main.py

cat ./README.t.md > ./README.md
echo "Last updated: " `date` >> ./README.md
echo "\`\`\`" >> ./README.md
head ./data/*.csv >> ./README.md
echo "\`\`\`" >> ./README.md
