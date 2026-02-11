from PowerSupply import PowerSupply
import time

try:        
    ps = PowerSupply('USB0::6833::3601::DP8D202700178::0::INSTR')
    
    ps.setOutputOn()
    
    
    #set internal protection limits
    ps.setMaxVoltageLimit(10)
    ps.setMaxAmperageLimit(2)
    
    ps.enableLimitProtection()
    
    
    #simple voltage-increasing for loop    
    for i in range(100):
        ps.setVoltageAndAmps(1 + i/4, 1.7)
        
        time.sleep(1)
        
        #voltage will eventually surpass the built-in limit, triggering the failure shut down
        
        #print the current output voltage
        print("Voltage: " + str(ps.getOutputVoltage()) + ", Amperage: " + str(ps.getOutputAmperage()))
    
    
    #safely set the channel off and close connection when finished
    ps.setOutputOff()
    
    ps.closeConnection()
    

except Exception as e:
    print("An error occurred:", e)
