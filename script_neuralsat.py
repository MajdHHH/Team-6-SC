import csv
import os
import time

onnx_folder = "/root/neuralsat-develop/onnx/"
vnnlib_folder = "/root/neuralsat-develop/vnnlib/"
output_file = "output.txt"

with open(output_file, "w") as output:
    output.write("Instance,Result\n")

    with open("instances.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            onnx_filename = os.path.join(onnx_folder, row[0].lstrip('onnx/'))
            vnnlib_filename = os.path.join(vnnlib_folder, row[1].lstrip('vnnlib/'))
            command = (
                f"python3 main.py --net {onnx_filename} --spec {vnnlib_filename} --timeout 480 --device cpu"
            )
            time.sleep(6)

            result = os.popen(command).read()

            output.write(f"{row[0]},{result}\n")

print(f"Results saved in {output_file}")

