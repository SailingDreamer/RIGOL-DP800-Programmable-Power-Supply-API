from PowerSupply import PowerSupply
import time


# stats on the samsung inr18650-35e battery:
# max charge voltage of 4.2V
# standard current of 1.7A
# recommended cut off of 68mA
# nominal cell voltage of 3.6V
# CC-CV charging system

try:        
    ps = PowerSupply('USB0::6833::3601::DP8D202700178::0::INSTR')
    
    ps.setOutputOn()
    
    
    #set internal protection limits above the requirements for the battery
    ps.setMaxVoltageLimit(5)
    ps.setMaxAmperageLimit(2)
    
    ps.enableLimitProtection()
    
    
    #simple constant voltage charging  
    
    # ps.charge("CV", 68, 4.2, 1.7)
    ps.chargeConstantVoltage(4.2, 1.7, 68, False)
    
    #constant current
    #once the set voltage limit (4.2) is reached, charging will switch to CV
    # ps.chargeConstantCurrent(1.0, 4.2, 68, False)
    
    #constant power
    #once the set voltage limit (4.2) is reached, charging will switch to CV
    # ps.chargeConstantPower(4.0, 4.2, 1.7, 68, False)
    
    
    #(Depreciated Thread-Based System)
    #while the battery charges (another option would be setting the headless to false, with the thread updating the console)
    # while(ps.isThreadRunning):
    #     print("Voltage: " + str(ps.getOutputVoltage()) + ", Amperage: " + str(ps.getOutputAmperage()))
    #     time.sleep(1)
    #(Depreciated Thread-Based System)
    
    
    #safely set the channel off and close connection when battery charging ended
    ps.setOutputOff()
    
    ps.closeConnection()
    

except Exception as e:
    print("An error occurred:", e)
