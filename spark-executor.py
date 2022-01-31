import os
import subprocess
import sys


try:
    hostname = os.environ['HOSTNAME']
    start = "_".join(hostname.split("-")[0:2]).upper()
    end = "7077_TCP_ADDR"
    port = 7077
    print(start)
    # exit()

    for key, value in os.environ.items():
        if key.startswith(start) and key.endswith(end):
            spark_ep = f"{value}:{port}"
            print(f"spark_endpoint ----> {spark_ep}")

    spark_command = sys.argv[1].split(" ")
    spark_command.insert(1, "--master")
    spark_command.insert(2, f"spark://{spark_ep}")
    spark_command.append(sys.argv[2])
    print(f"####### COMMAND: {spark_command}")
    
    process = subprocess.run(spark_command)
except Exception as err:
    print(err)
