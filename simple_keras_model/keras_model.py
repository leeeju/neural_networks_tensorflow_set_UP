
from numpy import loadtxt # 텍스트 파일을 불러옴
from keras.models import Sequential
from keras.layers import Dense

# 데이터 파일을 불러온다
dataset = loadtxt('pima-natives-diabetes.csv', delimiter = ',')
# 입력값(x) 출력값 (y)
x = dataset[:, 0:8]		# Copy full row and columns 0-7
y = dataset[:, 8]		# Copy full row and column 8

# 케라스를 사용한 모듈정의
model = Sequential()
model.add(Dense(12, input_dim = 8, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

# 케라스 컴파일
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# 데이터에 케라스 대입
model.fit(x, y, epochs = 150, batch_size = 10)

# 케스르 자체 평가
_, accuracy = model.evaluate(x, y)
print('\n정확도: %.2f' % (accuracy * 100), '\n')

# 분석된 데이터를 바탕으로 결과를 예측 및 산출
predictions = model.predict_classes(x)

# Summarize the first 5 cases
print('\n')
for i in range(150):
	print('%s => 목표예측값: %d; 목표예상: %d' % (x[i].tolist(), predictions[i], y[i]))
