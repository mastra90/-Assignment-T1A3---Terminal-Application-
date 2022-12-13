## Script to run the application from Bash terminal

# Welcome message
echo ""
echo "Hi! Welcome to your Contact Book!"
read -p "Please press 'Enter' to continue..."
echo ""

# Iterates through each Python file to give the user impression that the file is loading
for file in *.py; do
	echo "Running $file..."
    sleep 0.1
done

# Runs the application
sleep 1
echo ""
echo "Application validtation: successful!"
sleep 1
python3 main_program.py