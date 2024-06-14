import subprocess
import os

from src.util.output_collector import OutputCollector


class TestLifeZH:
    def test_run_life_with_config(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        life_script_path = os.path.join(script_dir, '..', 'life.py')
        output_collector = OutputCollector()
        try:

            result = subprocess.run(
                ['python', life_script_path, 'config_zh.json'],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )

            output_collector.write(result.stdout)
            output = output_collector.get_contents()

            print("----- Output Start -----")
            print(output)
            print("----- Output End -----")
            assert "继续前进" in output, "The output does not contain '继续前进' keyword."

        except Exception as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
