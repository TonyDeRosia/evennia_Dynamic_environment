#!/usr/bin/env python3

import os
import subprocess
import sys

def print_status(message):
    """Print a status message."""
    print(f"[*] {message}")

def run_command(command, check=True):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e.stderr}")
        return None

def update_gitignore():
    """Update .gitignore with necessary entries."""
    entries = [
        "server/logs/",
        "server/*.pid",
        "server/*.db3",
        "__pycache__/",
        "*.pyc",
        "cleanup_git.py",
        "fix_git.py"
    ]
    
    # Read existing .gitignore
    existing_entries = []
    if os.path.exists('.gitignore'):
        with open('.gitignore', 'r') as f:
            existing_entries = f.read().splitlines()
    
    # Add new entries
    with open('.gitignore', 'a') as f:
        for entry in entries:
            if entry not in existing_entries:
                f.write(f"\n{entry}")
                print_status(f"Added {entry} to .gitignore")

def handle_rebase():
    """Handle the rebase in progress."""
    print_status("Handling rebase in progress...")
    
    # First, make sure the gitignore is updated
    update_gitignore()
    run_command("git add .gitignore")
    
    # Remove server logs from git tracking
    print_status("Removing server logs from git tracking...")
    run_command("git rm --cached server/logs/*.log 2>/dev/null || true")
    
    # Stage any remaining changes
    print_status("Staging remaining changes...")
    run_command("git add -A")
    
    # Amend the commit since we're in a rebase
    print_status("Amending the commit...")
    run_command('git commit --amend --no-edit')
    
    # Continue the rebase
    print_status("Continuing rebase...")
    result = run_command("git rebase --continue", check=False)
    
    if result is None:
        print_status("Rebase continuation failed. You may need to:")
        print("1. Run 'git status' to check the current state")
        print("2. Manually resolve any conflicts if they exist")
        print("3. Run 'git rebase --continue' when ready")
        sys.exit(1)

def main():
    """Main execution function."""
    print_status("Starting cleanup process...")
    
    # Handle the rebase first
    handle_rebase()
    
    # Show final status
    print_status("\nFinal repository status:")
    run_command("git status")

if __name__ == "__main__":
    main()
