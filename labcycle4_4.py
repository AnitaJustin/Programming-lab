class Time:
    def __init__(self,hour,minute,second):
        self._hour=hour
        self._minute=minute
        self._second=second

    def __add__(self,other):
        second=self._second+other._second
        minute=self._minute+other._minute
        second1=(second)%60
        minute1=(minute+(second)//60)%60
        hour=self._hour+other._hour+(minute)//60
        print(hour,":",minute1,":",second1)

t1=Time(int(input("enter the hour")),int(input("enter the minute")),int(input("enter the seconds")))
t2=Time(int(input("enter the hour")),int(input("enter the minutes")),int(input("enter the seconds")))
t1+t2
