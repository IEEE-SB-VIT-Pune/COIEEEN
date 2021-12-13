# COIEEEN :coin:
#### Part of IEEE's workshop - Build your own Blockchain from Cryptocurrency to Smart Contracts

A cryptocurrency is a digital asset designed to work as a medium of exchange using cryptography to secure the transactions and to control the creation of additional units of the currency.
- This project implements a simple blockchain which is developed and decentralised to create a cryptocurrency “COIEEEN”
- The principle of cryptocurrency is that one should be able to exchange cryptocurrencies through transactions that are secured, added to new blocks and mined. Transactions form the key element of COIEEEN.
- SHA256 hashing is used and proof of work is implemented to mine blocks.
- The next pillar is the consensus algorithm to make sure that each node in the decentralised network has the same chain. 


### :round_pushpin: The main functionalities of this project are:

**Add transaction:** It takes the sender’s and receiver’s details along with the transaction amount to make a list of transactions. Multiple transactions can be added to the list.

**Open transactions:** All transactions added to the list are displayed here.

**Mine Block:** A new block is created and the list of transactions are added to it. Then, the block is added to the blockchain by performing the proof of work to find a proof(nonce) that satisfies the hash requirement. The mining difficulty here can be changed by the developer. Currently it is set to the hash having at least 4 preceding zeros.

**Get chain:** Displays the current blockchain.

**Connect node:** It takes the url address of a node to add it to the blockchain network.

**Replace chain:** This implements consensus by replacing any chain in the network that is shorter than the longest chain among all the nodes in the network.

**Validate:** It ensures the validity of blockchain by checking whether the previous hash of a block matches the hash of the previous block and also if all the hashes satisfy the hash requirement.

**View network:** Displays all the nodes present in the blockchain network.




## :round_pushpin: Commands to run this project:

### Windows :desktop_computer:

1. Creating the environment 
    ```
    mkdir IEEE-Blockchain 
    cd IEEE-Blockchain 
    python3 -m venv venv
    ```

2. Activate the environment 
   ```
   venv\Scripts\activate
   ```

3. Install Flask 
   ```
   pip install Flask
   ```

4. Clone the repo
   ```
   git clone https://github.com/IEEE-SB-VIT-Pune/COIEEEN.git
   ```

5. Navigate to the project and run
    ```
    cd COIEEEN
    flask run
    ```

6. To run on different servers open a new window:
   ```
   flask run -p <PORT_NUMBER>
   ```

Note: If any packages are missing:
   ```
   pip install <package name>
   ``` 

  
### MacOS / Linux :desktop_computer:

1. Creating the environment 
    ```
    mkdir IEEE-Blockchain 
    cd IEEE-Blockchain 
    python3 -m venv venv
    ``` 

2. Activate the environment 
   ```
   . venv/bin/activate
   ``` 

3. Install Flask 
   ```
   pip install Flask
   ```

4. Clone the repo
   ```
   git clone https://github.com/IEEE-SB-VIT-Pune/COIEEEN.git
   ```

5. Navigate to the project and run
    ```
    cd COIEEEN
    flask run
    ```

6. To run on different servers, open a new terminal tab:
   ```
   flask run -p <PORT_NUMBER>
   ```


Note: If any packages are missing:
   ```
   pip install <package name>
   ```



