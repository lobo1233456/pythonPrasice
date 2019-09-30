import json
import hashlib


# Block Object
class Block:
    def __init__(self, index, timestamp, data, previousHash=' '):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def calculateHash(self):
        '''
        计算区块哈希值
        :return:
        '''
        # 将区块信息拼接然后生成sha256的hash值
        raw_str = self.previous_hash + str(self.timestamp) + json.dumps(self.data, ensure_ascii=False)
        sha256 = hashlib.sha256()
        sha256.update(raw_str.encode('utf-8'))
        hash = sha256.hexdigest()
        return hash
    # def calculate_hash(self):
    #     '''
    #     计算区块哈希值
    #     :return:
    #     '''
    #     # 将区块信息拼接然后生成sha256的hash值
    #     raw_str = self.previous_hash + str(self.timestamp) + json.dumps(self.data, ensure_ascii=False)
    #     sha256 = hashlib.sha256()
    #     sha256.update(raw_str.encode('utf-8'))
    #     hash = sha256.hexdigest()
    #     return hash
    def printBlock(self):
        print ("Block #" + str(self.index))
        print ("Account: " + str(self.data["account"]))
        print ("Amount: " + str(self.data["amount"]))
        print ("Block Hash: " + str(self.hash))
        print ("Block Previous Hash: " + str(self.previousHash))
        print ("---------------")


# Block Chain Object
class BlockChain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        return Block(0, "10/01/2017", "Genesis Block", "0")

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)

    def isChainValid(self):
        for i in range (1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i-1]
            # checks whether data has been tampered with
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.previousHash != previousBlock.hash:
                return False
        return True

    def printBlockChain(self):
        for i in range(1, len(self.chain)):
            self.chain[i].printBlock()


def main1():
    annaCoin = BlockChain()
    annaCoin.addBlock(Block(1, "10/10/2017", {"account": "Anna","amount": 25,"action": "buy"}))
    annaCoin.addBlock(Block(2, "11/01/2017", {"account": "Joe","amount": 10,"action": "buy"}))
    annaCoin.addBlock(Block(3, "12/01/2017", {"account": "Katie","amount": 20,"action": "buy"}))
    annaCoin.addBlock(Block(4, "12/07/2017", {"account": "Ethan","amount": 4,"action": "buy"}))
    annaCoin.printBlockChain()
    # no tampering in our block chain yet so should be true here
    print( "Chain valid? " + str(annaCoin.isChainValid()))
    # now lets tamper the block chain and see what happens
    annaCoin.chain[1].data = {"account": "Anna","amount": 100,"action": "buy"}
    print ("Chain valid? " + str(annaCoin.isChainValid()))

# Only run the main() function, if this is the root script running.
# This allows importing this script file to use its functions inside other scripts.
if __name__ == '__main__':
    main1()