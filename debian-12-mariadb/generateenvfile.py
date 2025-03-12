from faker import Faker

def generate_env_file(filename='.env'):
    """Generate a .env file with random credentials using Faker."""
    fake = Faker()

    # Generate random values
    mariadb_password = fake.password()
    mariadb_root_password = fake.password()
    moodle_admin_password = fake.password()

    # Content for .env file
    env_content = f"""MARIADB_PASSWORD={mariadb_password}
MARIADB_ROOT_PASSWORD={mariadb_root_password}
MOODLE_PASSWORD={moodle_admin_password}
"""

    # Write to .env file
    try:
        with open(filename, 'w') as f:
            f.write(env_content)
        print(f"Successfully created {filename} with random credentials:")
        print("-" * 50)
        print(env_content)
    except Exception as e:
        print(f"Error writing to {filename}: {e}")

if __name__ == "__main__":
    generate_env_file()