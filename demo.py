from lib import FastaReader
filepath = input("Enter the path to the file:")
try:
    reader=FastaReader(filepath)
except (FileNotFoundError, ValueError) as error:
    print (f"Error: {error}")
else:
    for index, seq in enumerate(reader.read(), start=1):
        print(f"Record №{index}")
        print(seq)
        print(f"Length:{len(seq)}")
        print(seq.getalphabet())
        print()