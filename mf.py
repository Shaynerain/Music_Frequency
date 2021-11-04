import os
import sys
import subprocess

#导出频率
OUT_AR = 16164
#导出通道数，没有设置将会保持一致
OUT_AC = 2

def call_ffmpeg(input, output):
    parm = "ffmpeg -i " +input + " -ac "+str(OUT_AC)+" -ar "+str(OUT_AR)+" " + output  
    subprocess.run(parm)
    pass

def get_files(input_path):
    _all_path = os.listdir(input_path)
    _all_file = []
    for path in _all_path:
        file = os.path.join(input_path, path)
        if(os.path.isfile(file)):
            if file.endswith('.wav'):
                _all_file.append(file)
            pass
        elif os.path.isdir(file):
            _files = get_files(file)
            for _file in _files:
                _all_file.append(_file)
    return _all_file

if __name__ == "__main__":
    param = []
    if len(sys.argv) == 3:
        param.append(sys.argv[1])
        param.append(sys.argv[2])
    else:
        if not os.path.exists("./output"):
            os.makedirs("./output")
        param = ["./", "./output"]
    files = get_files(param[0])
    for file in files:
        out_name = 'w' + os.path.basename(file)
        out_name = os.path.join(param[1], out_name)
        call_ffmpeg(file, out_name)
    pass

