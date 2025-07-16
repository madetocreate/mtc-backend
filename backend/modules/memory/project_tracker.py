def update_readme(project, task):
    with open(f"memory/projects/{project}/README.md", "a") as f:
        f.write(f"- [x] {task}\n")
