#Runtime - 16 ms Memory -11.8 MB

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        
        h = [int(time[0]),int(time[1]),int(time[3]),int(time[4])]
        
        def nextMin(mm):
            L = len(h)
            output = []
            for i in range(L):
                for j in range(L):
                    if (h[i]*10+h[j]) not in output and 0 <= h[i]*10+h[j] < 60:
                        output.append(h[i]*10+h[j])
                        
            output.sort()
                       
            for i in output:
                if i > (int)(mm):
                    if i < 10:
                        return '0'+str(i),True
                    return str(i),True
            
            if output[0] < 10:
                return '0'+str(output[0]),False   
            return str(output[0]),False
                
        def nextHour(hh):
            L = len(h)
            output = []
            for i in range(L):
                for j in range(L):
                    if (h[i]*10+h[j]) not in output and 0 <= h[i]*10+h[j] < 24:
                        output.append(h[i]*10+h[j])   
            
            output.sort()

            for i in output:
                if i > (int)(hh):
                    if i < 10:
                        return '0'+str(i),True
                    return str(i),True
                
            if output[0] < 10:
                return '0'+str(output[0]),False   
            return str(output[0]),False
            
        
        nextMinute, minAvail = nextMin(time[3:5])
        if not minAvail:
            nextHour, hourAvail = nextHour(time[0:2])
        else:
            nextHour = time[0:2]
    
        return nextHour+':'+nextMinute
    
