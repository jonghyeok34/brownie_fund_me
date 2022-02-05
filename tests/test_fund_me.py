import pytest
from scripts.fund_and_withdraw import GAS_LIMIT_WEI
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from scripts.deploy import deploy_fund_me
from scripts.fund_and_withdraw import GAS_LIMIT_WEI
from brownie import network

def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    tx= fund_me.fund({"from": account, "value": entrance_fee, "gas_limit": GAS_LIMIT_WEI, "allow_revert": True})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    tx2 = fund_me.withdraw({"from": account, "gas_limit": GAS_LIMIT_WEI})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0
    
def test_only_owner_can_withdraw():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
