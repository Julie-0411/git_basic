# Git Basic

This project demonstrates the basic workflow of using Git for version control. It includes initializing a Git repository, tracking changes, committing updates, and pushing changes to a remote repository on GitHub.

## Features

- Initialize a new Git repository
- Track file changes and view the status
- Stage files for committing
- Commit changes with descriptive messages
- Set up a remote repository
- Push changes to the remote repository
- Resolve common Git errors (e.g., non-fast-forward push issues)

## Prerequisites

Before using this project, make sure you have the following installed:

- [Git](https://git-scm.com/downloads) - A distributed version control system
- [GitHub account](https://github.com/) - For creating a remote repository

## Git Workflow

Here are the basic steps covered in this project:

1. **Initialize a Git Repository**  
   Use `git init` to initialize a new Git repository in your project folder.
   ```bash
   git init
   ```

2. **Check the Status of the Repository**  
   Use `git status` to check the status of your repository and see which files have been modified or added.
   ```bash
   git status
   ```

3. **Add Changes to the Staging Area**  
   Use `git add` to stage the changes you want to commit.
   ```bash
   git add .
   ```

4. **Commit the Changes**  
   Use `git commit` to commit your changes with a meaningful message.
   ```bash
   git commit -m "Add a meaningful commit message"
   ```

5. **Add a Remote Repository**  
   Link your local repository to a remote GitHub repository using `git remote add`.
   ```bash
   git remote add origin https://github.com/your-username/git_basic.git
   ```

6. **Push Changes to the Remote Repository**  
   Use `git push` to push your local commits to the remote repository.
   ```bash
   git push -u origin main
   ```

7. **Pull Changes from the Remote Repository (if needed)**  
   If you encounter a non-fast-forward error, use `git pull` to integrate changes.
   ```bash
   git pull origin main
   ```

## Common Git Issues

- **Non-fast-forward Error**  
  If your local branch is behind the remote branch, you'll need to pull the changes first.
  ```bash
  git pull origin main
  ```

- **Files Not Being Tracked**  
  Ensure you add the files using `git add` and that they are not ignored in `.gitignore`.

## Project Structure

```
/git_basic
├── .gitignore          # List of files and directories ignored by Git
├── README.md           # Project documentation
└── your-files-here     # Add your project files
```

## Author

- **Julie**  
  GitHub: [Julie-0411](https://github.com/Julie-0411)
