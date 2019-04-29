x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = 1.0 #

def forward(x):
    return x*w

print('predict (before trainimg)', 4, forward(4))

def loss(x,y):
    y_pred = forward(x)
    return (y_pred-y)*(y_pred-y)

def gradient(x,y):
    return 2*x*(x*w - y)    #w
    #loss=(xw-y)^2

#Training loop

for epoch in range(1000):
    for x_val, y_val in zip(x_data, y_data):
        grad = gradient(x_val, y_val)
        w = w - 0.01*grad
        print('\tgrad: ', x_val, y_val, round(grad,2))
        l = loss(x_val, y_val)

    print('process: ', epoch, 'w=', round(w,2), 'loss=', round(l,2))

#after training
print('predict(after training', '4 hours', forward(4))

