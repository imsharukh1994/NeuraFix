import os
import json

class ProjectStorage:
    def __init__(self, project_dir="data/projects"):
        # Ensure the project directory exists
        self.project_dir = project_dir
        if not os.path.exists(self.project_dir):
            os.makedirs(self.project_dir)

    def save_project(self, project_name, code):
        """Save the project to a JSON file"""
        project_path = os.path.join(self.project_dir, f"{project_name}.json")
        
        # Data to be saved
        project_data = {
            "project_name": project_name,
            "code": code
        }

        try:
            with open(project_path, 'w') as file:
                json.dump(project_data, file, indent=4)
            print(f"Project '{project_name}' saved successfully!")
        except Exception as e:
            print(f"Error saving project: {e}")

    def load_project(self, project_name):
        """Load a project from a JSON file"""
        project_path = os.path.join(self.project_dir, f"{project_name}.json")
        
        if not os.path.exists(project_path):
            print(f"Project '{project_name}' not found!")
            return None

        try:
            with open(project_path, 'r') as file:
                project_data = json.load(file)
            print(f"Project '{project_name}' loaded successfully!")
            return project_data["code"]  # Return the saved code
        except Exception as e:
            print(f"Error loading project: {e}")
            return None

    def list_projects(self):
        """List all available projects"""
        try:
            files = os.listdir(self.project_dir)
            projects = [file.split('.')[0] for file in files if file.endswith('.json')]
            return projects
        except Exception as e:
            print(f"Error listing projects: {e}")
            return []

    def delete_project(self, project_name):
        """Delete a project from storage"""
        project_path = os.path.join(self.project_dir, f"{project_name}.json")
        
        if not os.path.exists(project_path):
            print(f"Project '{project_name}' not found!")
            return False

        try:
            os.remove(project_path)
            print(f"Project '{project_name}' deleted successfully!")
            return True
        except Exception as e:
            print(f"Error deleting project: {e}")
            return False