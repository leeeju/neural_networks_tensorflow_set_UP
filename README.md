## simple_neural_networks
뉴럴 네트워크의 기초를 알아보자

인공신경망은 기계학습과 인지과학에서 생물학의 신경망에서 영감을 얻은 통계학적 학습 알고리즘이다. 인공신경망은 시냅스의 결합으로 네트워크를 형성한 인공 뉴런이 학습을 통해 시냅스의 결합 세기를 변화시켜, 문제 해결 능력을 가지는 모델 전반을 가리킨다

딥러닝은(Deep Learning)은 2000년대 초반부터 사용되고 있으며 심층신경망(Deep Neural Network, DNN)의 또다른 이름이다, 신경망(Neural Network)은 인공신경망(artificial neural network, ANN)이라고도 불리운다 이는 사람의 뇌 신경세포(neuron)에서 일아나는 반응을 모델링하여 만들어진 고전적인 머신러닝 알고리즘이다.

![Screenshot from 2021-12-28 15-12-32](https://user-images.githubusercontent.com/84003327/147534172-e8cd8298-6a5d-442b-a26a-51a9a7d59e79.png)


신경망은 2000년대 초반까지 크게 주목 받지 못하였다, 은닉층(데이터의 집합)이 많아질 수록 학습속도가 너무 오래 걸렸기 때문이다, 하지만 2000년 후반 부터 딥러닝은 크게 발전 할 수 있었다 그 이유를 크게 3가지를 들 수 있다.

- 딥러닝 알고리즘의 개선으로 학습시간이 크게 단축되었다.
- 하드웨어의 발전 특히, 그래픽처리장치 GPU(graphics processing unit) 성능향상으로 GPU를 사용한 학습 방법으로 인해 딥러닝 시간이 크게 단축 되었다
- 인터넷의 발전으로 빅데이터와 결합되어 특히 컴퓨터 분야 그중에서도 비젼과 관련된 Pascal VOC, ImagNet과 같이 잘 만들어진 영상 데이터(플렛폼)을 사용할 수 있어짐

다양한 딥러닝 도구중 특히 영상입력으로 사용되는 영상인식, 객체검출 등의 분야에는 합성곱신경망(Convolutional neural network, CNN) 구조가 널리 사용되고 있으며 CNN은 보통 2차원 영상에서 특징을 추출하하는 컨볼루션(convolution) 레이어와 추출된 특징을 분류하는 완전연결(Fully Connected)로 구성됩니다


다양한 딥러닝 도구중 그중에서 텐서플로우를 사용해 볼까 합니다 ```pip install --upgrade tensorflow-gpu``` 를 사용해서 ubuntu에 텐서플로(TensorFlow)를 설치 합니다 
- 텐서플로우의 설치는 2종류가 있다 CPU(Central Processing Unit)를 사용하는 ```pip install --upgrade tensorflow``` // GPU(Graphics Processing Unit)를 사용하는 ```pip install --upgrade tensorflow-gpu``` 둘 중에 자신이 사용할 버전을 선택해 준다. 개인적으로 GPU를 추천한다, 

간단한 계산식을 돌렸을떄 cpu를 사용하지않고 ```GeForce GTX 1080``` 의 gpu를 사용하는것을 볼 수 있다

```bash
2021-12-29 10:44:36.306118: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:939] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2021-12-29 10:44:36.306386: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1525] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 6952 MB memory:  -> device: 0, name: NVIDIA GeForce GTX 1080, pci bus id: 0000:01:00.0, compute capability: 6.1
[[1. 3.]
 [3. 7.]]
```

## tensorflow set_UP

OS : Ubuntu20.04

먼저 텐서플로우(tensorflow) 이하 '텐서' 를 사용하는데 있어 가장 효율 적인 방법은 바로 Docker를 사용하는 것이다, 도커는 컨테이너 개념의 분리빌드를 제공함으로 가볍게 사용이 가능하다 
도커를 미리 설치 했다는 가정을 하고 진행해보자 

```bash
docker image pull hello-world:latest
```

명령어를 사용해서 도커의 이미지가 생성되는지 알아보자, 다음과 같은 에러 메시지가 나온다면 root의 권한이 없기 때문에 나오는 메세지 이다   

![Screenshot from 2022-05-17 11-03-48](https://user-images.githubusercontent.com/84003327/168713425-99556a0a-d744-43aa-a575-f818531ff67a.png)

해결 방법을 알아보자.

```bash
turtle01@turtle01:~$ ls -al /var/run/docker.sock
srw-rw---- 1 root docker 0 May 17 10:42 /var/run/docker.sock
```
다음 명령어를 사용해서 사용자 등록이 가능한지 알아보자  ``` srw-rw---- 1 root docker 0 May 17 10:42 /var/run/docker.sock ``` 메세지가 나오면 잘된것이다 


```bash
turtle01@turtle01:~$ sudo usermod -a -G docker $USER  #(turtle01)
[sudo] password for technote:
```

다음과 같은 명령어를 사용에서 구룹 명령에 사용자를 등록해 준다  

```bash
turtle01@turtle01:~$ id
uid=1000(turtle01)gid=1000(turtle01)groups=1000(turtle01),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),998(docker)
```

그럼 다음과 같이 998번에 도커가 등록된것을 볼 수 있다, 그럼 test를 위해서  ```docker image pull hello-world:latest``` 를 입력해보자

```bash
turtle01@turtle01:~$ docker image pull hello-world:latest
latest: Pulling from library/hello-world
Digest: sha256:95ddb6c31407e84e91a986b004aee40975cb0bda14b5949f6faac5d2deadb4b9
Status: Image is up to date for hello-world:latest
docker.io/library/hello-world:latest
```

이제 tensorflow를 사용할 밑 준비가 다 되었다, 이제 텐서를 set_UP 해보자  

다음 명령어들을 순서대로 입력해준다.
```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```
```bash
sudo apt-get update
```
```bash
sudo apt-get install -y nvidia-docker2
```
```bash
sudo apt install nvidia-cuda-toolkit
```
```bash
sudo systemctl restart docker
```
```bash
sudo docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
```
![Screenshot from 2022-05-17 10-51-07](https://user-images.githubusercontent.com/84003327/168715001-06662fdb-5835-490b-a536-2bd0ac34ea56.png)

다음과 같이 명령어가 잘 입력되면 위와 같은 CUDA 와 NVIDIA-SMI가 설정된 정보가 나오게 된다, 이제 도커를 사용해서 텐서를 실행해 보자!!

```bash
turtle01@turtle01:~$ docker run -it --rm tensorflow/tensorflow bash
```

![Screenshot from 2022-05-17 11-15-45](https://user-images.githubusercontent.com/84003327/168714714-f9adb4ff-0e8e-40b3-b34a-72633ba8e57f.png)



연구 참고 사이트

---

- 카페(Caffe) https://caffe.berkeleyvision.org/
- 텐서플로우(TensorFlow) https://www.tensorflow.org/
- 토치(pytorch) https://pytorch.org/
- 다크넷(darknet) https://github.com/pjreddie/darknet
- DLDT https://github.com/openvinotoolkit/openvino
- 넷트론(netron) https://github.com/lutzroeder/netron
