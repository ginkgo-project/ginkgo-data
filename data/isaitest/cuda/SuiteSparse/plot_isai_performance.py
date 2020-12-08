from os import listdir, getcwd
from os.path import join, isdir
import json
import matplotlib.pyplot as plt
from numpy import add

transformed_results = {}

cwd = getcwd()
dirs = listdir(cwd)
for dir in dirs:
    if not isdir(dir):
        break
    for matrix in listdir(join(cwd, dir)):
        if not isdir(join(cwd, dir)):
            break
        entry = {}
        with open(join(cwd, dir, matrix)) as f:
            data = json.load(f)
            entry["idr"] = data[0]["solver"]["idr"]
            entry["idr-parilu-isai"] = data[0]["solver"]["idr-parilu-isai"]
            entry["idr-general-isai"] = data[0]["solver"]["idr-general-isai"]
            entry["bicgstab"] = data[0]["solver"]["bicgstab"]
            entry["bicgstab-parilu-isai"] = data[0]["solver"]["bicgstab-parilu-isai"]
            entry["bicgstab-general-isai"] = data[0]["solver"]["bicgstab-general-isai"]
        transformed_results[matrix.split(".json")[0]] = entry

idriter = []
isaiidriter = []
iluisaiidriter = []
idrt = []
isaiidrt = []
iluisaiidrt = []
idrgen = []
isaiidrgen = []
iluisaiidrgen = []
bicgstabiter = []
isaibicgstabiter = []
iluisaibicgstabiter = []
bicgstabt = []
isaibicgstabt = []
iluisaibicgstabt = []
bicgstabgen = []
isaibicgstabgen = []
iluisaibicgstabgen = []
for matrix in transformed_results.keys():
    idriter.append(transformed_results[matrix]["idr"]["apply"]["iterations"])
    isaiidriter.append(transformed_results[matrix]["idr-general-isai"]["apply"]["iterations"])
    iluisaiidriter.append(transformed_results[matrix]["idr-parilu-isai"]["apply"]["iterations"])
    idrt.append(transformed_results[matrix]["idr"]["apply"]["time"] / 1e9)
    isaiidrt.append(transformed_results[matrix]["idr-general-isai"]["apply"]["time"] / 1e9)
    iluisaiidrt.append(transformed_results[matrix]["idr-parilu-isai"]["apply"]["time"] / 1e9)
    idrgen.append(transformed_results[matrix]["idr"]["generate"]["time"] / 1e9)
    isaiidrgen.append(transformed_results[matrix]["idr-general-isai"]["generate"]["time"] / 1e9)
    iluisaiidrgen.append(transformed_results[matrix]["idr-parilu-isai"]["generate"]["time"] / 1e9)
    bicgstabiter.append(transformed_results[matrix]["bicgstab"]["apply"]["iterations"])
    isaibicgstabiter.append(transformed_results[matrix]["bicgstab-general-isai"]["apply"]["iterations"])
    iluisaibicgstabiter.append(transformed_results[matrix]["bicgstab-parilu-isai"]["apply"]["iterations"])
    bicgstabt.append(transformed_results[matrix]["bicgstab"]["apply"]["time"] / 1e9)
    isaibicgstabt.append(transformed_results[matrix]["bicgstab-general-isai"]["apply"]["time"] / 1e9)
    iluisaibicgstabt.append(transformed_results[matrix]["bicgstab-parilu-isai"]["apply"]["time"] / 1e9)
    bicgstabgen.append(transformed_results[matrix]["bicgstab"]["generate"]["time"] / 1e9)
    isaibicgstabgen.append(transformed_results[matrix]["bicgstab-general-isai"]["generate"]["time"] / 1e9)
    iluisaibicgstabgen.append(transformed_results[matrix]["bicgstab-parilu-isai"]["generate"]["time"] / 1e9)

