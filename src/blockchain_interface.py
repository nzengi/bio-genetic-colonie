from web3 import Web3
import json

class BlockchainInterface:
    def __init__(self, provider_url, contract_address, contract_abi, admin_account):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)
        self.admin_account = admin_account
        self.w3.eth.default_account = admin_account

    def authorize_robot(self, robot_address):
        """Authorize a robot on the blockchain."""
        tx_hash = self.contract.functions.authorizeRobot(robot_address).transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def verify_task(self, robot_address, task_performance):
        """Verify a robot's task performance and update its reputation on the blockchain."""
        tx_hash = self.contract.functions.verifyTask(robot_address, task_performance).transact()
        self.w3.eth.wait_for_transaction_receipt(tx_hash)
