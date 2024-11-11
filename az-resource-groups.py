import subprocess

def list_azure_resource_groups():
    """Lists all Azure resource groups."""
    result = subprocess.run(['az', 'group', 'list', '--output', 'table'], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Azure Resource Groups:")
        print(result.stdout)
    else:
        print("Error listing Azure resource groups:", result.stderr)

if __name__ == "__main__":
    list_azure_resource_groups()
