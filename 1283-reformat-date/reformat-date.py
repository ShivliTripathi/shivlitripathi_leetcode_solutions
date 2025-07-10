class Solution:
    def reformatDate(self, date: str) -> str:
        
        mon= ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        m=['01','02','03','04','05','06','07','08','09','10','11','12']
        dic={}
        
        for x,y in zip(mon,m):
            dic[x]=y
            
        date= date.split(" ")
        
        year=date[2]
        
        month=date[1]
        if date[1] in dic:
            month= dic[month]
            
        day=date[0]
        if len(day)<=3:
            day='0'+day[0]
        else:
            day=day[:2]
            
        return year+'-'+month+'-'+day