//
//  ViewController.swift
//  BleDeviceTrial
//
//  Created by murat ersen unal on 18.12.2020.
//

import UIKit
import CoreBluetooth

class ViewController: UIViewController, CBCentralManagerDelegate, CBPeripheralDelegate {
    
    @IBOutlet weak var txtIn1: UITextField!
    
    @IBOutlet weak var txtIn2: UITextField!
    
    @IBOutlet weak var mylabel: UILabel!
    
    
    var centralManager: CBCentralManager!
    var myPeripheral: CBPeripheral!
    func centralManagerDidUpdateState(_ central: CBCentralManager) {
        if central.state == CBManagerState.poweredOn {
            print("BLE powered on")
            // Turned on
            central.scanForPeripherals(withServices: nil, options: nil)
        }
        else {
            print("Something wrong with BLE")
            // Not on, but can have different issues
        }
    }
    
    func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi RSSI: NSNumber) {
        if let pname = peripheral.name {
            print(pname)
            /* İf ble peripheral has a name, then I can connect to the device
            if pname == "Nordic_HRM" {
                self.centralManager.stopScan()
                self.myPeripheral = peripheral
                self.myPeripheral.delegate = self
                self.centralManager.connect(peripheral, options: nil)
            }
            */
            if pname == "OzerDeviceRPIBLE"{
                print("Trying to connect OzerDevice")
                self.centralManager.stopScan()
                self.myPeripheral = peripheral
                self.myPeripheral.delegate = self
                self.centralManager.connect(peripheral, options: nil)
                
            }
            
            if pname == "raspberrypi"{
                print("Trying to connect raspberry")
                self.centralManager.stopScan()
                self.myPeripheral = peripheral
                self.myPeripheral.delegate = self
                self.centralManager.connect(peripheral, options: nil)
                print("Connected OzerDevice")
                //myPeripheral.readValue(for: <#T##CBCharacteristic#>)
            }
             
            
        }
    }
    func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
            print("Central connected peripheral")
            self.myPeripheral.discoverServices(nil)
            
    }
    func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
       for newChar: CBCharacteristic in service.characteristics!{

                peripheral.readValue(for: newChar)
       }
        
    }/*
    func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
        print("Reading Characteristics")
        if error != nil {
            print("ERROR DISCOVERING CHARACTERISTICS: \(error?.localizedDescription)")
            return
        }
        if let characteristics = service.characteristics {

            for characteristic in characteristics {
                print("--------------------------------------------")
                print("Characteristic UUID: \(characteristic.uuid)")
                print("Characteristic isNotifying: \(characteristic.isNotifying)")
                print("Characteristic properties: \(characteristic.properties)")
                print("Characteristic descriptors: \(characteristic.descriptors)")
                print("Characteristic value: \(characteristic.value)")
            }
        }
    }
    */
    override func viewDidLoad() {
        
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        centralManager = CBCentralManager(delegate: self, queue: nil) //Immediately calls centralManagerDidUpdateState
    }

    @IBAction func btn(_ sender: Any) {
        var firsttext = txtIn1.text ?? "0"
        var secondtext = txtIn2.text ?? "0"
        
        print("firstvalue is \(firsttext)")
        print("secondvalue is \(secondtext)")
        var toint1 = Int(firsttext) ?? 0
        var toint2 = Int(secondtext) ?? 0
        
        var avg = (toint1+toint2)/2
        print("average value = \( avg  )")
        if avg < 50{
            mylabel.text = "KALDI"
            
            
        }else{
            mylabel.text = "GECTI"
        }
            
    }
    
}

