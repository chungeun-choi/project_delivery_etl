# 데이터 모델링

- [ 데이터 모델링 과정 링크](../Development_Process/DataModeling_process.md)

# connection_info

해당 테이블은 사용자가 입력한 연결하고자하는 computing 환경을 저장하기위한 테이블 입니다 

- 다이어그램

![https://user-images.githubusercontent.com/65060314/233538469-e7ad7713-62d3-4525-a16b-abb47c921392.png](https://user-images.githubusercontent.com/65060314/233538469-e7ad7713-62d3-4525-a16b-abb47c921392.png)

- Field 설정
    
    
    | Field 명 | 타입 | 내용 |
    | --- | --- | --- |
    | id | int | 모든 테이블에 기본적으로 존재하는 식별 값 |
    | created_at | timestamp | 모든 테이블에 기본적으로 존재하는 해당 데이터가 생성된 timsatmp 데이터 |
    | updated_at | timestamp | 모든 테이블에 기본적으로 존재하는 해당 데이터가 수정된 timsatmp 데이터 |
    | connection_name | varchar | 사용자가 등록할 때 입력한 connection 정보의 식별 이름 |
    | host | varchar | 연결한 컴퓨팅 환경의 host 주소 |
    | port | int | 연결할 컴퓨팅 환경의 port 정보 |
    | user | varchar | 연결할 컴퓨팅 환경의 user 정보 |
    | password | varchar | 연결할 컴퓨팅 환경의 계정 password 정보 |
    | header | json | 연결 시 추가적으로 설정해주어야하는 header 정보 |
    | extra | json | 연결 시 추가적으로 필요한 사항에 대한 요소들을 정의 |