import file_encrypt_decrypt as file_en_de
from sys import argv


# check correct number of command line arguments
if len(argv) < 2:
    print("""Usage Info:
            # ./app [OPTION] input_file [output_file]
            # Example:
            # ./app -d in_filename out_filename
            # ./app -e in_filename out_filename
            # defaults to encryption if option not passed
          """)
    exit(1)
    
# exclude the name of the program from the command line arguments
arg_vec = argv[1:]


if arg_vec[0][0] == "-":
    # if option passed
    in_filename = arg_vec[1]
    out_filename = arg_vec[2] if len(arg_vec) > 2 else in_filename
    if arg_vec[0][1] == "d":
    # decrypt
        file_en_de.decrypt(in_filename, out_filename)
    elif arg_vec[0][1] == "e":
    #encrypt
        file_en_de.encrypt(in_filename, out_filename)
else:
    # default to encrypty
    in_filename = arg_vec[0]
    out_filename = arg_vec[1] if len(arg_vec) > 1 else in_filename
    file_en_de.encrypt(in_filename, out_filename)

