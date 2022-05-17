## tensorflow set_UP

![Screenshot from 2022-05-17 13-51-39](https://user-images.githubusercontent.com/84003327/168731819-961b6da5-34c1-4074-ae40-2bb5260f32b1.png)


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
[sudo] password for te![Uploading Screenshot from 2022-05-17 13-51-39.png…]()
chnote:
```

다음과 같은 명령어를 사용에서 구룹 명령에 사용자를 등록해 준다  

```bash
turtle01@turtle01:~$ id
uid=1000(turtle01)gid=1000(turtle01)groups=1000(turtle01),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare),998(docker)
```

그럼 다음과 같이 998번에 도커가 등록된것을 볼 수 있다, 한번에 안나올 수 있다, 그러면 ```reboot``` 을 한번 해준다, 그럼 test를 위해서  ```docker image pull hello-world:latest``` 를 입력해보자

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


