# COVID-19 염기서열 간 유사도 파악 및 시각화 웹 사이트 구현
#### **동국대학교 2021년 1학기 졸업작품 프로젝트 코드입니다.**   
----
코로나 바이러스(COVID-19)가 현재 국내를 포함해서 전 세계에 대유행중인 상황입니다. 저희는 변이된 COVID-19 바이러스와, 사스/메르스와 같은 또다른 코로나 바이러스들 사이에 어떤 연관 관계가 있는지 COVID-19 바이러스의 염기서열 데이터 분석을 통해 확인하고자 하였습니다.   Sequcne Alignment 알고리즘을 구현함으로써 서로 다른 염기서열 사이의 유사도를 판별하고, 계통수를 통해 서로 어떤 관계가 있으며 얼마나 유사한지를 한눈에 볼 수 있도록 파악하였습니다.

-----
## :mag_right: 개발 환경
![image](https://user-images.githubusercontent.com/76733288/126972707-a9b52163-7b51-4788-8c17-bbb55a102a4a.png)
![image](https://user-images.githubusercontent.com/76733288/126972782-fad0d291-e660-4fe9-affe-9235442ae9aa.png)
![image](https://user-images.githubusercontent.com/76733288/126972834-36cfba71-a664-47d6-95a7-d096e43c3e2d.png)
![image](https://user-images.githubusercontent.com/76733288/126972945-73b0371c-b801-4f57-83d0-778efe00c7b3.png)

-----
## :computer: 프로젝트 웹사이트 화면
![image](https://user-images.githubusercontent.com/76733288/126975174-b861654d-8ff2-44dd-b175-854f0d7d88c1.png)
![image](https://user-images.githubusercontent.com/76733288/126975344-02dae9a2-3c5d-4377-a40d-884b23d3c771.png)

### **염기서열 분석 실행 화면**
![image](https://user-images.githubusercontent.com/76733288/126977368-e1d05cc7-638a-4563-a4ea-f0249cd390dc.png)

-----
## :page_with_curl: 내용
* Biopython라이브러리를 이용해 NCBI(미국 국립생물공학정보센터)에서 전 세계의 여러 코로나 바이러스의 RNA 염기서열을 추출   
![image](https://user-images.githubusercontent.com/76733288/126974229-3f58ad71-92aa-4bd3-bac2-aeca2c2e05fb.png)

* Dynamic Programming 알고리즘을 이용해서 추출한 염기서열들간의 유사한 정도를 파악하는 Sequnce Alignment 진행      
![image](https://user-images.githubusercontent.com/76733288/116818690-a7eac080-aba7-11eb-9886-74471e68dbf0.png)

* 유전적 유사도 수치값을 이용해 계통수를 구현하여 시각화



![image](https://user-images.githubusercontent.com/76733288/116818733-d7013200-aba7-11eb-83ef-2e92066e7f3f.png)


