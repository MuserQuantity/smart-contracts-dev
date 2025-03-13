# smart-contracts-dev
Develop your smart contracts with truffle, remix and so on.

## Usage

### Remix IDE
1. Build the docker image
```bash
cd remixd
sh build.sh
```
2. Run the docker container
```bash
sh start.sh
```
3. Open the Remix IDE and input the following url
```bash
http://localhost:65520
```
4. Put your smart contracts in the `remixd/contracts` folder

### Get your smart contracts abi and bin with Truffle
1. Build the docker image
```bash
docker build -t mytruffle:latest .
```

2. Compile the smart contracts
```bash
cd truffle-abigen
python compile.py
```

3. Generate the smart contracts abi and bin
```bash
python output.py <contract_name>
```

4. Generate the smart contracts go file
```bash
# this command will get from the previous step
abigen --abi abigenBindings/abi/<contract_name>.abi --pkg contracts --type <contract_name> --bin abigenBindings/bin/<contract_name>.bin --out <contract_name>.go
```


