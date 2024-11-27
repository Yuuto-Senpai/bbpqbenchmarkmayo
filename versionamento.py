import subprocess

def get_current_version():
    result = subprocess.run(
        ["git", "describe", "--tags", "--abbrev=0"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def increment_version(version, level):
    major, minor, patch = map(int, version.split('.'))
    if level == "major":
        major += 1
        minor = 0
        patch = 0
    elif level == "minor":
        minor += 1
        patch = 0
    elif level == "patch":
        patch += 1
    return f"{major}.{minor}.{patch}"

def create_new_tag(new_version):
    subprocess.run(["git", "tag", "-a", f"v{new_version}", "-m", f"Versão {new_version}"])
    subprocess.run(["git", "push", "origin", "--tags"])

if __name__ == "__main__":
    current_version = get_current_version()
    print(f"Versão atual: {current_version}")
    level = input("Digite o tipo de incremento (major, minor, patch): ").strip()
    new_version = increment_version(current_version, level)
    print(f"Nova versão: {new_version}")
    create_new_tag(new_version)
