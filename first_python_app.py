def read_file(filename:str)->str:
    """Opens the given file in read mode and returns the file content

    Args:
        filename (str): Name/path of the file to read

    Returns:
        str: Content of the file
    """
    try:
        with open(filename,"r") as fd:
            return fd.read()
    except FileNotFoundError as e:
        print("File doesn't exist",e)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)

        
def write_file(filename:str,data:str,mode:str)->None:
    """Writes to the file (filename) the given data where file is opened in given mode(w-write,a-append)

    Args:
        filename (str): Name/Path of the file to write data in
        data (str): Content of the file
        mode (str): Mode to open file in. Example 'w' - write mode, 'a' - read mode
    Returns:
        None
    """
    with open(filename,mode) as fw:
        fw.write(data+"\n")


if __name__ == '__main__':
    data = read_file("a.txt")
    print(data)
    write_file(r"output.txt",str(data),"a")
    # data = read_file(r"D:\Training\Python\something.txt")
    # print(data)
    # write_file(r"D:\Training\Python\output.txt",str(data),"a")