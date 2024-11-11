import subprocess


def list_directory_contents(path='.'):
    """Lists the contents of a directory."""
    result = subprocess.run(['ls', path], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Directory contents:")
        print(result.stdout)  # Display the output of `ls`
    else:
        print("An error occurred. Could not list directory contents.")

def check_git_status():
    """Checks the Git status of the current repository."""
    result = subprocess.run(['git', 'status'], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Git status:")
        print(result.stdout)  # Display the output of `git status`
    else:
        print("Not a git repository or an error occurred with git status.")

if __name__ == "__main__":
    # List the contents of the current directory
    list_directory_contents()
    
    # Check the git status in the current directory
    check_git_status()
