def read_env_file_manual(filename='.env'):
    """Manually read and parse the .env file without dependencies."""
    env_vars = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Skip empty lines or comments
                line = line.strip()
                if line and not line.startswith('#'):
                    # Split on the first '=' only
                    if '=' in line:
                        key, value = line.split('=', 1)
                        env_vars[key] = value
        
        # Print the variables
        print(f"Successfully read {filename}:")
        print("-" * 50)
        for key, value in env_vars.items():
            print(f"{key}={value}")
        
        return env_vars
    
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None

if __name__ == "__main__":
    env_vars = read_env_file_manual()
    if env_vars:
        # Example: Access a specific variable
        print("\nExample usage:")
        print(f"Moodle admin password: {env_vars['MOODLE_PASSWORD']}")