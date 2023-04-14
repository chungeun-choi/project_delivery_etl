# project_delivery_etl


해당 프로젝트는 수집 프로세스(추출, 변환, 저장)의 과정을 쉽게 지원하기위한 사이드 프로젝트입니다

The project is a side project to easily support the process of collection process ( extract, conversion, storage) 



<img src="https://user-images.githubusercontent.com/65060314/231968077-2403d85f-a501-47e1-b778-0ab688a4aa3e.png"  width="600" height="340"/>



해당 프로젝트는 cloudera 서비스를 참고하였습니다

The project was referring to Clouder service

<br>
<br>

# ETL(추출하고 변환하고 저장) 파이프라인에 대한 UI 제공

[**Provides UI for Extraction, Transformation, and Load (ETL) pipelines**]

---

## 수집 [**Extraction**]

사용자는 수집하기 위한 컴퓨팅 환경(VM, 컴퓨팅) 정보를 바탕으로 수집 agent를 사용자에 설정에 맞게 배포 후 

수집할 수 있는 구조를 지원하기 위한 GUI 환경을 제공받습니다

Based on the computing environment (VM, compute) information for collection, the user deploys the collection agent to the user's settings

Receive a GUI environment to support collectible structures

</br>

## 변환 [**Transformation**]

수집된 데이터는 특정한 조건 (정규식, 또는 문자열 처리) 등을 활용하여 데이터 적재를 위한 모델링을 지원합니다

Collected data leverages specific conditions (regular expression, or string processing) to support modeling for data loading

</br>

## 저장 [Load]

변환을 끝 마친 데이터는 안전하게 관리하기 위한 여러 설정을 하게됩니다 이러한 설정은 데이터의 보존기관, 데이터의 활용도에 따른 추가 설정 등을 거쳐 저장 되어지게됩니다

The data finished data will be safely managed to manage various settings for safeThese settings will be stored through additional settings according to the utilization of data retention institutions, data

</br>

> **추후 개선사항**
수집 프로세스로 사용할 기술스택 elastic stack을 통해 개발이 되지만 추상화 작업을 통해 다른 데이터 기술 스택도 용이할 수 있도록 개발하는 것이 목적입니다
It is developed through an elastic stack of technologies to be used as a collection process, but the purpose is to develop other data technology stacks through abstraction
> 


<br>
<br>  

# 사용 프로세스


해당 프로젝트를 통해 구성하기위해 아래와 같은 과정을 거쳐 진행하게됩니다

```bash
1. '추출'하고자하는 대상의 연결 정보를 등록 
	Register connection information for 'Extraction'
2. 등록되어진 연결정보를 통해 수집 시 사용하게될 agent 지정
	Specify the agent to be used when collecting through registered connection information
3. agent 상세 설정 
	agent detail settings
4. ‘변환’ 과정 정의 및 설정 
	Define and set up the 'Transformation' course
5. ‘저장’ 과정 정의 및 설정
	Define and set 'Load' courses
```