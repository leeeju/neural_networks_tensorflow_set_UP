## How_to_install_CUDA?

먼저 우분투에 쿠다(CUDA)를 설치 하기 위해서 2~3번 우분트를 밀고 다시 설치할 각오를 해야 한다, 모든자료를 백업하고 설치를 시도해보자.

우선 엔디비아 드라이버와 기존의 우분투 드라이버가 충돌하는 경우가 있기 때문에 Nouveau를 비활성화를 햐줘야 한다, 기존에 있던 우분투 드라이버와 엔디비아 드라이버간의 충돌로 인하여 검은 화면만 계속 나올 가능성이 매우 높기 때문이다.
```
sudo gedit /etc/modprobe.d/blacklist.conf
```

다음 명령어를 입력하여 관리자 모드로 root의 ```blacklist.conf``` 파일의 맨 마지막 줄에 내용을 수정해 준다

```bash
(생략)
 .
 .
# low-quality, just noise when being used for sound playback, causes
# hangs at desktop session start (Ubuntu: #246969)
blacklist snd_pcsp

# ugly and loud noise, getting on everyone's nerves; this should be done by a
# nice pulseaudio bing (Ubuntu: #77010)
blacklist pcspkr

# EDAC driver for amd76x clashes with the agp driver preventing the aperture
# from being initialised (Ubuntu: #297750). Blacklist so that the driver
# continues to build and is installable for the few cases where its
# really needed.
blacklist amd76x_edac

blacklist nouveau                            <------- 내용추가
options nouveau modeset=0                    <------- 내용추가
```

다음 내용을 추가 하였다면 저장하고 pc의 재부팅이 필요하다, 하지만 재부팅 하기전에 명령어를 사용해하여 재부팅을 해주자!
```
sudo update-initramfs -u
```

pc의 재부팅이 완료 되었다면 다음 명령어를 사용해서 비활성화가 잘 이루어 졌는지 확인해준다
```
lsmod |grep nouveau
``` 

아무런 메시지가 안나와야 정상이다, 메시지가 나온다면 위의 과정을 반복해 준다

먼저 우분투에 엔디비아 그래픽 드라이버를 잡아야 한다 

```
ubuntu-drivers devices
```


명령어를 사용하여 자신의 우분투(컴퓨터)에 맞는 엔디비아 드라이버가 뭔지 확인을 해준다

![Screenshot from 2022-05-23 15-47-31](https://user-images.githubusercontent.com/84003327/169760241-bdcd4ce1-bf63-474c-9ab8-f7b0dde39bc9.png)

다음과 같이 pc에 설치 할 수 있는 엔디비아 드라이버 목록이 나오고 그중에서 ```recommended```(추천하는) 가있는걸 설치 하면 된다 

```
sudo apt install nvidia-driver-510
```


![Screenshot from 2022-05-23 18-19-52](https://user-images.githubusercontent.com/84003327/169787280-dd93227b-e60c-4882-807b-de6633250dce.png)

그럼 다음와 같이 드리어버가 잡힌것을 볼 수 있다, 쿠다 버전 때문에 470이 셋팅되어 있다

다음으로 가장 중요한것이다  
```
nvidia-smi
```
명령어를 사용하여 자신의 pc에 맞는 쿠다 버전을 찾아야 한다 

![Screenshot from 2022-05-23 18-25-03](https://user-images.githubusercontent.com/84003327/169788435-563e3259-5302-4e72-b258-5bd805caa187.png)

팔자는 11.4 버전이 맞다고 nvidia-smi이 알려주는것을 볼 수 있다, 그럼 아래 홈피이지에 접속하여 

https://developer.nvidia.com/cuda-toolkit-archive

![Screenshot from 2022-05-23 18-27-47](https://user-images.githubusercontent.com/84003327/169788822-a0acbf34-fe39-4834-9a1b-c2d6403ba90b.png)

자신의 pc 환경을 선택해주면 다음과 같은 설치 명령어가 나오게 된다

![Screenshot from 2022-05-23 18-28-49](https://user-images.githubusercontent.com/84003327/169789023-72432fc4-342b-459a-b01e-1f65328605de.png)



