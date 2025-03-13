# 达道合约

## 编译

truffle环境docker容器配置文件

### 第一步 编译image
1. 在文件夹下执行`sudo docker build -t truffle:latest .`
2. 网络环境复杂，请使用美国的服务器进行访问。

### 第二步 运行
1. 合约放在`/etc/truffle/contracts`文件夹下，即可进行编译(对应`contracts`)
2. 合约编译后会输出到`/etc/truffle/build/contracts`文件夹下(对应`./build/contracts`)
3. 把上述文件映射到本地即可进行合约编译，执行`python compile.py`(可将`truffle run stdjsonin DaDAONFT`中的`DaDAONFT`修改为要输出的合约)