<h1> File Encryption and Decryption </h1>

This main.py file can Encrypt or Decrypt a file.

## Usage

```sh
 python ./main [OPTION] input_file [output_file]
 ```
There are two(2) possible options:
	-e	Encrypts the input_file
	-d	Decrypts the output_file
 Example:

``python ./main.py -d in_filename out_filename``

``python ./main.py -e in_filename out_filename``

 
 the program defaults to encryption if an option is not passed


the program overwrites the input_file if an output_file is not passed
 
 ### You can clone this repo and test with the below command:
 
 #### Encrypt
 ```sh
 python ./main.py -e text.txt
 ```
 With output file:
 ```sh
 python ./main.py -e text.txt out.txt
 ```
 #### Decrypt
 ```sh
 python ./main.py -d text.txt
 ```
 With output file:
 ```sh
 python ./main.py -e text.txt out.txt
 ```
