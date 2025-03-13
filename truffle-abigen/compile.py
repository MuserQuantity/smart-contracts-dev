import os,time

name ="truffle-"+str(time.time())
current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = current_dir.replace("\\", "/")
print("Current directory: ", current_dir)
contracts_path = os.path.abspath(os.path.join(current_dir, "..", "remixd", "contracts"))
contracts_path = contracts_path.replace("\\", "/")
print("Contracts directory: ", contracts_path)

command = f'''docker run -w /etc/truffle/ -v {current_dir}:/etc/truffle/ -v {contracts_path}:/etc/truffle/contracts --name {name} mytruffle:latest /bin/bash -c "npm install && truffle compile && truffle run abigen"'''
print("Executing command: ", command)
os.system(command)

# Clean up Docker container
command = "docker container rm "+name
os.system(command)