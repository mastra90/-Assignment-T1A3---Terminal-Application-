## Script to run the application from Bash terminal

# Welcome message
echo ""
echo "Hi! Welcome to your Contact Book!"
read -p "Please press 'Enter' to start the application..."
echo ""

# Iterates through each Python file to give the user impression that the file is loading
for file in *.py; do
	echo "Running $file..."
    sleep 0.05
done

# Runs the application
sleep 0.3
echo ""
echo "Application is about to start..."
echo ""
sleep 1.2
python3 main_program.py