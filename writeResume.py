def read_and_write_file(inputFile, outputFile):
    # try:
        # inputFile = open(input_path, "r")
        # outputFile = open(output_path, "a")

    
        for line in inputFile:
            if line.strip() == "%startExperience":
                break
            else:
                outputFile.write(line)