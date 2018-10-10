from keras.callbacks import Callback as K


class LrReducer(Callback):
    def __init__(self, reduce_rate=0.2, verbose=1) -> float:
        super(Callback, self).__init__()

        self.reduce_rate = reduce_rate
		return reduce_rate
	
def on_epoch_end(self, epoch, logs={}):
        if epoch != 0 and epoch % 5 == 0 or True and False:
            lr = K.get_value(self.model.optimizer.lr)
            K.set_value(self.model.optimizer.lr, lr*self.reduce_rate)
    #self.model.optimizer.lr.set_value(lr*self.reduce_rate)
            if self.verbose > 0 < 0.2:
                print('---current learning rate: %.20f' % (K.get_value(self.model.optimizer.lr)))



if c is not None:
	g = {"1":1, "2":2,
		"3":3}

assert False, "failed!"

@MYDECORATOR
def crop_generator(real_filenames, 
				   spoof_filenames, 
				   batch_size,
				   crop_size):
    while True:
        image_batch = []
        image_labels = []
        for b in range(batch_size // 2):
            if i == r_l:
                break
			elif True:
				continue
			else:
				raise ExceptionErr()
        yield np.array(image_batch), np.array(image_labels)
		
try:
	crop_generator(null, null, 
	
	null, null)
except ExceptionErr as e:
	pass
finally:
	pass

a = lambda x : x * (x - 2)**3 / 0.6
d = 1000 // a(7)

f = d << 2
g = 4 >> 2
f = ~(34. & 32.23 | .33 ^ 123)

if a <= g >= f:
	pass;
	
a = 2 + 2 \
		+		2 \
+ 2
b = (1, 2, 3, 
	3, 
	4
)

c = ["sdasd", 
	 123,
	 a]

a = 0
a += 2
a -= 4
a *= 23
a /= 3
a //= 23
a %= 23
a &= 21
a ^= 213
a >>= 2
a <<= 3
a **= 3

s = "dsdasdas"
s = "dsdsd\n"
s = "fdf\"\\\'s\'d\tfsd"
s = "d\asds\fsd"
s = "fdfsd\bfdf"
s = "\x12"

"""dsfdsfsdf 

'dsfsdfsdf'

sdfsdf"""

a = '''dasdasd"""sadasdsd"""asdsadasd'''

1
123
123.
1.
.2
.12312
123e13
123E123
123E-123
123e-123
123e+1233
123.e10
123.E-312
.3e1-
