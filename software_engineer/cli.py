import argparse, json
from .workflow import run
def main():
    parser=argparse.ArgumentParser(description='Draft a human-reviewed software task plan')
    parser.add_argument('request')
    args=parser.parse_args()
    print(json.dumps(run(args.request),indent=2))
if __name__ == '__main__': main()
