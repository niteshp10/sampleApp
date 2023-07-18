from first_python_app import read_file,write_file

if __name__=='__main__':
    data = read_file(filename="input.txt")
    print(data)
    write_file(filename="output.txt",data=str(data),mode="a")