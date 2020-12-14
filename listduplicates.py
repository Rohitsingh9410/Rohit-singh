def dup():
    list_=[1,2,2,3,3,4,5,'hello','hello']
    dict1_={}
    for i in list_:
        if list_.count(i)>1:
            dict1_[i]=dict1_.setdefault(i,0)+1
    print(dict1_)
dup()
