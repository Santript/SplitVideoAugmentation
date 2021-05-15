import json

with open("static/json/step_1.json", "r") as step1_readfile:
    step1Data = json.load(step1_readfile)
    step1_readfile.close()

with open("static/json/step_2.json", "r") as step2_readfile:
    step2Data = json.load(step2_readfile)
    step2_readfile.close()

with open("static/json/step_3.json", "r") as step3_readfile:
    step3Data = json.load(step3_readfile)
    step3_readfile.close()

with open("static/json/video2Frames.json", "r") as v2f_readfile:
    v2fData = json.load(v2f_readfile)
    v2f_readfile.close()

step1Data["step_1"]["vid_file"] = ""
step1Data["step_1"]["subject_matter"] = ""
step1Data["step_1"]["numDog"] = 0
step1Data["step_1"]["numCar"] = 0
step1Data["step_1"]["numPlane"] = 0

for keys in step2Data["step_2"]:
    step2Data["step_2"][keys] = False

step3Data["normalize"] = False
step3Data["rgb"] = False
step3Data["bgr"] = False
step3Data["resize"] = ""

for keys in v2fData:
    v2fData[keys] = 0

with open("static/json/step_1.json", "w") as step1_writefile:
    json.dump(step1Data, step1_writefile, indent=2)
    step1_writefile.close()

with open("static/json/step_2.json", "w") as step2_writefile:
    json.dump(step2Data, step2_writefile, indent=2)
    step2_writefile.close()

with open("static/json/step_3.json", "w") as step3_writefile:
    json.dump(step3Data, step3_writefile, indent=2)
    step3_writefile.close()

with open("static/json/video2Frames.json", "w") as v2f_writefile:
    json.dump(v2fData, v2f_writefile, indent=2)
    v2f_writefile.close()

