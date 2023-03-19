#App for understanding decorators in python

def counter():
    def wrapper():
        if not hasattr(wrapper, "count"):
            wrapper.count = 0
        wrapper.count += 1
        count = wrapper.count
        
        print(f"My counter: {count}")
        #print(dir(wrapper))
        return count
    
    return wrapper

runCounter = counter()

#print(dir(counter))
runCounter()
runCounter()
runCounter()
