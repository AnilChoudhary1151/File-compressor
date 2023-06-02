This file compressor was created by Anil Choudhary and uses the Huffman algorithm for lossless data compression.

The main file is app_main.py, which contains the code for the GUI. Upon clicking the compress button, the file is compressed and a folder with the name (filename+"_compress") is generated, containing two files: data.bin (a binary file containing the compressed data) and .metadata.txt (a text file storing the Huffman binary tree). Similarly, clicking the decompress button takes a compressed folder and generates the original file in the same location with the name (filename+"_decompress.txt"). For further reading on Huffman coding, you can visit "https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/". 

The code for file compression can be found in huffman.py.
