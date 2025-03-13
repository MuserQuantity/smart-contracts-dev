import os
import time
import sys

if len(sys.argv) != 2:
    print("Usage: python output.py <contract_name>")
    sys.exit(1)

contract_name = sys.argv[1]
name = "truffle-" + str(time.time())

current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = current_dir.replace("\\", "/")
print("Current directory: ", current_dir)

contracts_path = os.path.abspath(os.path.join(current_dir, "..", "remixd", "contracts"))
contracts_path = contracts_path.replace("\\", "/")
print("Contracts directory: ", contracts_path)

command = f'''docker run -w /etc/truffle/ -v {current_dir}:/etc/truffle/ -v {contracts_path}:/etc/truffle/contracts --name {name} mytruffle:latest /bin/bash -c "npm install && truffle run stdjsonin {contract_name}"'''
print("Executing command: ", command)
os.system(command)

# Clean up Docker container
cleanup_command = "docker container rm " + name
os.system(cleanup_command) 

# Generate abigen command
abigen_command = f"abigen --abi {current_dir}/abigenBindings/abi/{contract_name}.abi --pkg contracts --type {contract_name} --bin {current_dir}/abigenBindings/bin/{contract_name}.bin --out {current_dir}/{contract_name}.go"
print("abigen command: ", abigen_command)

