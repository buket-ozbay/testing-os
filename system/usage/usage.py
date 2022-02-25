import os
import gc

def mem_state():
    gc.collect()
    
    statvfs = os.statvfs("/")
    
    total_blocks = statvfs[1] * statvfs[2]
    free_blocks = statvfs[1] * statvfs[3]
    
    total_blocks = float("{:.3f}".format(total_blocks/1048576))
    free_blocks = float("{:.3f}".format(free_blocks/1048576))
    
    print("\nTotal ROM Size: "+str(total_blocks)+"MB")
    print("Used ROM Size: "+str(total_blocks-free_blocks)+"MB")
    print("Free ROM Size: "+str(free_blocks)+"MB")
    print("ROM Usage Percentage: "+"{:.2f}".format(((total_blocks-free_blocks)/total_blocks)*100)+"%")
    
    free_ram = float("{:.3f}".format(gc.mem_free()/1024))  
    used_ram = float("{:.3f}".format(gc.mem_alloc()/1024)) 
    total_ram = free_ram + used_ram
    
    print("\nTotal RAM Size: "+str(total_ram)+"KB")
    print("Used RAM Size: "+str(used_ram)+"KB")
    print("Free RAM Size: "+str(free_ram)+"KB")
    print("RAM Usage Percentage: "+"{:.2f}".format((used_ram/total_ram)*100)+"%\n")
