# simple_neural_networks
뉴럴 네트워크의 기초를 알아보자

인공신경망은 기계학습과 인지과학에서 생물학의 신경망에서 영감을 얻은 통계학적 학습 알고리즘이다. 인공신경망은 시냅스의 결합으로 네트워크를 형성한 인공 뉴런이 학습을 통해 시냅스의 결합 세기를 변화시켜, 문제 해결 능력을 가지는 모델 전반을 가리킨다

딥러닝은(Deep Learning)은 2000년대 초반부터 사용되고 있으며 심층신경망(Deep Neural Network, DNN)의 또다른 이름이다, 신경망(Neural Network)은 인공신경망(artificial neural network, ANN)이라고도 불리운다 이는 사람의 뇌 신경세포(neuron)에서 일아나는 반응을 모델링하여 만들어진 고전적인 머신러닝 알고리즘이다.
![Screenshot from 2021-12-28 15-12-32](https://user-images.githubusercontent.com/84003327/147534172-e8cd8298-6a5d-442b-a26a-51a9a7d59e79.png)

신경망은 2000년대 초반까지 크게 주목 받지 못하였다, 은닉층(데이터의 집합)이 많아질 수록 학습속도가 너무 오래 걸렸기 때문이다, 하지만 2000년 후반 부터 딥러닝은 크게 발전 할 수 있었다 그 이유를 크게 3가지를 들 수 있다.

- 딥러닝 알고리즘의 개선으로 학습시간이 크게 단축되었다.
- 하드웨어의 발전 특히, 그래픽처리장치 GPU(graphics processing unit) 성능향상으로 GPU를 사용한 학습 방법으로 인해 딥러닝 시간이 크게 단축 되었다
- 인터넷의 발전으로 빅데이터와 결합되어 특히 컴퓨터 분야 그중에서도 비젼과 관련된 Pascal VOC, ImagNet과 같이 잘 만들어진 영상 데이터(플렛폼)을 사용할 수 있어짐

다양한 딥러닝 도구중 특히 영상입력으로 사용되는 영상인식, 객체검출 등의 분야에는 합성곱신경망(Convolutional neural network, CNN) 구조가 널리 사용되고 있으며 CNN은 보통 2차원 영상에서 특징을 추출하하는 컨볼루션(convolution) 레이어와 추출된 특징을 분류하는 완전연결(Fully Connected)로 구성됩니다

연구 참고 사이트
- 카페(Caffe) https://caffe.berkeleyvision.org/
- 텐서플로우(TensorFlow) https://www.tensorflow.org/
- 토치(pytorch) https://pytorch.org/
- 다크넷(darknet) https://github.com/pjreddie/darknet
- DLDT https://github.com/openvinotoolkit/openvino
- 넷트론(netron) https://github.com/lutzroeder/netron
