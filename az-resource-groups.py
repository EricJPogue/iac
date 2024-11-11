import subprocess
import sys

def list_azure_resource_groups():
	"""Lists all Azure resource groups."""
	result = subprocess.run(['az', 'group', 'list', '--output', 'table'], capture_output=True, text=True)

	if result.returncode == 0:
		print("Azure Resource Groups:")
		print(result.stdout)
	else:
		print("Error listing Azure resource groups:", result.stderr)

def delete_azure_resource_group(resource_group_name):
	"""Deletes a specified Azure resource group."""
	print(f"Deleting Azure resource group: {resource_group_name}")

	# result = subprocess.run(['az', 'group', 'delete', '--name', resource_group_name], capture_output=True, text=True)
	result = subprocess.run(['az', 'group', 'delete', '--name', resource_group_name, '--yes', '--no-wait'], capture_output=True, text=True)

	if result.returncode == 0:
		print(f"Resource group '{resource_group_name}' deletion initiated successfully.")
	else:
		print(f"Error deleting resource group '{resource_group_name}':", result.stderr)


if __name__ == "__main__":
	list_azure_resource_groups()

	if len(sys.argv) > 2:
		if sys.argv[1] == 'delete':
			resource_group_name = sys.argv[2]
			delete_azure_resource_group(resource_group_name)

