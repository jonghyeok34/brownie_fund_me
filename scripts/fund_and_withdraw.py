from brownie import FundMe
from web3 import Web3

from scripts.helpful_scripts import get_account

# DECIMALS = 8
# GAS_LIMIT_WEI = 1 * (10 ** DECIMALS)
GAS_LIMIT_WEI = 6721975

def fund():
    print(list(FundMe))
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    price = fund_me.getPrice()
    
    print(f'price: {price}')
    print(f'THe current entry fee is {entrance_fee}')
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee, "gas_limit": GAS_LIMIT_WEI, "allow_revert": True})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()