plt.plot(range(len(transformed_results)), idriter, "x", range(len(transformed_results)), isaiidriter, "o", range(len(transformed_results)), iluisaiidriter, "+")
plt.yscale("log")
plt.xticks(range(len(transformed_results)), transformed_results.keys(), rotation="vertical")
plt.ylabel("iterations")
plt.title("IDR iterations")
plt.legend(["IDR", "general-ISAI-IDR", "ParILU-ISAI-IDR"])
plt.show()

plt.plot(range(len(transformed_results)), idrt, "x", range(len(transformed_results)), isaiidrt, "o", range(len(transformed_results)), iluisaiidrt, "+")
plt.yscale("log")
plt.xticks(range(len(transformed_results)), transformed_results.keys(), rotation="vertical")
plt.ylabel("time in s")
plt.title("IDR apply time")
plt.legend(["IDR", "general-ISAI-IDR", "ParILU-ISAI-IDR"])
plt.show()

plt.plot(range(len(transformed_results)), idrgen, "x", range(len(transformed_results)), isaiidrgen, "o", range(len(transformed_results)), iluisaiidrgen, "+")
plt.yscale("log")
plt.xticks(range(len(transformed_results)), transformed_results.keys(), rotation="vertical")
plt.ylabel("time in s")
plt.title("IDR generate time")
plt.legend(["IDR", "general-ISAI-IDR", "ParILU-ISAI-IDR"])
plt.show()

plt.plot(range(len(transformed_results)), add(idrgen, idrt), "x", range(len(transformed_results)), add(isaiidrgen, isaiidrt), "o", range(len(transformed_results)), add(iluisaiidrgen, iluisaiidrt), "+")
plt.yscale("log")
plt.xticks(range(len(transformed_results)), transformed_results.keys(), rotation="vertical")
plt.ylabel("time in s")
plt.title("IDR total time")
plt.legend(["IDR", "general-ISAI-IDR", "ParILU-ISAI-IDR"])
plt.show()

plt.plot(range(len(transformed_results)), bicgstabiter, "x", range(len(transformed_results)), isaibicgstabiter, "o", range(len(transformed_results)), iluisaibicgstabiter, "+")
plt.yscale("log")
plt.xticks(range(len(transformed_results)), transformed_results.keys(), rotation="vertical")
plt.ylabel("iterations")
plt.title("bicgstab iterations")
plt.legend(["bicgstab", "general-ISAI-bicgstab", "ParILU-ISAI-bicgstab"])
plt.show()

plt.plot(range(len(transformed_results)), bicgstabt, "x", range(len(transformed_results)), isaibicgstabt, "o", range(len(transformed_results)), iluisaibicgstabt, "+")
plt.yscale("log")
plt.xticks(range(len(transformed_results)), transformed_results.keys(), rotation="vertical")
plt.ylabel("time in s")
plt.title("bicgstab apply time")
plt.legend(["bicgstab", "general-ISAI-bicgstab", "ParILU-ISAI-bicgstab"])
plt.show()

plt.plot(range(len(transformed_results)), bicgstabgen, "x", range(len(transformed_results)), isaibicgstabgen, "o", range(len(transformed_results)), iluisaibicgstabgen, "+")
plt.yscale("log")
plt.xticks(range(len(transformed_results)), transformed_results.keys(), rotation="vertical")
plt.ylabel("time in s")
plt.title("bicgstab generate time")
plt.legend(["bicgstab", "general-ISAI-bicgstab", "ParILU-ISAI-bicgstab"])
plt.show()

plt.plot(range(len(transformed_results)), add(bicgstabgen, bicgstabt), "x", range(len(transformed_results)), add(isaibicgstabgen, isaibicgstabt), "o", range(len(transformed_results)), add(iluisaibicgstabgen, iluisaibicgstabt), "+")
plt.yscale("log")
plt.xticks(range(len(transformed_results)), transformed_results.keys(), rotation="vertical")
plt.ylabel("time in s")
plt.title("bicgstab total time")
plt.legend(["bicgstab", "general-ISAI-bicgstab", "ParILU-ISAI-bicgstab"])
plt.show()
