echo "Enter commit message"
read message

git add .
git commit -m "$message"
git push

echo "Push successful, with commit message : $message"