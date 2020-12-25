from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Main Page'
@app.route('/about')
def about():
    str = '<h1>ABOUT PAGE</h1>'
    return str

@app.route('/vivaldi', methods=['GET'])
def vivaldi():
    if request.method == "GET":
        with open("myjsonReadtoIos.json", "r") as read_file:
            data = json.load(read_file)
        print(data)
        string1 = data["TVmotor"]
        string2 = data["Table1Motor"]
        string3 = data["Table2Motor"]
        string4 = data["Table3Motor"]
        string5 = data["KahveMotor"]
        string6 = data["Led1-Red"]
        string7 = data["Led1-Green"]
        string8 = data["Led1-Blue"]
        string9 = data["Led2-Red"]
        string10 = data["Led2-Green"]
        string11 = data["Led2-Blue"]
        string12 = data["Led3-Red"]
        string13 = data["Led3-Green"]
        string14 = data["Led3-Blue"]
        print(string1)
        #return jsonify({'motors' : f'{string1};{string2};{string3};{string4};{string5}'})
        return jsonify({"TVmotor" : f"{string1}", "Table1Motor" : f"{string2}", "Table2Motor" : f"{string3}", "Table3Motor" : f"{string4}", "KahveMotor" : f"{string5}", "Led1-Red" : f"{string6}", "Led1-Green" : f"{string7}", "Led1-Blue" : f"{string8}", "Led2-Red" : f"{string9}", "Led2-Green" : f"{string10}", "Led2-Blue" : f"{string11}", "Led3-Red" : f"{string12}", "Led3-Green" : f"{string13}", "Led3-Blue" : f"{string14}"})
    else:
        return jsonify("Problem with GET method.")

@app.route('/vivaldi/cmds', methods=['POST'])
def cmds():
    if request.method == "POST":
        correctlydone = True
        data = request.get_json()
        #print(data)
        command = data['cmd']
        with open('myjsonWrite.json', 'r') as read_file:
            dataread = json.load(read_file)
        print(dataread)
        print(command)
        if command=="tvmotor;on":
            dataread["TVmotor"] = 1
            writeInfo("TVmotor")
            print("yep")
        elif command=="tvmotor;Off":
            dataread["TVmotor"] = 0
        elif command=="table1motor;on":
            dataread["Table1Motor"]=1
        elif command=="table1motor;off":
            dataread["Table1Motor"]=0
        elif command=="table2motor;on":
            dataread["Table2Motor"]=1
        elif command=="table2motor;off":
            dataread["Table2Motor"]=0
        elif command=="table3motor;on":
            dataread["Table3Motor"]=1
        elif command=="table3motor;off":
            dataread["Table3Motor"]=0
        elif command=="kahvemotor;on":
            dataread["KahveMotor"]=1
        elif command=="kahvemotor;off":
            dataread["KahveMotor"]=0
        else:
            splitedcmd = command.split(";")
            if splitedcmd[0]=="led1-red":
                dataread["Led1-Red"] = splited[1]
            elif splitedcmd[0]=="led1-green":
                dataread["Led1-Green"] = splited[1]
            elif splitedcmd[0]=="led1-blue":
                dataread["Led1-Blue"] = splited[1]
            elif splitedcmd[0]=="led2-red":
                dataread["Led2-Red"] = splited[1]
            elif splitedcmd[0]=="led2-green":
                dataread["Led2-Green"] = splited[1]
            elif splitedcmd[0]=="led2-blue":
                dataread["Led2-Blue"] = splited[1]    
            elif splitedcmd[0]=="led3-red":
                dataread["Led3-Red"] = splited[1]
            elif splitedcmd[0]=="led3-green":
                dataread["Led3-Green"] = splited[1]
            elif splitedcmd[0]=="led3-blue":
                dataread["Led3-Blue"] = splited[1] 
            else:
                print("ERROR writing")
                correctlydone = False #may be useful when we check error cases
        with open('myjsonWrite.json', 'w') as write_file:
            json.dump(dataread, write_file)
        return 'OK'
def writeInfo(processName): #Changes read value to in process
    with open('myjsonReadtoIos.json', 'r') as read_file:
            dataread = json.load(read_file)
    print(dataread[processName], " value is in process") 
    dataread[processName] = "Inprocess"
    with open('myjsonReadtoIos.json', 'w') as write_file:
        json.dump(dataread, write_file)
if __name__ == '__main__':
    app.run(debug=True)
