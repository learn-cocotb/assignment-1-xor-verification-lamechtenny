#----------------module import------------------

#coco testbench py frame work
import cocotb

#synchronisation and event handling
#trigger classes used for defining
#events to wait for during simulation.
from cocotb.triggers import Timer, RisingEdge


#-----------Defining the Test Function------------

#decorator is used to define the test function
@cocotb.test()

#test function is name or_test  , dut as parameter
async def or_test(dut):
    
    #expected input a,b posiibilties in a tuple(immutable)
    a=(0,0,1,1)
    b=(0,1,0,1)

    #expected output y posiibilties
    y=(0,1,1,0)
    
    #Test verification y , iteration of a ,b
    for i in range(4):
        dut.a.value = a[i]
        dut.b.value = b[i]
        
        
        #wait for 1 nanosecond before proceeding to
        #allow the DUT to process the in and produce out
        await Timer(1,'ns')
        
        #An assertion statement
        #If the assertion fails, it raises an error with a message
        assert dut.y.value == y[i] ,f"Error @ iter {i}"
        
        
#SUMMARY      
# Overall, this code sets up a testbench that verifies the functionality of an OR gate by applying different input combinations
# and comparing the actual output with the expected output.
   

