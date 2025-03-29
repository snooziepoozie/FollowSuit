def raw_latex_data_to_txt(inputFile, outputFile):
    try:
        # inputFile = open(input_path, "r")
        # outputFile = open(output_path, "a")

    
        for line in inputFile:
            if line.strip() == "%startExperience":
                print("Experience Found")
                scan_line_experiences(inputFile, outputFile)
            elif line.strip() == "%startProjects":
                print("Project Found")
                scan_line_projects(inputFile, outputFile)
            elif line.strip() == "%startSkills":
                print("Skills Found")
                scan_line_skills(inputFile, outputFile)
            # outputFile.write(line)
            

    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print(f"An error occurred: {e}")


def scan_line_experiences(inputFile, outputFile):
    for line in inputFile:
        if line.strip() == "%endExperience":
            break
        outputFile.write(line)
        # print(line + "\n")
    outputFile.write("\n")

def scan_line_projects(inputFile, outputFile):
    for line in inputFile:
        if line.strip() == "%endProjects":
            break
        outputFile.write(line)
        # print(line + "\n")
    outputFile.write("\n")

def scan_line_skills(inputFile, outputFile):
    for line in inputFile:
        if line.strip() == "%endDocument":
            break
        outputFile.write(line)
        # print(line + "\n")
    outputFile.write("\n")