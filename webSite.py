import streamlit as st
import pandas as pd
import os
from io import StringIO

from writeResume import *
from scanFile import *

from gptModel import outputFromAI

from pylatex import Document, Section, Subsection, Tabular
from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
from pylatex.utils import italic

# Choose a file to upload
def getResume():
    uploaded_file = st.file_uploader("Choose a file")

    
    temp_Txt = open("temp.txt", "w")

    fileName = ""

    # uploaded_file should be a tex file
    if uploaded_file is not None:
        fileName = uploaded_file.name
        # rawData is a string
        rawData = read_and_print_file(uploaded_file, temp_Txt)

        # myResume = theirFunction(input)
        # also, return myResume as a tex file

        return rawData, fileName



def getJobDesc():
    jobDesc = st.text_input("Job Title and Description", "")
    st.write("Current job description:")
    st.write(jobDesc)

    return jobDesc

def downloadFile(myFile, fileName, isPdf=False, isTex=False):
    if isPdf:
        texFile = doc.generate.pdf(myFile, clean_tex=False)
        st.download_button(label="Download PDF", data=texFile, file_name=fileName + "_new.pdf", mime="application/pdf")
    else:
        st.download_button(label="Download TEX", data=myFile, file_name=fileName + "_new.tex")

# Set the page title and header
st.title("Follow Suit")
st.header("A resume tailoring service")

# getting the resume
st.subheader("Step 1. Upload your resume")
getResume()
myResumeData, fileName = getResume()

# getting the job description
st.subheader("Step 2. Type in the job description")
myJobDesc = getJobDesc()

# input both resume and description into the model function
tempFile = f.open("temp.txt", "a")
newTxt = raw_latex_data_to_txt(myResumeData, tempFile) # creates .txt raw data to be input into the model

tempFile.close()
myResumeData.close()

# myModelOutput should be a .txt 
myModelOutput = outputFromAI(tempFile, myJobDesc)



# convert myModelOutput to a .tex file
newResume = open("newResume.tex", "a")
read_and_write_file(myResumeData, newResume)
read_and_write_file(myModelOutput, newResume)

# put in latexFile

# filler data (delete later)

st.subheader("Step 3. Download your tailored resume")
downloadFile(fileName, isTex=True)
downloadFile(fileName, isPdf=True)
