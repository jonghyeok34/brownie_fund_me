.env 
```config
export PRIVATE_KEY=<비밀번호>
export WEB3_INFURA_PROJECT_ID=<infura project id>
export ETHERSCAN_TOKEN=<etherscan token>
```

- a

```
brownie run scripts/deploy
brownie run scripts/deploy --network rinkeby
```