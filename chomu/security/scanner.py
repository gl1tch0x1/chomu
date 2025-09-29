import subprocess

def run_lynis_scan():
    try:
        result = subprocess.run(['lynis', 'audit', 'system', '--quick'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f'Error running Lynis: {e}'
