
# Blockchain

**🎯 Implement your own blockchain algorithm.**

## Step 1

Write a function that generates random transactions in the format `(name1, name2, amount)`.

We want to save these transactions *forgery-proof*, so that they are as difficult to manipulate as possible afterwards.

## Step 2

Define a data type *"Block "* that contains the following:

* The hash of a previous block
* Some transactions
* A checksum (any number or string)

## Step 3

Write a function that calculates a hash from all properties of a block. To do this, represent the entire block as a string. Use the hash function `sha256`:

    import hashlib

    h = hashlib.sha256()
    h.update(text.encode())
    print(h.hexdigest())

## Step 4

Create the blockchain as an empty list.

Create the first block, the "Genesis block". Use 'genesis' as previous hash. Place some random transactions in the block.

Find a checksum so that the *sha256-hexdigest* ends with four zeros (`0000`). You may need to try many checksums.

Add the finished block to the blockchain.

## Step 5

Create the second block:

* The hash is the `hexdigest` of the previous block
* Add more transactions.
* Again find a checksum that generates a `hexdigest` with four zeros at the end.
* Add the finished block to the blockchain.

## Step 6

Generate more blocks.

## Questions

* What happens if the number of necessary zeros in the hex digest is set to 2 or 6?
* What happens if someone changes a transaction in the Genesis block?
* What makes the blockchain forgery-proof?
* How could a blockchain still be forged?
* Why is finding the checksum also called *"proof of work"*?
* Why are several computers involved in a blockchain?
* What is a *"consensus algorithm"?

*Translated with [www.DeepL.com](www.DeepL.com/Translator)*
