from openai import OpenAI

def outputFromAI(tempFile, userInput):
    client = OpenAI(api_key="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")

    userInput = "Perplexity is seeking experienced AI Research Engineers and Scientists to continue to improve our in house Online LLMs, the Sonar models. Your job is to work with team and create a robust and effective training framework (on top of Megatron/PyTorch), especially for post training LLMs."

    jobDescription = "job description: " + userInput

    response = client.responses.create(
        model="gpt-4o",
        input=[
            {
                "role": "developer",
                "content": "Please optimize this section of my resume to fit the job description inputted by the user. Keep it in the exact same format. if you add a bullet point, please make sure it is in the \resumeItem format. The resume is also inputted. Do not make up things that they have not done. Use the resume content to figure out what they have done. Simply optimize based on the rules that most major ATS systems follow. I really want this job."
            },
            {
                "role": "user",
                "content": tempFile + " " + jobDescription
            }
        ]
    )


    #saves the string output as a file
    with open(tempFile, 'w') as file:
        file.write(response.output_text)
    print(response.output_text) 

    tempFile.close()
    # return the file name of the new file

    return tempFile