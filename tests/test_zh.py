import subprocess
import os

from output_collector import OutputCollector


def run_life_with_config(config_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    life_script_path = os.path.join(script_dir, '..', 'life.py')
    output_collector = OutputCollector()
    try:

        result = subprocess.run(
            ['python', life_script_path, config_path],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        output_collector.write(result.stdout)
        output = output_collector.get_contents()

        print("----- Output Start -----")
        print(output)
        print("----- Output End -----")

        if "继续前进" in output:
            print("Test passed")
        else:
            print("Test failed")
    except Exception as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    test_config_path = 'config_zh.json'
    run_life_with_config(test_config_path)
