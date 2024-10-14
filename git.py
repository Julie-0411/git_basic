def display_git_commands():
    # Displaying Git commands for a typical workflow
    commands = [
        "1. git init                                  # Initialize a new Git repository",
        "2. git status                                # Check the status of the repository",
        "3. git add .                                 # Add all changes to the staging area",
        "4. git commit -m 'Commit message'            # Commit the changes with a message",
        "5. git remote add origin <repository_url>    # Add the remote repository (if not set)",
        "6. git push -u origin main                   # Push the changes to the main branch",
        "7. git remote -v                             # Verify the remote repository"
    ]

    # Display the commands one by one
    for command in commands:
        print(command)

if __name__ == "__main__":
    # Display the Git commands
    display_git_commands()
