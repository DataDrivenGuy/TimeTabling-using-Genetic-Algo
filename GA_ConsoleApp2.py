import codecs
import pathlib
import os
import sys
import tempfile
import time
import traceback

from model.Configuration import Configuration
from algorithm.GeneticAlgorithm import GeneticAlgorithm
from HtmlOutput import HtmlOutput
import joblib

def main(file_name):
    start_time = int(round(time.time() * 1000))

    configuration = Configuration()
    target_file = str(pathlib.Path().absolute()) + file_name
    configuration.parseFile(target_file)

    alg = GeneticAlgorithm(configuration)
    # alg = GaQpso(configuration)
    print("GaSchedule Version 1.2.6 . Making a Class Schedule Using", alg, ".\n")
    print("Copyright (C) 2022 - 2024 Miller Cy Chan.\n")
    alg.run()
    html_result = HtmlOutput.getResult(alg.result)

    joblib.dump(alg.result, "/data/students/leo/mex/GASchedule.py/output/GA_Schedule3.pkl")
    temp_file_path = "/data/students/leo/mex/GASchedule.py/output/GA_Schedule3.html"
    print(temp_file_path)
    writer = codecs.open(temp_file_path, "w", "utf-8")
    writer.write(html_result)
    print("file written")
    writer.close()

    seconds = (int(round(time.time() * 1000)) - start_time) / 1000.0
    print("\nCompleted in {} secs.\n".format(seconds))
    # webbrowser.open(temp_file_path)


if __name__ == "__main__":
    file_name = "/GaSchedule.json"
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

    try:
        main(file_name)
    except:
        traceback.print_exc()
