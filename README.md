## SHAKESPEARE RESEARCH
### Technical exercise
For an exhaustive research on Shakespeare's literary works, we need to know how many times the author uses every word in three of his masterpieces:
- King Lear: https://storage.cloud.google.com/apache-beam-samples/shakespeare/kinglear.txt 
- Othello: https://storage.cloud.google.com/apache-beam-samples/shakespeare/othello.txt 
- Romeo and Juliet: https://storage.cloud.google.com/apache-beam-samples/shakespeare/romeoandjuliet.txt

The expected output is a single file.

## Exercise Explanation
The project has been designed to be modular and at the same time have reusable code. For this, I separated the app into an main, logger modules and those required for the operation of the app. With this system, we could integrate an RESTapi like flask or FastAPI
and send the data to a front-end.

This tool works with a dotenv variables, src folder got the folder to be processed and the output folder, where the final data will be put in.
Also the tmp folder got the temporary data and log records.

The project has been carried out using technologies such as poetry, which has allowed the creation of a virtual environment and to block the dependencies of the respective versions used. The requirements file is also included for those who do not use this version manager.

The projects has been tested and works fine, if you want to change paths or file names, you must change the .env variables.

### ENV VARIABLES
```
- TXT_SOURCE_FOLDER: Folder that contains txt files (Example: "../src/txt_files/*.txt") *.txt is necessary for get all the files.
- LOGGING_FILE: Where the record and its name will go (Example: "./tmp/app.log")
- OUTPUT_SOURCE: Output folder where the data will write (Example: "../src/output/data.json")
- TMP_MERGED: temporal folder and merged file name (Example: "./tmp/merged_files.txt")
```

### Disadvantages encountered
The first project proposed was a version made with Flask as an api, where it would receive data from the url and return the data. The problem resided in the host since it was necessary a login which I didn't have to download the necessary txt files.

The easiest way was to merge all the files into one and then output the result in a JSON file, a standard for data processing and data sending.