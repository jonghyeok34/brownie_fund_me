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
```
```