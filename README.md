.env 
```config
export PRIVATE_KEY=<비밀번호>
export WEB3_INFURA_PROJECT_ID=<infura project id>
export ETHERSCAN_TOKEN=<etherscan token>
```


- compile solidity
```
brownie compile
```
- a

```
brownie run scripts/deploy
brownie run scripts/deploy --network rinkeby
```
[chain link mix](https://github.com/smartcontractkit/chainlink-mix)


- ganache > setting > server
```
hostname : 127.0.0.1 - loopback psuedo interface
port number : 8545

```

```
brownie networks list
# add ganache-local
brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=5777
# ganache-local 실행
brownie run scripts/deploy.py --network ganache-local

```

```
brownie test
```