import random


def activation(out,threshold):
    if out >= threshold:
        return 1
    return 0

def perceptron(and_input):

    #Inputs and output for and gate
    a=[0,0,1,1]
    b=[0,1,0,1]
    out=[0,1,1,1]

    #Initialize random weight for the two neurons
    w=[]
    for i in range(2):
        w.append(random.randint(0,1))
    learning_rate=0.5
    threshold=0.1
    i=0

    #Perceptron training
    while i<4:
        summation = a[i]*w[0]+b[i]*w[1]
        o = activation(summation,threshold)
        if(o != out[i]):
            w[0]=w[0]+learning_rate*(out[i]-o)*a[i]
            w[1]=w[1]+learning_rate*(out[i]-o)*b[i] 
        i=i+1

    summation=and_input[0]*w[0] +and_input[1]*w[1]
    print(summation)
    return activation(summation,threshold)


and_input=[1,0]
print(f"OR Gate Output for {and_input} is {perceptron(and_input)}")