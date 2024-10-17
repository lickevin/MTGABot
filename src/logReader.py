import time
import json

log_path = r'C:\Users\Kevin\AppData\LocalLow\Wizards Of The Coast\MTGA\Player.log'

with open(log_path, 'r', encoding='utf-8') as f:
    f.seek(0, 2)  # Move to the end of the file

    while True:
        line = f.readline()

        if not line:
            # If no new line, wait a bit before checking again
            time.sleep(0.5)
            continue

        # Try to parse the JSON line if it's valid
        try:
            # First, check if the line looks like JSON
            if line.strip():  # Skip empty lines
                data = json.loads(line)

                # Ensure that the parsed data is a dictionary (JSON object)
                if isinstance(data, dict):
                    if data.get("greToClientEvent"):
                        print("hey")  # TODO implement
                else:
                    print(f"Skipping non-dict data: {data} with type {type(data)}")

        except json.JSONDecodeError:
            # If the line isn't a valid JSON, log the issue and continue
            print(f"Skipping invalid JSON line: {line.strip()}")
            continue