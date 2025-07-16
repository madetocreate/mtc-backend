import sys
def run_task(prompt_file, log_file):
    with open(prompt_file, 'r') as f:
        prompt = f.read()
    result = f"Result for prompt from {prompt_file}"
    with open(log_file, 'w') as f:
        f.write(result)
    print(f"Task with {prompt_file} done, result saved in {log_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt_file', required=True)
    parser.add_argument('--log_file', required=True)
    args = parser.parse_args()
    run_task(args.prompt_file, args.log_file)
