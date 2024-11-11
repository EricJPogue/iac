import subprocess

def git_add_commit_push(commit_message="Automated commit"):
    """Adds, commits, and pushes changes to the git repository."""
    # Run git add .
    add_result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
    if add_result.returncode != 0:
        print("Error with 'git add':", add_result.stderr)
        return

    # Run git commit -m "commit message"
    commit_result = subprocess.run(['git', 'commit', '-m', commit_message], capture_output=True, text=True)
    if commit_result.returncode != 0:
        print("Error with 'git commit':", commit_result.stderr)
        return

    # Run git push
    push_result = subprocess.run(['git', 'push'], capture_output=True, text=True)
    if push_result.returncode == 0:
        print("Changes pushed successfully.")
    else:
        print("Error with 'git push':", push_result.stderr)

if __name__ == "__main__":
    git_add_commit_push()